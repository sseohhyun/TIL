from airflow import DAG  
import pendulum 
import datetime
from airflow.operators.bash import BashOperator 

# DAG 정의
with DAG(
    dag_id="dags_bash_select_fruit",  # DAG의 고유 식별자
    schedule="0 10 * * 6#1",  # 매월 첫 번째 토요일 00:10 (UTC) 실행되는 스케줄
    start_date=pendulum.datetime(2025, 11, 25, tz="Asia/Seoul"),  # DAG 시작 날짜
    catchup=False  # 과거 실행 일정에 대한 캐치업 여부
) as dag:
    
    # 첫 번째 BashOperator 태스크: ORANGE 선택
    t1_orange = BashOperator(
        task_id="t1_orange",  # 태스크 ID (유니크한 값)
        bash_command="/opt/airflow/plugins/shell/select_fruit.sh ORANGE",  # 실행할 Bash 명령어 (ORANGE 선택)
    )

    # 두 번째 BashOperator 태스크: AVOCADO 선택
    t2_avocado = BashOperator(
        task_id="t2_avocado",  # 태스크 ID (유니크한 값)
        bash_command="/opt/airflow/plugins/shell/select_fruit.sh AVOCADO",  # 실행할 Bash 명령어 (AVOCADO 선택)
    )
