import time
import random
import pandas as pd
from pyflink.datastream import StreamExecutionEnvironment
from pyflink.datastream.window import GlobalWindows, Trigger, TriggerResult
from pyflink.datastream.state import ValueStateDescriptor
from pyflink.common.typeinfo import Types
from datetime import datetime

# 트리거 클래스 (Trigger)
class CustomCountTrigger(Trigger):
    def __init__(self, count_threshold):
        super().__init__()
        self.count_threshold = count_threshold  # 일정 개수 도달 시 실행

    @staticmethod
    def of(count_threshold):
        return CustomCountTrigger(count_threshold)

    def on_element(self, element, timestamp, window, ctx):
        """ 새 데이터가 들어올 때마다 트리거 실행 여부 확인 """
        count_state_desc = ValueStateDescriptor("count", Types.INT())  
        count_state = ctx.get_partitioned_state(count_state_desc)

        current_count = count_state.value() or 0  
        current_count += 1
        count_state.update(current_count)

        if current_count >= self.count_threshold:
            count_state.clear()  
            return TriggerResult.PURGE  # 트리거 실행 후 윈도우 초기화
        return TriggerResult.CONTINUE  # 현재 윈도우를 유지하고 아무 작업도 수행하지 않음


    def on_processing_time(self, time, window, ctx):
        return TriggerResult.CONTINUE

    def on_event_time(self, time, window, ctx):
        return TriggerResult.CONTINUE

    def on_merge(self, window, ctx):
        return TriggerResult.CONTINUE

    def clear(self, window, ctx):
        """ 윈도우 종료 시 상태 초기화 """
        count_state_desc = ValueStateDescriptor("count", Types.INT())
        ctx.get_partitioned_state(count_state_desc).clear()

def format_time(record):
    ts = datetime.fromtimestamp(record[2]).strftime("%H:%M:%S")
    return (record[0], record[1], ts)

# 실행 환경 설정
def main():
    env = StreamExecutionEnvironment.get_execution_environment()
    env.set_parallelism(1)

    # CSV 데이터 로드
    df = pd.read_csv("/home/ssafy/101_offline_sh/day_9_d_Flink/data_engineering1_ws_9_4/data/data.csv")
    transactions = df[['transaction_id', 'amount']].dropna().values.tolist()

    # 랜덤 타임스탬프 추가 (현재 시간에서 최대 1시간 전까지)
    transactions = [(t[0], t[1], time.time() - random.randint(0, 3600)) for t in transactions]  

    # 전체 스트림을 미리 필터링한 후 stream으로 넘김
    now = time.time()
    filtered_transactions = [t for t in transactions if now - t[2] <= 1800]

    # 위에서 필터링된 리스트를 stream으로 생성
    transaction_stream = env.from_collection(
        filtered_transactions, 
        type_info=Types.TUPLE([Types.STRING(), Types.FLOAT(), Types.FLOAT()])
    )

    # 사람이 읽기 좋은 시간으로 변환
    formatted_stream = transaction_stream.map(
        format_time,
        output_type=Types.TUPLE([Types.STRING(), Types.FLOAT(), Types.STRING()])
    )
    formatted_stream.print("Filtered Data")

    # 트리거 적용 (3개 데이터 도달 시 실행)
    windowed_stream = (
        transaction_stream
        .window_all(GlobalWindows.create())  # 전체 데이터를 단일 윈도우에서 처리
        .trigger(CustomCountTrigger.of(3))  # 3개가 쌓이면 트리거 실행
        .reduce(lambda a, b: (a[0], a[1] + b[1], time.time()))  # 거래 금액 합산
        .map(lambda x: (x[0], x[1], datetime.fromtimestamp(x[2]).strftime("%H:%M:%S")),
         output_type=Types.TUPLE([Types.STRING(), Types.FLOAT(), Types.STRING()]))
    )


    # 결과 출력
    windowed_stream.print("Final Result")

    # 실행
    env.execute("Evictor and Trigger Example")


if __name__ == "__main__":
    main()
