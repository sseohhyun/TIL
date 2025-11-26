from airflow import DAG
from airflow.operators.python import BranchPythonOperator
from airflow.operators.bash import BashOperator  
import pendulum

# 분기 조건을 결정하는 Python 함수
def choose_branch(**kwargs):
    """
    조건에 따라 실행할 태스크(task_A 또는 task_B)를 결정하는 함수.
    현재 value 변수에 "A" 값을 할당했으므로 항상 "task_A"가 실행됨.
    """
    value = "A"  # 실행 조건 변경 가능 (예: "B"로 변경 시 task_B가 실행됨)
    return "task_A" if value == "A" else "task_B" # 실행할 Task ID 반환

# DAG (Directed Acyclic Graph) 정의
with DAG(
    dag_id="simple_branch_operator_example",  # DAG의 고유한 ID 설정
    start_date=pendulum.datetime(2025, 8, 18, tz="Asia/Seoul"),  # DAG 시작 날짜 및 시간대 설정
    catchup=False,  # 과거 실행 여부 설정 (False: 지정된 start_date 이후의 실행만 수행)
) as dag:

    # 분기 처리를 위한 BranchPythonOperator
    branch_task = BranchPythonOperator(
        task_id="branching",  # Task ID
        python_callable=choose_branch  # 실행할 Python 함수 지정
    )

    # 선택될 Task A (Bash 명령어 실행)
    task_A = BashOperator(
        task_id="task_A",  # Task ID
        bash_command="echo 'Task A 실행'"  # 실행할 Bash 명령어
    )

    # 선택될 Task B (Bash 명령어 실행)
    task_B = BashOperator(
        task_id="task_B",  # Task ID
        bash_command="echo 'Task B 실행'"  # 실행할 Bash 명령어
    )

    # 모든 분기 이후 실행되는 종료 Task
    end_task = BashOperator(
        task_id="end_task",  # Task ID
        bash_command="echo '모든 분기 완료'",  # 실행할 Bash 명령어
        trigger_rule="none_failed_or_skipped"  # 실패하거나 건너뛴 Task가 없을 경우 실행
    )

    # DAG 실행 흐름 정의
    branch_task >> [task_A, task_B]  # 분기 Task 실행 후 하나의 Task만 선택적으로 실행됨
    [task_A, task_B] >> end_task  # 선택된 Task 완료 후 종료 Task 실행
