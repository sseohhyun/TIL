# Docker 정상 작동 확인 및 컨테이너 상태 점검

# Step 1: 도커가 정상적으로 작동하는지 확인
# - hello-world 이미지는 Docker의 기본 테스트 이미지입니다.
# - 이 명령을 실행하면 도커 엔진이 잘 작동하는지 확인할 수 있습니다.
docker run hello-world

# Step 2: 실행했던 컨테이너 목록 확인
# - docker ps는 현재 실행 중인 컨테이너만 보여줍니다.
# - -a 옵션을 붙이면 중지된 컨테이너도 포함해 모든 컨테이너를 보여줍니다.
docker ps -a

# Step 3: 컨테이너 중지 (예시로 컨테이너 이름 또는 ID가 'abc123'인 경우)
# - 실행 중인 컨테이너를 중지합니다.
docker stop c7743e8aba2b5d1381bb074be62f5b26ea3a940ed69eeb2273a3b7243f4e0edf

# Step 4: 컨테이너 삭제
# - 중지된 컨테이너를 삭제합니다.
docker rm c7743e8aba2b5d1381bb074be62f5b26ea3a940ed69eeb2273a3b7243f4e0edf