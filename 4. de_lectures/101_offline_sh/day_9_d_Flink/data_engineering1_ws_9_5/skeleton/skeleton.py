import json
import os
from datetime import datetime
from pyflink.datastream import StreamExecutionEnvironment
from pyflink.datastream.connectors import FlinkKafkaConsumer
from pyflink.datastream.window import TumblingEventTimeWindows
from pyflink.datastream.functions import AggregateFunction, ProcessFunction
from pyflink.common import Configuration, Duration
from pyflink.common.time import Time
from pyflink.common.serialization import SimpleStringSchema
from pyflink.common.typeinfo import Types
from pyflink.common.watermark_strategy import WatermarkStrategy, TimestampAssigner


# ---------------------------------------------------------------------
# 사용자 정의 TimestampAssigner 클래스
# Kafka에서 수신한 JSON 메시지의 timestamp 필드 값을 이벤트 타임으로 추출함
# Flink 내부의 워터마크 전략(WatermarkStrategy)과 함께 사용됨
# ---------------------------------------------------------------------
class JsonTimestampAssigner(TimestampAssigner):
    def extract_timestamp(self, element, record_timestamp):
        try:
            # Kafka에서 받은 메시지를 JSON으로 파싱
            ts = json.loads(element).get("timestamp")
            # ISO8601 형식(예: "2025-11-10T17:35:00")을 epoch(ms)로 변환
            if ts:
                return int(datetime.fromisoformat(ts).timestamp() * 1000)
        except Exception:
            pass
        # timestamp가 없거나 오류 발생 시 현재 시각(ms)을 반환
        return int(datetime.utcnow().timestamp() * 1000)


# ---------------------------------------------------------------------
# ProcessFunction을 상속한 클래스
# 각 이벤트 처리 시점에서 현재 워터마크 값을 함께 출력
# (디버깅 또는 워터마크 동작 확인 용도)
# ---------------------------------------------------------------------
class PrintWatermarkProcessFunction(ProcessFunction):
    def process_element(self, value, ctx):
        # 현재 연산자가 알고 있는 워터마크 시각을 조회
        watermark = ctx.timer_service().current_watermark()
        # 이벤트 값과 현재 워터마크를 콘솔에 출력
        print(f"[DEBUG] Event: {value}, Current Watermark: {watermark}")
        # 원본 데이터를 다음 연산자로 전달
        yield value


# ---------------------------------------------------------------------
# 집계 함수(AggregateFunction)
# 동일한 sensor_id를 가지는 이벤트를 윈도우 단위로 평균 계산함
# ---------------------------------------------------------------------
class SensorAggregate(AggregateFunction):
    def create_accumulator(self):
        # 누적기(accumulator) 초기화
        # (온도 합계, 습도 합계, 개수, 마지막 상태, 센서 ID)
        return (0.0, 0.0, 0, "", "")

    def add(self, value, acc):
        # 새로운 레코드를 누적기에 더함
        t_sum, h_sum, cnt, _, _ = acc
        return (t_sum + value[2], h_sum + value[3], cnt + 1, value[4], value[0])

    def get_result(self, acc):
        # 최종 집계 결과 계산
        t_sum, h_sum, cnt, last_status, sensor_id = acc
        if cnt == 0:
            return "{}"  # 데이터가 없을 경우 빈 JSON 반환
        # 평균 온도, 평균 습도, 상태, 갱신 시각 등을 JSON 형태로 반환
        return json.dumps({
            "sensor_id": sensor_id,
            "avg_temperature": round(t_sum / cnt, 2),
            "avg_humidity": round(h_sum / cnt, 2),
            "last_status": last_status,
            "update_time": datetime.utcnow().isoformat()
        })

    def merge(self, a, b):
        # 병합 로직 (여기서는 단순히 첫 번째 누적기를 반환)
        return a


# ---------------------------------------------------------------------
# 문자열(JSON 포맷)을 튜플 형태로 변환하는 함수
# 이후 key_by, window 등의 연산을 수행하기 위해 사용
# ---------------------------------------------------------------------
def parse_json_to_tuple(x: str):
    try:
        data = json.loads(x)
    except Exception:
        data = {}
    # (sensor_id, location, temperature, humidity, status)
    return (
        data.get('sensor_id', 'unknown'),
        data.get('location', 'unknown'),
        float(data.get('temperature', 0.0)),
        float(data.get('humidity', 0.0)),
        data.get('status', 'UNKNOWN')
    )


def main():
    # -----------------------------------------------------------------
    # 1. Flink-Kafka 커넥터 JAR 파일 등록
    # PyFlink는 Java 기반이므로, 외부 커넥터를 사용하려면 JAR 경로를 지정해야 함
    # -----------------------------------------------------------------
    kafka_jar_path = os.path.abspath("flink-sql-connector-kafka-3.3.0-1.19.jar")
    conf = Configuration()
    conf.set_string("pipeline.jars", f"file://{kafka_jar_path}")

    # -----------------------------------------------------------------
    # 2. StreamExecutionEnvironment 생성
    # Flink 스트리밍 실행 환경을 초기화하고 병렬도 설정
    # -----------------------------------------------------------------
    env = StreamExecutionEnvironment.get_execution_environment(configuration=conf)
    env.set_parallelism(1)

    # -----------------------------------------------------------------
    # 3. Kafka Consumer 정의
    # sensor_readings 토픽에서 JSON 문자열을 읽어옴
    # SimpleStringSchema()를 사용하여 메시지를 문자열로 직렬화/역직렬화
    # -----------------------------------------------------------------
    kafka_source = FlinkKafkaConsumer(
        topics="sensor_readings",
        deserialization_schema=SimpleStringSchema(),
        properties={
            "bootstrap.servers": "localhost:9092",
            "group.id": "flink-sensor-group",
            "auto.offset.reset": "earliest",
        }
    )

    # -----------------------------------------------------------------
    # 4. 워터마크 전략 설정
    # - for_bounded_out_of_orderness: 최대 지연 허용 시간 지정
    # - Duration.of_seconds(1): 최대 1초 지연 허용
    # - with_timestamp_assigner: 만들어 둔 Assigner 지정
    # -----------------------------------------------------------------
    watermark_strategy = (
        WatermarkStrategy
        .for_bounded_out_of_orderness(Duration.of_seconds(1))
        .with_timestamp_assigner(JsonTimestampAssigner())
    )

    # -----------------------------------------------------------------
    # 5. 데이터 스트림 구성
    # Kafka → Watermark 할당 → 워터마크 디버깅 출력 → JSON 파싱
    # -----------------------------------------------------------------
    stream = (
        env.add_source(kafka_source)
        .assign_timestamps_and_watermarks(watermark_strategy)
        .map(lambda x: x, output_type=Types.STRING())
        .map(parse_json_to_tuple, output_type=Types.TUPLE([
            Types.STRING(),
            Types.STRING(),
            Types.FLOAT(),
            Types.FLOAT(),
            Types.STRING()
        ]))
    )

    # -----------------------------------------------------------------
    # 6. 이벤트 타임 기반 텀블링 윈도우 집계
    # - key_by: sensor_id를 기준으로 데이터 그룹화
    # - window: 10초 단위의 Tumbling Window 생성
    #   (Processing Time 기준으로 일정 시간 단위로 데이터를 집계)
    # - aggregate: 사용자 정의 SensorAggregate 함수 적용
    # 센서 ID를 기준으로 데이터를 그룹화한 후,센서 데이터를 집계하려면 동일한 센서에서 발생한 데이터끼리 그룹핑해야 하므로, 각 요소의 sensor_id를 기준으로 데이터를 묶어야 합니다.
    # sensor_id는 튜플의 첫 번째 요소에 위치하므로, key_by 함수에서 이를 기준으로 그룹핑하도록 구현합니다.
    # 이후 집계를 위한 시간 단위를 설정해야 하는데, 해당 스트리밍 처리에서는 실시간 처리 기준의 10초 단위로 데이터를 구분하여 집계합니다.
    # 따라서 Processing Time 기반의 고정 간격 윈도우(Tumbling Window)를 사용하고, 그 간격을 10초로 설정해 데이터를 시간 블록 단위로 분할해 처리할 수 있도록 구현합니다.
 
    # -----------------------------------------------------------------
    result_stream = (
        stream
        .key_by(lambda x: x[0])
        .window(TumblingEventTimeWindows.of(Time.seconds(10)))
        .aggregate(SensorAggregate(), output_type=Types.STRING())
    )

    # -----------------------------------------------------------------
    # 7. 최종 결과를 콘솔에 출력
    # Flink 파이프라인 실행
    # -----------------------------------------------------------------
    result_stream.print()
    env.execute("Sensor Stream with Watermark Example (PyFlink 1.19)")

if __name__ == "__main__":
    main()
