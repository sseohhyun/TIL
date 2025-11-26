from airflow import DAG
from airflow.operators.empty import EmptyOperator
from datetime import datetime

# Task 목록: DAG 내에서 실행될 개별 작업들의 ID를 리스트로 정의합니다.
task_list = ['task_1', 'task_2', 'task_3']

# DAG (Directed Acyclic Graph) 정의
dag = DAG(
    dag_id="dynamic_dag_example",  # DAG의 고유 식별자 (이름)
    start_date=datetime(2025, 11, 26)  # DAG 시작 날짜 설정
)

# 반복문을 활용한 동적 Task 생성
for task_name in task_list:
    # 각 task_list의 요소(task_name)를 task_id로 갖는 EmptyOperator 인스턴스를 생성합니다.
    task = EmptyOperator(
        task_id=task_name,  # 작업의 ID (Airflow에서 유일해야 함)
        dag=dag  # 해당 DAG에 속하도록 지정
    )

# 위의 코드는 개별 작업들을 생성하는 역할을 하고, 생성된 작업들 간의 의존 관계는 따로 설정하지 않았기 때문에 독립적으로 실행됩니다.