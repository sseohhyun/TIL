
from airflow import DAG

import datetime
import pendulum
from airflow.operators.bash import BashOperator

# DAG (Directed Acyclic Graph)를 정의합니다.
with DAG(
    dag_id="dags_bash_operator",  # DAG의 고유한 식별자 (이름)
    schedule="0 0 * * *",  # DAG의 실행 일정 (매일 00:00 실행)
    start_date=pendulum.datetime(2025, 8, 18, tz="Asia/Seoul"),  # DAG의 시작 날짜 (빈칸 채우기)
) as dag:
    
    # 첫 번째 BashOperator 정의
    bash_t1 = BashOperator(
        task_id="bash_t1",  # 태스크의 고유 식별자
        bash_command="whoami",  # 실행할 Bash 명령어 (현재 실행 중인 사용자 출력)
    )
    
    # 두 번째 BashOperator 정의
    bash_t2 = BashOperator(
        task_id="bash_t2",  # 태스크의 고유 식별자
        bash_command="echo $HOSTNAME",  # 실행할 Bash 명령어 (현재 실행 중인 호스트 이름 출력)
    )
    
    # 태스크 실행 순서를 정의
    bash_t1 >> bash_t2  # 첫 번째 태스크가 실행된 후 실행될 태스크 지정