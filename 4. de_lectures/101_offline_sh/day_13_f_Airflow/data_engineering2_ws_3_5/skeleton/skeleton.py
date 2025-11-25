from airflow import DAG  # DAG 생성을 위한 기본 클래스
from airflow.operators.empty import EmptyOperator  # 실행할 작업이 없는 빈 태스크
import pendulum  # 시간대 설정을 위한 라이브러리

# DAG 정의 (이 DAG는 Task 실행 주기 설정을 실습하기 위한 예제입니다.)
with DAG(
    dag_id="test_airflow_schedule",  # DAG의 고유한 이름 (Airflow UI에서 확인 가능)
    start_date=pendulum.datetime(2054, 8, 17, tz="Asia/Seoul"),  # DAG 실행을 시작할 기준 날짜 (연도, 월, 일 입력)
    schedule="0 9 * * *",  # 실행 주기 설정 (Cron 표현식 사용)
    tags=["schedule_interval"],  # DAG 태그 (Airflow UI에서 필터링 가능)
) as dag:

    # DAG 실행 시작을 나타내는 태스크 (실행만 하고 아무 동작 없음)
    start = EmptyOperator(task_id="start_task")  

    # DAG 실행 종료를 나타내는 태스크 (마지막 단계)
    end = EmptyOperator(task_id="end_task")  

    # 실행 순서 설정 (start → end 순서로 실행됨)
    start >> end 

# 실행 주기(Schedule Interval) 설명:
# - schedule="0 9 * * *": 매일 오전 9시에 실행됨 (Cron 표현식 사용)

# Schedule Interval 설정 방법:
# 1. Cron 표현식 사용 (예제: "0 9 * * *" → 매일 오전 9시 실행)
# 2. 예약어 사용 가능: @daily, @hourly, @weekly, @monthly 등
# 3. None으로 설정하면 스케줄 없이 수동 실행만 가능

# Airflow 기본 설정 변경:
# - airflow.cfg 또는 Docker 환경 변수에서 설정을 변경할 수 있음
# - 주요 설정 항목:
#   - executor: 실행 엔진 설정 (SequentialExecutor, LocalExecutor, CeleryExecutor 등)
#   - default_timezone: 기본 시간대 설정 (예: Asia/Seoul)
#   - dags_folder: DAG 파일이 저장되는 경로

# DAG 실행 후 Web UI에서 확인할 것:
# 1. DAG 목록에서 test_airflow_schedule DAG이 표시되는지 확인
# 2. DAG이 매일 오전 9시에 자동 실행되는지 확인
# 3. Airflow UI에서 DAG 실행 시간을 변경하고, 다음 실행 예정 시간을 확인
# 4. 실행 후, Task 상태가 정상적으로 "Success"로 변경되는지 확인