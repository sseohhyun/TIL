# Elasticsearch 컨테이너 실행을 위한 Shell Script
# 본 스크립트는 `docker-compose` 명령을 이용하여 Elasticsearch를 실행합니다.
# 실행 후, 컨테이너가 정상적으로 동작하는지 확인하는 루틴을 포함합니다.

# Docker-Compose를 사용하여 Elasticsearch 컨테이너를 백그라운드에서 실행
# docker-compose.yml 파일을 기반으로 컨테이너를 실행합니다.

# Elasticsearch 실행 상태 확인 루프
# Elasticsearch가 완전히 실행될 때까지 기다리는 역할을 합니다.
# 'curl'을 사용하여 localhost:9200에 접근해 응답을 확인합니다.
# 아직 실행되지 않았다면, 5초 후에 다시 확인하는 구조입니다.
while ! curl -X GET http://localhost:9200; 
do
  echo "Elasticsearch가 아직 실행되지 않았습니다. 잠시 후 다시 시도합니다..."
  sleep 5
done

echo "Elasticsearch가 정상적으로 실행되었습니다!"
