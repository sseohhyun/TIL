from airflow import DAG
from airflow.operators.empty import EmptyOperator
from airflow.operators.bash import BashOperator
import pendulum

# DAG 정의
with DAG(
    dag_id="trigger_rule_example",  # DAG의 고유한 ID (식별자)
    start_date=pendulum.datetime(2025, 11, 24, tz="Asia/Seoul"),  # DAG 실행 시작일 (과거 날짜)
    catchup=False,  # (1) 백필(이전 날짜에 대한 실행) 여부를 결정 (True/False 중 선택)
) as dag:

    # DAG 시작 Task (실제 작업 수행 없이 DAG의 실행 흐름을 제어하는 역할)
    start = EmptyOperator(task_id="start")

    # 정상적으로 실행되는 Bash Task
    # - 실행 시 "Task 1 실행" 메시지를 출력함
    task_1 = BashOperator(
        task_id="task_1",
        bash_command="echo 'Task 1 실행'",  # (2) "Task 1 실행"을 출력하는 Bash 명령어를 입력
    )

    # 실행이 실패하도록 설정된 Bash Task
    # - `exit 1` 명령어를 실행하여 강제 실패 발생
    task_2 = BashOperator(
        task_id="task_2",
        bash_command="exit 1",  # (3) 강제 실패시키는 명령어를 입력
    )

    # Trigger Rule 적용 예시 1: "all_success"
    # - 모든 upstream(이전 단계의 Task) Task가 성공해야 실행됨
    # - 하지만 task_2가 실패할 예정이므로 실행되지 않음
    task_3 = BashOperator(
        task_id="task_3",
        bash_command="echo 'Task 3 실행'",
        trigger_rule="all_success",  # (4) 모든 upstream Task가 성공해야 실행되는 Trigger Rule을 입력
    )

    # Trigger Rule 적용 예시 2: "one_failed"
    # - 최소 1개의 upstream Task가 실패해야 실행됨
    # - task_2가 실패하므로 실행됨
    task_4 = BashOperator(
        task_id="task_4",
        bash_command="echo 'Task 4 실행 (one_failed)'",
        trigger_rule="one_failed",  # (5) 최소 하나의 Task가 실패해야 실행되는 Trigger Rule을 입력
    )

    # Trigger Rule 적용 예시 3: "all_done"
    # - 모든 upstream Task가 완료되면 실행됨 (성공/실패 여부 무관)
    # - task_1(성공)과 task_2(실패) 모두 완료되었기 때문에 실행됨
    task_5 = BashOperator(
        task_id="task_5",
        bash_command="echo 'Task 5 실행 (all_done)'",
        trigger_rule="all_done",  # (6) 모든 Task가 완료되면 실행되는 Trigger Rule을 입력
    )

    # DAG 종료 Task (실제 작업은 없고 DAG의 흐름을 마무리하는 역할)
    end = EmptyOperator(task_id="end")

    # DAG 실행 흐름 설정
    # - start Task 실행 후 task_1, task_2를 병렬 실행
    start >> [task_1, task_2]

    # - task_1과 task_2가 모두 성공해야 task_3 실행 (task_2가 실패하므로 실행되지 않음)
    [task_1, task_2] >> task_3  # (7) task_3 실행 조건을 고려하여 흐름을 확인

    # - task_1과 task_2 중 최소 1개 실패 시 task_4 실행 (task_2가 실패했으므로 실행됨)
    [task_1, task_2] >> task_4  # (8) task_4 실행 조건을 고려하여 흐름을 확인

    # - task_1과 task_2가 모두 완료되면 task_5 실행 (성공, 실패 여부 관계없이 실행됨)
    [task_1, task_2] >> task_5  # (9) task_5 실행 조건을 고려하여 흐름을 확인

    # - task_3, task_4, task_5가 모두 완료된 후 end Task 실행
    [task_3, task_4, task_5] >> end
