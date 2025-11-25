from airflow.models.dag import DAG 
import datetime 
import pendulum  
from airflow.operators.python import PythonOperator 
import logging  
import random  

# 1. 로그 출력 함수 정의
def sample_task():
    """
    실행 시 성공 또는 실패를 랜덤하게 결정하는 함수
    """
    logging.info("Task가 실행되었습니다!")  # 로그 기록
    print("이것은 표준 출력입니다.")  # 일반적인 print 사용 가능
    
    # 랜덤하게 성공 또는 실패를 시뮬레이션
    if random.choice([True, False]):
        logging.info("Task가 성공적으로 완료되었습니다!")
        return "Task 실행 완료"
    else:
        logging.error("Task가 실패했습니다!")
        raise Exception("의도적인 실패 발생")

# 2. DAG 정의 (Workflow)
with DAG(
    dag_id="dags_logging_example",  # DAG의 고유 ID (이름)
    schedule="0 9 * * *",  # 매일 특정 시간 실행 (CRON 표현식)
    start_date=pendulum.datetime(2025, 8, 18, tz="Asia/Seoul"),  # DAG 시작 날짜 및 시간대 설정
    dagrun_timeout=datetime.timedelta(minutes=60),  # DAG 최대 실행 시간 제한
) as dag:
    
    # 3. PythonOperator 정의 (Task)
    logging_task = PythonOperator(
        task_id='logging_task',  # Task의 고유 ID (이름)
        python_callable=sample_task  # 실행할 함수 지정
    )

    # DAG 내에서 실행 순서 지정 (현재는 단일 Task이므로 단순 실행)
    logging_task
