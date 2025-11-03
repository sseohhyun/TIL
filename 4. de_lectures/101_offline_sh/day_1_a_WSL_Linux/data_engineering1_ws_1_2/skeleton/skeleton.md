# echo를 활용한 ASCII 계단 만들기
# 목표: echo 명령어와 리디렉션(>>) 사용법을 익히고,
#       간단한 텍스트 출력 결과를 파일에 저장하고 읽는 방법을 연습합니다.

# [Step 1] 기존 stair.txt 파일이 있다면 초기화합니다.
> stair.txt   # '>'는 파일을 비우는 명령입니다.

# [Step 2] echo 명령어를 사용하여 다음과 같은 모양으로 별(*)을 계단처럼 출력하고 저장합니다.
# *
# **
# ***
# ****
# *****
# 각 줄마다 echo로 직접 작성하고, >> stair.txt로 파일에 추가 저장합니다.
echo "*" >> stair.txt
echo "**" >> stair.txt
echo "***" >> stair.txt
echo "****" >> stair.txt
echo "*****" >> stair.txt

# [Step 3] 저장된 파일 내용을 확인합니다.
cat stair.txt   # 파일 전체 내용 보기

# [Step 4] head 명령어를 사용하여 앞의 3줄만 확인해봅니다.
head -n 3 stair.txt   # 상위 3줄 출력