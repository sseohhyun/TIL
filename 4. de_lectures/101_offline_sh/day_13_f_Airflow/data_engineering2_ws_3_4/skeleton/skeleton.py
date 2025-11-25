# PythonOperator란?
# - Airflow에서 Python 함수를 실행할 수 있도록 도와주는 Operator입니다.
# - 'python_callable' 파라미터에 실행할 Python 함수를 전달하면, Airflow가 해당 함수를 실행합니다.
# - Python 함수를 실행하고, 실행 결과를 Airflow 로그에 남길 수 있습니다.

# PythonOperator 사용 예제
# - 실행할 Python 함수를 정의한 후, PythonOperator에서 'python_callable' 파라미터에 전달합니다.
# - 실행 결과를 Airflow Web UI에서 확인할 수 있습니다.

from airflow import DAG  # DAG 생성을 위한 기본 클래스
from airflow.operators.empty import EmptyOperator  # 실행할 작업이 없는 빈 태스크
from airflow.operators.python import PythonOperator  # Python 함수를 실행하는 오퍼레이터
import pendulum  # 시간대 설정을 위한 라이브러리

# 정상적으로 실행되는 Python 함수
def success_task():
    print("정상 실행: 이 메시지가 로그에 남습니다.")

# 오류를 발생시키는 Python 함수 (디버깅용)
def fail_task():
    print("실행 실패: 오류 발생!")
    raise ValueError("이것은 의도적인 에러입니다. 로그에서 확인하세요.")

# DAG 정의 (Airflow에서 태스크를 실행할 논리적 그룹)
with DAG(
    dag_id="test_airflow_logs_debugging",  # DAG의 고유한 이름 (Airflow UI에서 확인 가능)
    start_date=pendulum.today("Asia/Seoul"),  #  DAG 실행 시작 날짜 설정 (오늘 날짜)
    tags=["logs_debugging"],  # DAG 태그 (Airflow UI에서 필터링 가능)
) as dag:

    # DAG 실행 시작을 나타내는 태스크 (아무 작업도 하지 않음)
    start = EmptyOperator(task_id="start_task")  #  빈 태스크 생성

    # 정상적으로 실행되는 Task (로그에서 실행 성공 메시지를 확인할 수 있음)
    success = PythonOperator(  #  Python 함수를 실행하는 오퍼레이터 사용
        task_id="success_task",  # 태스크 ID (Airflow UI에서 보이는 이름)
        python_callable=success_task  #  실행할 Python 함수 지정
    )

    # 오류가 발생하는 Task (로그에서 오류 메시지를 확인하여 디버깅 가능)
    fail = PythonOperator(  #  Python 함수를 실행하는 오퍼레이터 사용
        task_id="fail_task",  # 태스크 ID (Airflow UI에서 보이는 이름)
        python_callable=fail_task  #  실행할 Python 함수 지정 (실패하는 함수)
    )

    # DAG 실행 종료를 나타내는 태스크 (아무 작업도 하지 않음)
    end = EmptyOperator(task_id="end_task")  #  빈 태스크 생성

    # 실행 순서 정의: start → success & fail → end
    start >> [success, fail] >> end  # DAG 태스크의 실행 순서 지정

# DAG 실행 후 Web UI에서 확인할 것:
# 1. DAG 목록에서 `test_airflow_logs_debugging` DAG이 표시되는지 확인
# 2. DAG 실행 후, `success_task`는 성공하고 `fail_task`는 실패하는지 확인
# 3. Airflow UI에서 `fail_task`를 클릭하고, 실행 로그에서 오류 메시지를 찾기
# 4. `success_task`의 로그를 확인하여 정상 실행 메시지를 찾기
