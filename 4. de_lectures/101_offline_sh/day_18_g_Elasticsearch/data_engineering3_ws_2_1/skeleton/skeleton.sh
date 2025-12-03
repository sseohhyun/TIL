# docker-compose에서 이전까지는 단일 노드 상태였습니다.
# 해당 docker-compose 파일의 environment 파일에는 elasticsearch의 설정으로 주석을 해제하여 사용합니다.
# 해당 docker-compose 파일을 확인한 후, 3개의 elasticsearch nodes가 잘 연결되고 설정되었는지 확인합니다.

docker-compose up -d

echo "Elasticsearch 클러스터가 실행될 때까지 60초 대기 중..."
sleep 60

# 1. 클러스터 상태 확인
# - 클러스터 상태(green, yellow, red)를 출력하여 노드가 정상적으로 연결되었는지 점검합니다.
curl -X GET "http://localhost:9200/_cluster/health?pretty"
echo ""
# 참고 문서: https://www.elastic.co/guide/en/elasticsearch/reference/current/cluster-health.html

# 2. 클러스터 노드 목록 확인
# - 각 노드의 역할, 사용 메모리, CPU 사용량 등을 출력하여 점검할 수 있습니다.
curl -X GET "http://localhost:9200/_cat/nodes?v"
echo ""
# 참고 문서: https://www.elastic.co/guide/en/elasticsearch/reference/current/cat-nodes.html