'''
    해당 코드는 제가 사용하기 위해 만든 코드입니다.
    여러분들은 BASE_URL에 해당하는 부분의 경로가 저와 다릅니다 :)
    사용하고자 하신다면 수정해서 사용해 주세요.
'''

import os
import subprocess

# 클론 받을 디렉토리 지정
clone_dir = r'C:\Users\SSAFY\Desktop\TIL\4. de_lectures\101_offline_sh\day_1_a_WSL_Linux'

# 디렉토리가 없으면 생성
os.makedirs(clone_dir, exist_ok=True)

subject = input('과목을 입력해 주세요 : ')
seperators = ['hw', 'ws']
set_number = input('세트 번호를 입력해 주세요 : ')
for sep in seperators:
    if sep == 'hw':
        pass
        BASE_URL = f'https://lab.ssafy.com/katie1426/'
        stages = [2, 4]
    else: 
        BASE_URL = f'https://lab.ssafy.com/katie1426/'
        # stages = [1, 2, 3, 4, 5, 'a', 'b', 'c']
        stages = [1, 2, 3, 4, 5]
    for stage in stages:   
        URL = f'{BASE_URL}{subject}_{sep}_{set_number}_{stage}'
        subprocess.run(['git', 'clone', URL], cwd=clone_dir)