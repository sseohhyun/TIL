from airflow import DAG
from airflow.operators.empty import EmptyOperator
from airflow.operators.bash import BashOperator
from airflow.utils.task_group import TaskGroup
import pendulum

# DAG 정의
with DAG(
    dag_id="nested_taskgroup_example",  # DAG의 고유 ID (DAG 이름)
    start_date=pendulum.datetime(2025, 8, 18, tz="Asia/Seoul"),  # DAG 실행 시작 날짜 (타임존: 서울)
    catchup=False,  # 과거 실행 날짜의 DAG 실행을 방지 (True: 실행, False: 실행 안 함)
) as dag:

    # 시작 Task (DAG의 시작 지점, 아무 작업 없이 흐름만 제어)
    start = EmptyOperator(task_id="start")  # 'start'라는 이름의 빈 Task

    # 첫 번째 TaskGroup 정의 (group_1) - 여러 Task를 묶어서 실행 흐름을 단순화
    with TaskGroup("group_1") as group_1:
        
        # 첫 번째 Task (group_1 내에서 실행)
        task_1 = BashOperator(
            task_id="task_1",
            bash_command="echo 'Task 1 실행'"  # 콘솔에 'Task 1 실행'을 출력하는 명령어 실행
        )

        # 내부 TaskGroup 정의 (inner_group_1) - group_1 내부에 포함됨
        with TaskGroup("inner_group_1") as inner_group_1:
            inner_task = BashOperator(
                task_id="inner_task",
                bash_command="echo 'Inner Group 실행'"  # 콘솔에 'Inner Group 실행'을 출력하는 명령어 실행
            )

        # 병렬로 실행될 Task (task_2, task_3)
        task_2 = BashOperator(
            task_id="task_2",
            bash_command="echo 'Task 2 실행'"  # 콘솔에 'Task 2 실행'을 출력하는 명령어 실행
        )

        task_3 = BashOperator(
            task_id="task_3",
            bash_command="echo 'Task 3 실행'"  # 콘솔에 'Task 3 실행'을 출력하는 명령어 실행
        )

        # 마지막 Task (task_2, task_3가 완료된 후 실행)
        task_4 = BashOperator(
            task_id="task_4",
            bash_command="echo 'Task 4 실행'"  # 콘솔에 'Task 4 실행'을 출력하는 명령어 실행
        )

        # 실행 순서 정의:
        # 1. task_1 실행
        # 2. inner_group_1 실행 (inner_task 포함)
        # 3. inner_group_1 완료 후 task_2, task_3가 병렬 실행
        # 4. task_2, task_3가 완료되면 task_4 실행
        task_1 >> inner_group_1 >> [task_2, task_3] >> task_4

    # 종료 Task (DAG의 마지막 지점, 아무 작업 없이 흐름만 제어)
    end = EmptyOperator(task_id="end")  # 'end'라는 이름의 빈 Task

    # DAG 실행 흐름 설정:
    # 1. start 실행 → group_1 실행 → end 실행
    start >> group_1 >> end