from pyspark.sql import SparkSession
from pyspark.sql.functions import *
from pyspark.sql.types import *
import findspark

# 로컬 Python 환경에서 Spark를 사용할 수 있도록 초기화
findspark.init()

# 배치 코드를 스트리밍 코드로 거의 그대로 재사용할 수 있게 하자."
# 이게 Structured Streaming의 설계 철학이기 때문에 Dataframe API와 거의 흡사하게 생겼음

## -----------------------------------------------------
# 1. Spark 세션 생성 함수
# PySpark 애플리케이션의 시작점이며, Kafka와 연동하기 위한 패키지를 등록해야 함
# -----------------------------------------------------
def create_spark_session():
    return SparkSession.builder \
        .appName("KafkaSparkStreaming") \  # Web UI나 로그에서 보이는 이름
        .config("spark.jars.packages",     # Kafka 연동을 위해 필요한 패키지를 자동으로 다운로드
                "org.apache.spark:spark-sql-kafka-0-10_2.12:3.5.0") \
        .getOrCreate()

# -----------------------------------------------------
# 2. Kafka 스트리밍 데이터 처리 함수
# 실시간 Kafka 메시지를 수신하고, 시간 기반으로 집계하여 콘솔에 출력
# -----------------------------------------------------
def process_kafka_stream():
    # [1] Spark 세션 생성
    spark = create_spark_session()

    # [2] Kafka로부터 실시간 데이터를 읽기 위한 스트리밍 소스 정의
    # Kafka 메시지는 key-value 구조를 가지며, value에 실제 데이터가 들어있음
    df = spark 
        .readStream                                # 스트리밍 처리임을 명시 (read → readStream 차이 주목)
        .format("kafka")                           # 소스는 Kafka
        .option("kafka.bootstrap.servers", "localhost:9092")   # Kafka 브로커 주소
        .option("subscribe", "test-topic")         # 구독할 Kafka 토픽 이름
        .option("startingOffsets", "latest")       # 'latest'는 현재 이후 메시지만 처리함
        .load()                                     # 정의된 옵션을 기반으로 Kafka에서 메시지 수신

    # [3] Kafka 메시지의 value는 binary (bytes)이므로 문자열로 변환
    # Kafka는 key, value 모두 기본적으로 바이너리이기 때문
    value_df = df.selectExpr("CAST(value AS STRING)")

    # [4] Kafka 메시지 내부는 JSON 문자열이라고 가정하고, 그 구조를 정의함
    # JSON → Row 변환을 위해 스키마를 반드시 명시해야 함
    schema = StructType([
        StructField("timestamp", TimestampType(), True),  # 이벤트 발생 시각 (문자열 아님!)
        StructField("message", StringType(), True)        # 본문 내용
    ])

    # [5] value 컬럼에 있는 JSON 문자열을 스키마 기반으로 구조화함
    # from_json: 문자열 JSON을 구조화된 컬럼으로 파싱하는 함수
    parsed_df = value_df.select(
        from_json(col("value"), schema).alias("data")  # JSON 파싱 결과를 "data" 컬럼에 담음
    ).select("data.*")  # "data" 구조체를 풀어헤쳐 실제 컬럼(timestamp, message)로 만듦

    # [6] 이벤트 발생 시간(timestamp)을 기준으로 1분 단위 윈도우를 설정하고 집계
    # watermark는 지연 허용 설정으로, "1분까지 늦게 도착한 데이터도 포함하겠다"는 의미
    # window는 타임스탬프 컬럼을 기반으로 시간 창을 나누는 함수
    # "현재 처리 시각(처리된 최대 이벤트 시각) 기준으로, 최대 1분까지 늦게 들어온 이벤트는 인정하겠다."
    # 즉, 이벤트의 timestamp 값이 기준
    # 그 시점으로부터 1분 이상 늦게 들어온 데이터는 무시
    # 이벤트 시간(timestamp 컬럼)을 기준으로 1분짜리 시간 구간(윈도우)을 나눠서 데이터를 그룹핑하겠다
    result_df = parsed_df \
        .withWatermark("timestamp", "1 minute") \
        .groupBy(window("timestamp", "1 minute")) \  # 1분 단위 시간 창 생성
        .count()  # 각 윈도우(시간 창) 내에서 메시지 수 계산

    # [7] 실시간 집계된 결과를 콘솔에 출력하도록 스트리밍 Sink 설정
    # outputMode:
    #   - complete: 모든 윈도우 결과를 계속 출력 (전체 집계 결과가 매번 출력됨)
    #   - append: 결과가 확정된(더 이상 업데이트되지 않을) 윈도우만 출력
    query = result_df \
        .writeStream \
        .outputMode("complete") \       # 모든 결과를 계속 보여줌 (학습용으로 적합)
        .format("console") \            # 콘솔에 출력
        .start()                        # 스트리밍 시작

    # [8] 프로그램이 종료되지 않도록 무한 대기 (Ctrl+C로 종료 가능)
    query.awaitTermination()

# -----------------------------------------------------
# 3. 메인 함수 실행
# Python 파일을 직접 실행할 때만 스트리밍 로직이 동작하도록 함
# -----------------------------------------------------
if __name__ == "__main__":
    process_kafka_stream()
    
    """
    -------------------------------------------                                     
Batch: 1
-------------------------------------------
+--------------------+-----+
|              window|count|
+--------------------+-----+
|{2025-04-20 22:50...|    1|
+--------------------+-----+

-------------------------------------------                                     
Batch: 2
-------------------------------------------
+--------------------+-----+
|              window|count|
+--------------------+-----+
|{2025-04-20 22:52...|    2|
|{2025-04-20 22:51...|    2|
|{2025-04-20 22:50...|    4|
|{2025-04-20 22:49...|    2|
|{2025-04-20 22:53...|    2|
+--------------------+-----+

-------------------------------------------                                     
Batch: 3
-------------------------------------------
+--------------------+-----+
|              window|count|
+--------------------+-----+
|{2025-04-20 22:52...|    2|
|{2025-04-20 22:51...|    5|
|{2025-04-20 22:49...|    3|
|{2025-04-20 22:50...|    4|
|{2025-04-20 22:53...|    5|
+--------------------+-----+

trigger 주기마다 한 번씩 데이터를 수집 → 처리 → 결과 출력하는 과정 중

Batch 1, Batch 2, Batch 3는 각각의 처리 타이밍

window는 window("timestamp", "1 minute")로 정의한 시간 창

count는 해당 윈도우에 포함된 메시지 개수

22:50:00 ~ 22:51:00 구간에 메시지 4개

22:51:00 ~ 22:52:00 구간에 메시지 2개

...

이렇게 각 1분 단위로 윈도우를 자르고,
각 윈도우에 해당하는 메시지를 카운트한 것

🔹 왜 같은 윈도우가 여러 배치에 반복될까?
outputMode("complete")이기 때문에, 전체 결과를 매번 덮어서 출력

즉, 새로운 메시지가 오면 기존 윈도우도 다시 출력됨

이건 정합성 유지를 위해 일부러 그렇게 설계된 동작입니다

    """