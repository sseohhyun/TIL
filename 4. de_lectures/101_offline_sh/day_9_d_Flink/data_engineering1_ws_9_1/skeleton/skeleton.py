import time
import pandas as pd
from pyflink.datastream import StreamExecutionEnvironment
from pyflink.datastream.window import TumblingProcessingTimeWindows
from pyflink.common.time import Time
from pyflink.common.typeinfo import Types

def delayed_map(record):
    """
    데이터 발생 시점을 조정하기 위한 지연 함수.
    모든 데이터에 동일한 간격으로 지연을 추가함.
    """
    time.sleep(1)
    return record

def main():
    # Flink 실행 환경 설정
    env = StreamExecutionEnvironment.get_execution_environment()  # Flink 실행 환경을 가져오는 메서드
    env.set_parallelism(1)

    # CSV 데이터 로드
    df = pd.read_csv("/home/ssafy/101_offline_sh/day_9_d_Flink/data_engineering1_ws_9_1/data/data.csv")
    transactions = df[['transaction_id', 'amount']].dropna().values.tolist()

    # Flink 데이터 스트림 생성
    data_stream = env.from_collection(
        transactions,
        type_info=Types.TUPLE([Types.STRING(), Types.FLOAT()])  # 데이터 타입을 지정(문자열)
    )

    # 데이터 지연 적용
    delayed_stream = data_stream.map(   # 데이터 발생 시점을 일정하게 조정
        delayed_map,
        output_type=Types.TUPLE([Types.STRING(), Types.FLOAT()])
    )

    # 텀블링 윈도우 적용 (5초 단위)
    windowed_stream = (
        delayed_stream
        .key_by(lambda x: x[0])  # 거래 ID 기준 그룹화
        .window(TumblingProcessingTimeWindows.of(Time.seconds(5)))  # 고정된 크기의 윈도우를 생성하여 데이터를 그룹화하는 방식(텀블링 윈도우우)
        .reduce(lambda a, b: (a[0], a[1] + b[1]))  # 그룹 내 데이터를 집계하는 연산
    )

    # 결과 출력
    windowed_stream.print()

    # 실행
    env.execute("Tumbling Window Example")

if __name__ == "__main__":
    main()
