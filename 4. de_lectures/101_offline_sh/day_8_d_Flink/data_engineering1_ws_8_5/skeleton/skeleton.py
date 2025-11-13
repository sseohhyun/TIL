from pyflink.datastream import StreamExecutionEnvironment
from pyflink.table import StreamTableEnvironment, EnvironmentSettings
import os
import logging
import time
# TODO: 해당 코드를 실행하기 전에 kafka_producer.py를 먼저 실행해주세요.

# 로깅 설정
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

def main():
    logger.info("Flink 작업 시작...")
    
    # [1] 실행 환경 구성
    env = StreamExecutionEnvironment.get_execution_environment()
    settings = EnvironmentSettings.new_instance().in_streaming_mode().build()
    table_env = StreamTableEnvironment.create(env, environment_settings=settings)

    # [2] Kafka 커넥터 JAR 경로 설정
    kafka_jar = os.path.join(os.path.abspath('.'), 'flink-sql-connector-kafka-3.3.0-1.19.jar')
    logger.info(f"사용하는 JAR 파일 경로: {kafka_jar}")
    if not os.path.exists(kafka_jar):
        logger.error(f"JAR 파일이 존재하지 않습니다: {kafka_jar}")
        return
        
    table_env.get_config().get_configuration().set_string("pipeline.jars", f"file://{kafka_jar}")

    # [3] Kafka 소스 테이블 생성
    try:
        logger.info("Kafka 소스 테이블 생성 시도...")
        table_env.execute_sql("""
        CREATE TABLE kafka_source (
            stock_code STRING,
            stock_name STRING,
            trade_type STRING,
            price DECIMAL(10,2),
            volume BIGINT,
            trade_time TIMESTAMP(3),
            proctime AS PROCTIME()
        ) WITH (
            'connector' = 'kafka',
            'topic' = 'stock_trades',
            'properties.bootstrap.servers' = 'localhost:9092',
            'properties.group.id' = 'flink-consumer-group',
            'scan.startup.mode' = 'earliest-offset',
            'format' = 'json',
            'json.fail-on-missing-field' = 'false',
            'json.ignore-parse-errors' = 'true'
        )
        """)
        logger.info("Kafka 소스 테이블 생성 성공")
    except Exception as e:
        logger.error(f"소스 테이블 생성 중 오류 발생: {e}")
        return

    # [4] Kafka 싱크 테이블 생성
    try:
        logger.info("Kafka 싱크 테이블 생성 시도...")
        table_env.execute_sql("""
        CREATE TABLE kafka_sink (
            stock_code STRING,
            stock_name STRING,
            total_volume BIGINT,
            avg_price DECIMAL(10,2),
            update_time TIMESTAMP(3),
            PRIMARY KEY (stock_code) NOT ENFORCED
        ) WITH (
            'connector' = 'upsert-kafka',
            'topic' = 'stock_stats',
            'properties.bootstrap.servers' = 'localhost:9092',
            'key.format' = 'json',
            'value.format' = 'json',
            'properties.group.id' = 'flink-sink-group'
        )
        """)
        logger.info("Kafka 싱크 테이블 생성 성공")
    except Exception as e:
        logger.error(f"싱크 테이블 생성 중 오류 발생: {e}")
        return

    # [5] SQL 쿼리 작성 및 실행
    try:
        logger.info("SQL 쿼리 실행 시도...")
        stmt_set = table_env.create_statement_set()
        stmt_set.add_insert_sql("""
        INSERT INTO kafka_sink
        SELECT 
            stock_code,
            stock_name,
            SUM(volume) AS total_volume,
            AVG(price) AS avg_price,
            CURRENT_TIMESTAMP as update_time
        FROM kafka_source
        GROUP BY stock_code, stock_name
        """)
        
        job_client = stmt_set.execute().get_job_client()
        
        if job_client:
            job_id = job_client.get_job_id()
            logger.info(f"작업이 성공적으로 제출되었습니다. 작업 ID: {job_id}")
            monitor_job(job_client)
        else:
            logger.error("작업 클라이언트를 가져올 수 없습니다.")
    except Exception as e:
        logger.error(f"작업 실행 중 오류 발생: {e}")

def monitor_job(job_client):
    """작업 상태를 모니터링하고 로그를 출력합니다."""
    try:
        job_status = job_client.get_job_status().result()
        logger.info(f"현재 작업 상태: {job_status}")
        
        logger.info("Kafka 토픽에 샘플 데이터가 있는지 확인해주세요.")
        logger.info("샘플 데이터가 없다면 kafka_producer.py를 실행하여 테스트 데이터를 생성하세요.")
        
        print("\n작업 모니터링 시작 (10초마다 상태 확인, Ctrl+C로 종료)")
        for i in range(6):
            time.sleep(10)
            try:
                current_status = job_client.get_job_status().result()
                print(f"[{i+1}/6] 현재 작업 상태: {current_status}")
            except Exception as e:
                print(f"상태 확인 중 오류 발생: {e}")
        
        print("\n모니터링 완료. 작업은 계속 실행 중입니다.")
        print("결과를 확인하려면 다음 명령어를 실행하세요:")
        print("/home/ssafy/kafka/bin/kafka-console-consumer.sh --topic stock_stats --bootstrap-server localhost:9092 --from-beginning")
        
    except Exception as e:
        logger.error(f"작업 모니터링 중 오류 발생: {e}")

if __name__ == '__main__':
    main()