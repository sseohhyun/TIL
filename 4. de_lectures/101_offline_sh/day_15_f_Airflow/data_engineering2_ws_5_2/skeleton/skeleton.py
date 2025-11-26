from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.operators.bash import BashOperator
import pendulum

# XCom을 사용하여 데이터를 저장하는 함수 정의
def push_xcom_value(**kwargs):
    """
    Airflow의 XCom (Cross-Communication) 기능을 사용하여 값을 저장하는 함수.
    이 함수는 PythonOperator에서 실행되며, 특정 키('message')로 데이터를 XCom에 저장한다.

    Args:
        **kwargs: Airflow에서 자동으로 전달하는 컨텍스트 변수.
    
    Returns:
        None
    """
    kwargs['ti'].xcom_push(key='message', value='Hello from PythonOperator!')

# DAG (Workflow) 정의
with DAG(
    dag_id="python_bash_xcom_example",  # DAG의 고유한 ID (이름)
    start_date=pendulum.datetime(2025, 8, 18, tz="Asia/Seoul"),  # DAG 시작 날짜 (과거 날짜를 설정하여 즉시 실행 가능)
    catchup=False,  # start_date 이후의 미실행 DAG를 모두 실행할지 여부 (False이면 실행하지 않음)
) as dag:

    # PythonOperator를 사용하여 XCom에 데이터 저장하는 작업 생성
    push_task = PythonOperator(
        task_id="push_task",  # 태스크 ID (고유해야 함)
        python_callable=push_xcom_value  # 실행할 Python 함수 (push_xcom_value 함수 호출)
    )

    # BashOperator를 사용하여 XCom에서 값을 가져와 출력하는 작업 생성
    pull_task = BashOperator(
        task_id="pull_task",  # 태스크 ID (고유해야 함)
        bash_command="echo '{{ ti.xcom_pull(task_ids=\"push_task\", key=\"message\") }}'",  
        # Bash 명령어 실행: XCom에서 "push_task"의 "message" 값을 가져와 출력
    )

    # DAG 실행 순서 정의: push_task 실행 후 pull_task 실행
    push_task >> pull_task