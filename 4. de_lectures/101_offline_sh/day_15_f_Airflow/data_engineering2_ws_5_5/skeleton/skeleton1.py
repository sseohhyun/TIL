from airflow import DAG
from airflow.operators.empty import EmptyOperator 

from datetime import datetime, timedelta

# DAG 정의
dag_a = DAG(  
    dag_id="dag_a",  # DAG의 고유한 ID 설정
    start_date=datetime(2025, 8, 18),  # DAG 실행을 시작할 날짜
)

# 작업(Task) 정의
task_a = EmptyOperator(  
    task_id="task_a",  # 작업의 고유 ID 설정
    dag=dag_a  # 이 작업이 속한 DAG을 지정
)