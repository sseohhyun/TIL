import time
import pandas as pd
from pyflink.datastream import StreamExecutionEnvironment
from pyflink.datastream.window import ProcessingTimeSessionWindows
from pyflink.common.time import Time
from pyflink.common.typeinfo import Types

def delayed_map(record):
    """
    세윈도우 테스트를 위해 데이터별 딜레이 설정
    - 특정 값에 대해 처리 지연을 적용하여 윈도우 동작 확인
    """
    if record[1] < 2000:
        time.sleep(0.5)  # 짧은 지연
    elif 2000 <= record[1] < 5000:
        time.sleep(1.5)  # 중간 지연
    else:
        time.sleep(3)  # 긴 지연 (새로운 세션 발생 가능)
    return record

def main():
    env = StreamExecutionEnvironment.get_execution_environment()
    env.set_parallelism(1)

    # CSV 데이터 로드
    df = pd.read_csv("/home/ssafy/101_offline_sh/day_9_d_Flink/data_engineering1_ws_9_2/data/data.csv")
    transactions = df[['transaction_id', 'amount']].dropna().values.tolist()

    # Flink 데이터 스트림 생성
    data_stream = env.from_collection(   # 데이터를 Flink 스트림으로 변환하는 메서드
        transactions,
        type_info=Types.TUPLE([Types.STRING(), Types.FLOAT()])
    )

    # 데이터 지연 적용 (이벤트 발생 간격 조정)
    delayed_stream = data_stream.map(delayed_map, # 변환 연산을 통해 데이터별로 지정된 지연 시간을 적용
                                      output_type=Types.TUPLE([Types.STRING(), Types.FLOAT()]))  
    

    # 세션 윈도우 적용 (2초 간격)
    windowed_stream = (
        delayed_stream
        .key_by(lambda x: x[0])  # 데이터를 그룹화할 키를 지정하는 부분
        .window(ProcessingTimeSessionWindows.with_gap(Time.seconds(2)))  # 일정 시간 동안 데이터가 없으면 새로운 윈도우를 시작하는 방식(세션윈도우 생성)
        .reduce(lambda a, b: (a[0], a[1] + b[1]))
    )

    # 결과 출력
    windowed_stream.print()

    # 실행
    env.execute("Session Window Example")

if __name__ == "__main__":
    main()
