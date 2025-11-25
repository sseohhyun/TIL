from airflow.models.dag import DAG
import datetime
import pendulum
from airflow.operators.python import PythonOperator

# 각 Task에서 실행할 Python 함수 정의
def task_A():
    print("Task A is running")  # Task A 실행 로그 출력

def task_B():
    print("Task B is running")  # Task B 실행 로그 출력

def task_C():
    print("Task C is running")  # Task C 실행 로그 출력

# DAG (Directed Acyclic Graph) 정의
with DAG(
    dag_id="dags_python_operator",  # DAG의 고유 ID  
    schedule="0 8 1 * *",  # DAG 실행 스케줄  
    start_date=pendulum.datetime(2025, 11, 25, tz="Asia/Seoul"),  # DAG 시작 날짜 및 시간대 설정  
    catchup=False,  # 과거 실행에 대한 catchup 여부 설정  
    dagrun_timeout=datetime.timedelta(minutes=60),  # DAG 실행 최대 시간 제한  
) as dag:
    
    # Task A 생성: PythonOperator를 사용하여 실행할 Python 함수 지정
    task_a = PythonOperator(
        task_id='task_a',  # Task의 고유 ID  
        python_callable=task_A  # 실행할 Python 함수 지정  
    )
    
    # Task B 생성
    task_b = PythonOperator(
        task_id='task_b',  # Task의 고유 ID  
        python_callable=task_B
    )
    
    # Task C 생성
    task_c = PythonOperator(
        task_id='task_c',  # Task의 고유 ID  
        python_callable=task_C
    )
    
    # Task Dependency 설정
    # task_a 실행 후, task_b와 task_c가 병렬로 실행됨
    task_a >> [task_b, task_c]  # Task 의존성 설정  