"""
목표: Kafka로부터 클릭 이벤트 데이터를 실시간으로 수집하고,
      Spark Structured Streaming으로 이벤트 유형별 집계를 수행한다.

학습내용:
1. SparkSession 생성 및 Kafka 연동
2. readStream, selectExpr, from_json 등의 메서드 사용법
3. withWatermark + groupBy + agg 구조 학습
4. writeStream 구성 이해

아래의 메서드 호출 부분(____)을 채우세요.
"""

from pyspark.sql import SparkSession
from pyspark.sql.functions import *
from pyspark.sql.types import *


def create_spark_session():
    # SparkSession 생성 (Kafka 패키지 포함)
    return SparkSession.builder \
        .appName("ClickEventStream") \
        .config("spark.jars.packages", "org.apache.spark:spark-sql-kafka-0-10_2.12:3.5.0") \
        .getOrCreate()  # SparkSession을 실제로 생성하는 메서드


def process_click_stream():
    spark = create_spark_session()

    # (1) Kafka에서 실시간 스트림 읽기
    df = (
        spark.readStream  # 실시간 데이터 읽기용 메서드 (read / readStream 중 선택)
        .format("kafka")  # 데이터 소스 형식 지정
        .option("kafka.bootstrap.servers", "localhost:9092")
        .option("subscribe", "click-events")
        .option("startingOffsets", "latest")
        .load()  # 스트림 로드 메서드
    )

    # (2) Kafka의 value는 binary → 문자열로 변환
    value_df = df.selectExpr("CAST(value AS STRING)")  # selectExpr() 메서드 호출

    # (3) JSON 스키마 정의
    schema = StructType([
        StructField("user_id", StringType(), True),
        StructField("page", StringType(), True),
        StructField("event_type", StringType(), True),
        StructField("timestamp", TimestampType(), True)
    ])

    # (4) JSON 파싱
    parsed_df = (
        value_df.select(from_json(col("value"), schema).alias("data"))  # select() 메서드 호출
        .select("data.*")  # select()로 구조체 컬럼 펼치기
    )

    # (5) 이벤트 시간 기반 집계 (1분 윈도우 + event_type별)
    result_df = (
        parsed_df
        .withWatermark("timestamp", "2 minutes")  # 워터마크 지정 메서드
        .groupBy(window("timestamp", "1 minute"), col("event_type"))  # 그룹화 메서드
        .agg(  # 집계 메서드
            count("*").alias("event_count"),
            approx_count_distinct("user_id").alias("unique_users")
        )
    )

    # (6) 콘솔 출력 스트림 시작
    query = (
        result_df.writeStream  # 쓰기 시작 객체 접근 (writeStream)
        .outputMode("complete")  # 출력 모드 지정
        .format("console")  # 출력 형식 지정
        .option("truncate", "false")
        .start()  # 스트리밍 실행 메서드
    )

    query.awaitTermination()  # 쿼리 종료까지 대기하는 메서드


if __name__ == "__main__":
    process_click_stream()
