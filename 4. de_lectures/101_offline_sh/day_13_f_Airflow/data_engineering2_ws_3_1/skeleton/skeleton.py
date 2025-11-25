from airflow.models.dag import DAG
from airflow.operators.empty import EmptyOperator

# Airflow에서 DAG(Directed Acyclic Graph)를 정의하는 코드
# DAG는 작업(Task)들의 실행 순서를 정의하는 개념

# DAG 정의
with DAG(
    dag_id="dags_dummy_operator",  # DAG의 고유 식별자 (이름)
    default_args={'start_date': None},  # DAG 실행에 필요한 기본 인자 설정 (여기서는 최소 설정만 포함)
    schedule=None  # DAG의 실행 주기를 설정하지 않음 (수동 실행 전용)
) as dag:
    
    # EmptyOperator 아무 작업도 수행하지 않는 Operator
    # DAG의 구조를 정의하는 데 사용됨
    
    # 첫 번째 EmptyOperator 태스크 생성 (시작 지점 역할)
    start = EmptyOperator(
        task_id='start'  # 태스크의 고유 식별자
    )
    
    # 두 번째 EmptyOperator 태스크 생성 (종료 지점 역할)
    end = EmptyOperator(
        task_id='end'  # 태스크의 고유 식별자
    )
    
    # DAG 내에서 태스크 실행 순서 정의
    # start_task 실행 후 end_task 실행됨
    start >> end
