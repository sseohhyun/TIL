import time
import pandas as pd
from datetime import datetime
from pyflink.datastream import StreamExecutionEnvironment
from pyflink.common.watermark_strategy import WatermarkStrategy, TimestampAssigner
from pyflink.datastream.window import TumblingEventTimeWindows
from pyflink.common import Duration, Time
from pyflink.common.typeinfo import Types
from pyflink.datastream.functions import AggregateFunction


# TimestampAssigner (타임스탬프를 데이터에서 추출)
class CustomTimestampAssigner(TimestampAssigner):
    def extract_timestamp(self, element, record_timestamp):
        """ 데이터에서 타임스탬프 값을 추출하여 Flink 내부 시간 기준으로 설정 """
        return element[1]


# AggregateFunction (최적화된 윈도우 연산)
class SumAggregate(AggregateFunction):
    def create_accumulator(self):
        """ 초기값 설정 (거래 금액 합산을 위한 누적값) """
        return 0

    def add(self, value, accumulator):
        """ 데이터가 들어올 때마다 거래 금액을 누적 """
        return accumulator + value[2]

    def get_result(self, accumulator):
        """ 최종 결과 반환 (누적된 총 거래 금액) """
        return accumulator # 누적된 총 거래 금액 반환

    def merge(self, acc1, acc2):
        """ 병렬 처리를 위해 여러 누적값을 병합 (reduce보다 더 효율적) """
        return acc1 + acc2


def main():
    # Flink 실행 환경 설정
    env = StreamExecutionEnvironment.get_execution_environment()
    env.set_parallelism(2)  # 병렬성 증가 (속도 향상)

    # CSV 데이터 로드
    df = pd.read_csv("/home/ssafy/101_offline_sh/day_9_d_Flink/data_engineering1_ws_9_3/data/data.csv")

    # 데이터에서 거래 ID, 타임스탬프, 금액 정보 추출
    transactions = df[['transaction_id', 'timestamp', 'amount']].dropna().values.tolist()

    # 타임스탬프 변환 (밀리초 단위)
    transactions = [(str(t[0]), int(datetime.strptime(t[1], "%Y-%m-%d %H:%M:%S").timestamp() * 1000), float(t[2])) for t in transactions]

    # Flink 데이터 스트림 생성
    source = env.from_collection(
        transactions,
        type_info=Types.TUPLE([Types.STRING(), Types.LONG(), Types.FLOAT()])
    )

    # 워터마크 전략 설정 (최대 1초의 지연 허용)
    watermark_strategy = (
        WatermarkStrategy.for_bounded_out_of_orderness(Duration.of_seconds(1))
        .with_timestamp_assigner(CustomTimestampAssigner())  # 커스텀 타임스탬프 할당기 적용
    )

    # 타임스탬프 및 워터마크 할당
    watermarked_stream = source.assign_timestamps_and_watermarks(watermark_strategy)

    # 기존 방식: Reduce 연산을 사용한 윈도우 집계 (메모리 사용량 증가)
    regular_window_stream = (
        watermarked_stream
        .key_by(lambda x: x[0])  # 거래 ID 기준 그룹화
        .window(TumblingEventTimeWindows.of(Time.seconds(5)))  # 5초 단위 윈도우
        .reduce(lambda a, b: (a[0], a[1], a[2] + b[2]))  # 모든 데이터를 유지한 채 합산 (메모리 사용량 증가)
    )

    # 최적화된 방식: AggregateFunction을 사용한 윈도우 집계 (메모리 절약 및 속도 향상)
    optimized_window_stream = (
        watermarked_stream
        .key_by(lambda x: x[0])  # 거래 ID 기준 그룹화
        .window(TumblingEventTimeWindows.of(Time.seconds(5)))  # 5초 단위 윈도우
        .aggregate(SumAggregate())  # AggregateFunction 사용하여 부분 결과만 유지 (성능 개선)
    )

    # 결과 출력 (두 방식의 차이 비교)
    regular_window_stream.print("Regular Window")  # 기존 방식
    optimized_window_stream.print("Optimized Window")  # 최적화된 방식

    # 실행 메서드 호출
    env.execute("Optimized Window Processing Example")


if __name__ == "__main__":
    main()
