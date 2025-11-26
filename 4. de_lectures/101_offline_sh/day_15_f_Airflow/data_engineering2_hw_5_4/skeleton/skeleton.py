import requests 
from airflow import DAG 
from airflow.operators.python import BranchPythonOperator, PythonOperator 
from airflow.operators.bash import BashOperator
import pendulum 

# (1) API 응답값을 확인하여 실행할 Task 결정하는 함수
def check_weather():
    # Open-Meteo API를 호출하여 현재 날씨 정보를 가져옴
    response = requests.get(
        "https://api.open-meteo.com/v1/forecast?latitude=37.5665&longitude=126.9780&current_weather=true"
    )
    data = response.json()  # API 응답 데이터를 JSON 형식으로 변환
    
    # JSON 응답 전체 출력 (디버깅 용도)
    print("API 응답 전체 데이터:", data)

    # (2) 현재 기온 가져오기
    temperature = data["current_weather"]["temperature"]  # JSON 응답에서 현재 기온 가져오기
    print("현재 기온:", temperature, "도")

    # 기온이 15도 이상이면 'task_hot' 실행, 15도 미만이면 'task_cold' 실행
    if temperature >= 15:
        return "task_hot"  # 기온이 15도 이상이면 실행할 Task ID 입력
    else:
        return "task_cold"  # 기온이 15도 미만이면 실행할 Task ID 입력

# (3) API 응답값을 출력하는 함수
def print_weather():
    # Open-Meteo API를 호출하여 현재 날씨 정보를 가져옴
    response = requests.get(
        "https://api.open-meteo.com/v1/forecast?latitude=37.5665&longitude=126.9780&current_weather=true"
    )
    data = response.json()  # API 응답 데이터를 JSON 형식으로 변환

    # 현재 기온 가져오기
    temperature = data["current_weather"]["temperature"]  # JSON 응답에서 현재 기온 가져오기

    # API 응답 데이터 및 현재 기온 출력
    print("현재 날씨 데이터:", data)
    print("현재 기온:", temperature, "도")

# (4) DAG 정의
with DAG(
    dag_id="branch_operator_weather_api_logging_example",  # DAG의 고유 ID 설정
    start_date=pendulum.datetime(2025, 8, 18, tz="Asia/Seoul"),  # DAG 시작 날짜 및 시간대 설정
    catchup=False,  # 과거 실행 안 함 (False로 설정)
) as dag:

    # (5) API 상태 확인 후 실행할 Task 선택
    branch_task = BranchPythonOperator(  # 올바른 Operator 사용
        task_id="branching_weather_api",  # Task ID 설정
        python_callable=check_weather  # 실행할 Python 함수 지정
    )

    # (6) 기온이 15도 이상이면 실행될 Task
    task_hot = BashOperator(  # 올바른 Operator 사용
        task_id="task_hot",  # Task ID 설정
        bash_command="echo '오늘 날씨: 덥습니다'"  # 터미널에서 메시지를 출력하는 Bash 명령 실행
    )

    # (7) 기온이 15도 미만이면 실행될 Task
    task_cold = BashOperator(  # 올바른 Operator 사용
        task_id="task_cold",  # Task ID 설정
        bash_command="echo '오늘 날씨: 춥습니다'"  # 터미널에서 메시지를 출력하는 Bash 명령 실행
    )

    # (8) API 결과값을 출력하는 Task
    log_weather = PythonOperator(  # 올바른 Operator 사용
        task_id="log_weather",  # Task ID 설정
        python_callable=print_weather  # 실행할 Python 함수 지정
    )

    # (9) DAG 실행 흐름 설정
    branch_task >> [task_hot, task_cold]  >> log_weather
    # branch_task가 task_hot 또는 task_cold를 선택하여 실행하도록 설정