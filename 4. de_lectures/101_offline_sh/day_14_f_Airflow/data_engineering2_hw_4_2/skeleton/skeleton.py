from airflow import DAG
# Airflow에서 타임존을 다루기 위한 pendulum 라이브러리 
import pendulum
from airflow.operators.python import PythonOperator
import random

# DAG (Directed Acyclic Graph) 정의
with DAG(
    dag_id="dags_python_operator",  # DAG의 고유 식별자
    schedule="30 6 * * *",  # 매일 특정 시간에 실행 (cron 표현식)
    start_date=pendulum.datetime(2025, 8, 18, tz="Asia/Seoul"),  # DAG 시작 날짜 (타임존 포함)
    catchup=False,  # 과거 실행 여부 설정
) as dag:

    # 실행될 Python 함수 정의
    def select_fruit():
        # 과일 리스트 정의
        fruit = ['APPLE', 'BANANA', 'ORANGE', 'AVOCADO']
        # 0부터 3 사이의 랜덤 정수를 생성
        rand_int = random.randint(0, 3)
        # 선택된 랜덤 과일을 출력
        print(fruit[rand_int])

    # PythonOperator를 사용하여 Python 함수 실행하는 작업(Task) 생성
    py_t1 = PythonOperator(
        task_id='py_t1',  # Task의 고유 ID
        python_callable=select_fruit  # 실행할 Python 함수 지정
    )