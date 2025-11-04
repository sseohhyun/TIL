# Docker Compose를 통해 여러 컨테이너를 동시에 실행하여 컨테이너 간의 기본 네트워크 구조 이해

# Step 1: docker compose 명령어로 컨테이너 실행 (up)
# -d 옵션은 백그라운드에서 실행함을 의미합니다.
# docker-compose.yml에 정의된 web, api 두 컨테이너가 실행됩니다.
docker compose up -d

# Step 2: 네트워크 통신 확인 - ping
# 'api' 컨테이너 안에서 'web' 컨테이너에 ping을 보내 네트워크 연결 확인
# Docker Compose에서는 서비스명이 곧 컨테이너 내부 DNS 이름으로 사용됩니다.
docker compose exec api ping web

# Step 3: curl 설치 - 외부 HTTP 요청 시뮬레이션
# 'api' 컨테이너는 Alpine 기반이기 때문에 패키지 설치가 필요합니다.
# apk는 Alpine의 패키지 관리자입니다.
docker compose exec api apk add curl

# Step 4: web 컨테이너로 curl 요청
# 'web' 컨테이너는 nginx 서버이므로, HTTP 요청에 대해 기본 Welcome 페이지를 응답합니다.
# 응답으로 HTML 코드가 출력되면 통신이 정상적으로 이루어진 것입니다.
docker compose exec api curl http://web

# Step 5: 실행 상태 확인
# 현재 실행 중인 컨테이너 목록 확인
docker ps

# 참고 사항
Docker Compose는 기본적으로 모든 서비스에 대해 하나의 bridge 네트워크를 생성하여 각 컨테이너를 연결합니다.
Compose 내부의 컨테이너는 서비스 이름으로 서로를 인식하며, DNS처럼 동작합니다.
ping web 또는 curl http://web과 같이 web을 호스트명처럼 사용 가능합니다.