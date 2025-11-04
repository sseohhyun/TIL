# 실습 목표
# Docker Compose를 사용하여 HTML 웹 서버를 구성

# Step 1: 실습용 디렉토리 생성 및 이동
# - 실습 파일을 관리할 디렉토리를 생성하고 이동합니다.
mkdir compose-lab
cd compose-lab

# Step 2: index.html 파일 생성
# - 웹 브라우저에서 확인할 HTML 파일을 작성합니다.
echo "<h1>Hello Docker Compose</h1>" > index.html

# Step 3: docker-compose.yml 파일 작성
# - HTML을 띄워줄 웹 서버(Nginx)를 정의한 Compose 설정 파일을 생성합니다.
# compose-lab에 docker-compose.yml 파일을 위치시켜주세요.

# Step 4: Docker Compose 실행
# - 웹 서버 컨테이너를 백그라운드에서 실행합니다.
docker compose up -d

# Step 5: 상태 확인
# - 현재 실행 중인 Compose 서비스 확인
docker compose ps

# Step 6: 접속 확인
# - 웹 브라우저 또는 curl로 접속
curl http://localhost:8080

# Step 7: Compose 종료 및 정리
# - 컨테이너와 네트워크를 정리합니다.
docker compose down