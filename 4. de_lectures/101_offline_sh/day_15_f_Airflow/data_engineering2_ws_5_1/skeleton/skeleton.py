from airflow import DAG
from airflow.operators.python import PythonOperator
import pendulum


# XCom에 데이터 저장 (Push)하는 함수
def push_xcom_value(**kwargs):
    """
    XCom을 사용하여 데이터를 전달하는 함수.
    kwargs['ti']를 사용하여 XCom 값을 push할 수 있음.
    'message'라는 키를 사용하여 데이터를 저장해야 함.
    """
    kwargs['ti'].xcom_push(key="message", value="hello airflow")  # 빈칸 채우기

# XCom에서 데이터 가져오기 (Pull)하는 함수
def pull_xcom_value(**kwargs):
    """
    XCom에서 값을 가져오는 함수.
    push_task에서 저장한 값을 가져와 출력해야 함.
    """
    message = kwargs['ti'].xcom_pull(task_ids="push_task", key="message")  # 빈칸 채우기
    print("XCom에서 받은 값:", message)  # 빈칸 채우기

# DAG 정의 (Airflow의 Workflow를 정의)
with DAG(
    dag_id="xcom_example",  # DAG의 ID 지정 (예: "xcom_example")
    start_date=pendulum.datetime(2025, 8, 18, tz="Asia/Seoul"),  # DAG 실행 시작 날짜 설정
    catchup=False,  # catchup을 False로 설정
) as dag:

    # XCom에 값을 저장하는 PythonOperator 생성
    push_task = PythonOperator(
        task_id="push_task",  # 작업(Task) ID 지정 (예: "push_task")
        python_callable=push_xcom_value  # 실행할 Python 함수 지정 (예: push_xcom_value)
    )

    # XCom에서 값을 가져오는 PythonOperator 생성
    pull_task = PythonOperator(
        task_id="pull_task",  # 작업(Task) ID 지정 (예: "pull_task")
        python_callable=pull_xcom_value  # 실행할 Python 함수 지정 (예: pull_xcom_value)
    )

    # DAG 실행 흐름 정의 (push_task 실행 후 pull_task 실행)
    push_task >> pull_task  # 빈칸 채우기 (예: push_task >> pull_task)