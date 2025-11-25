from airflow import DAG  # DAG 생성을 위한 기본 클래스
from airflow.operators.empty import EmptyOperator  # 실행할 작업이 없는 빈 태스크
import pendulum  # 시간대 설정을 위한 라이브러리

# DAG 정의 (이 DAG는 Airflow Web UI에서 DAG 목록 및 Task 상태를 확인하는 연습용입니다.)
with DAG(
    dag_id="test_airflow_web_ui",  # DAG의 고유한 이름 (Airflow UI에서 확인 가능)
    start_date=pendulum.today("Asia/Seoul"),  # DAG 실행을 시작할 기준 날짜 (오늘 날짜 설정)
    tags=["web_ui_test"],  # DAG 태그 (Airflow UI에서 필터링 및 관리할 때 유용)
) as dag:

    # DAG 실행 시작을 나타내는 태스크 (실행만 하고 아무 동작 없음)
    start = EmptyOperator(task_id="start_task")  

    # 병렬 실행을 테스트하는 태스크 (start_task 실행 후 동시에 실행됨)
    parallel_1 = EmptyOperator(task_id="parallel_task_1")  # 병렬 태스크 1
    parallel_2 = EmptyOperator(task_id="parallel_task_2")  # 병렬 태스크 2

    # 병렬 실행 후 합쳐지는 태스크 (두 개의 병렬 태스크가 완료된 후 실행됨)
    after_parallel = EmptyOperator(task_id="after_parallel_task")

    # 순차 실행을 테스트하는 태스크 (순서대로 실행됨)
    sequential_1 = EmptyOperator(task_id="sequential_task_1")  # 순차 실행 태스크 1
    sequential_2 = EmptyOperator(task_id="sequential_task_2")  # 순차 실행 태스크 2

    # DAG 실행 종료를 나타내는 태스크 (모든 실행이 끝난 후 마지막으로 실행됨)
    end = EmptyOperator(task_id="end_task")  

    # 실행 순서 설정
    start >> [parallel_1, parallel_2]  # start_task 실행 후 병렬_task_1, 병렬_task_2가 동시에 실행됨
    [parallel_1, parallel_2] >> after_parallel  # 두 개의 병렬 태스크가 완료되면 after_parallel_task 실행됨
    after_parallel >> sequential_1 >> sequential_2  # sequential_task_1 → sequential_task_2 순서로 실행됨
    sequential_2 >> end  # 마지막 태스크 실행 후 DAG 종료

# DAG 실행 후 Web UI에서 확인할 것:
# 1. DAG 목록에서 `test_airflow_web_ui` DAG이 표시되는지 확인
# 2. DAG 실행 후, Task 상태가 "대기(pending)" → "실행 중(running)" → "성공(success)"으로 변경되는지 확인
# 3. 병렬 실행되는 태스크와 순차 실행되는 태스크의 차이를 확인
# 4. 각 Task를 클릭하여 실행 로그를 확인 (실행 로그는 거의 없음)