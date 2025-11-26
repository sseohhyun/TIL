from airflow import DAG

# ExternalTaskSensor는 다른 DAG 또는 태스크의 완료 여부를 감지하는 센서
from airflow.sensors.external_task import ExternalTaskSensor
from datetime import datetime, timedelta

# DAG B 정의
dag_b = DAG(
    dag_id="dag_b",  # (2) DAG의 고유 ID를 입력하세요.
    start_date=datetime(2025, 8, 18),  # (3) 시작 날짜를 입력하세요. (예: 2025, 8, 18)
)

# ExternalTaskSensor를 사용하여 DAG A의 특정 태스크가 완료될 때까지 기다리는 센서 정의
wait_for_task_a = ExternalTaskSensor(
    task_id="wait_for_task_a",  # (4) 이 센서 태스크의 ID를 입력
    
    external_dag_id="dag_a",  # (5) 감시할 외부 DAG의 ID를 입력
    
    external_task_id="task_a",  # (6) 감시할 외부 DAG 내의 특정 태스크 ID를 입력
    
    timeout=600,  # 최대 600초(10분) 동안 기다린 후 타임아웃 발생
    
    poke_interval=30,  # 30초마다 "dag_a"의 "task_a" 완료 여부를 확인
    
    mode="poke",  # (7) 센서 실행 모드를 입력 ("poke" 또는 "reschedule")
    
    dag=dag_b  # (8) 이 센서를 포함할 DAG 객체를 입력
)