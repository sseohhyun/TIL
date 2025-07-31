# 1. pip install requests 명령어를 사용하여 requests 패키지를 설치한다.
# 터미널에서 다음 명령어를 실행하세요:
# pip install requests

import requests

# 3. main.py에서 requests 패키지를 사용하여 임의의 API에서 사용자 정보를 가져온다.
def fetch_user_info():
    response = requests.get('https://jsonplaceholder.typicode.com/users/1')
    return response.json()

# 4. 가져온 사용자 정보를 출력하는 함수를 작성한다.
def print_user_info(user_info):
    print(f"Name: {user_info['name']}")
    print(f"Username: {user_info['username']}")
    print(f"Email: {user_info['email']}")

# 사용자 정보를 가져와서 출력한다.
user_info = fetch_user_info()
print_user_info(user_info)