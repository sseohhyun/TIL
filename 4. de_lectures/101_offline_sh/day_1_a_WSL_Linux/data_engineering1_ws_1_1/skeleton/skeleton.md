# 실습 목표
디렉토리 생성, 이동, 구조 파악 명령어(cd, ls 등등) 사용법 익히기
실제처럼 구조화된 디렉토리 구성 연습

# 실습 시나리오
/home/ssafy/project 하위에 logs, backup, scripts 폴더를 생성합니다.
생성한 구조를 cd, ls -l, tree 명령어로 확인합니다.
샘플 파일을 생성한 뒤, 이를 mv로 logs로 이동하고, cp로 backup에 복사해봅니다.

# ---------------------------
# Step 1: 프로젝트 작업 디렉토리로 이동
# ---------------------------
cd /home/ssafy

# ---------------------------
# Step 2: 하위에 logs, backup, scripts 디렉토리 생성
# 구조: /home/ssafy/project/logs
#       /home/ssafy/project/backup
#       /home/ssafy/project/scripts
# ---------------------------
mkdir -p project/logs
mkdir -p project/backup
mkdir -p project/scripts

# ---------------------------
# Step 3: 생성한 디렉토리 구조로 이동 후
# 구조를 ls -l, tree 명령어로 확인해보세요.
# ---------------------------
cd project
ls -l
tree

# ---------------------------
# Step 4: 현재 위치에서 sample.txt 파일을 생성하고
#         logs 폴더로 이동한 뒤, backup 폴더로 복사해보세요.
# ---------------------------
touch sample.txt                # 샘플 파일 생성
mv sample.txt logs/      # 적절한 경로로 파일 이동
cp logs/sample.txt backup/      # 파일 복사