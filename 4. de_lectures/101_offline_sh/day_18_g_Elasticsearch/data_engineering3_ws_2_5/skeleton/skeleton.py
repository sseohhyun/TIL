from elasticsearch import Elasticsearch
import time

# ----------------------------------------------
# 1. Elasticsearch 클라이언트 연결
# ----------------------------------------------
es = Elasticsearch("http://localhost:9200")

# ----------------------------------------------
# 2. 테스트 인덱스 이름 지정
# ----------------------------------------------
index_name = "simulate_failure_index"

# ----------------------------------------------
# 3. 클러스터 상태 출력 함수 정의
# ----------------------------------------------
def show_cluster_health(stage):
    health = es.cluster.health()  
    print(f"[{stage}] Cluster status: {health['status']}, Active shards: {health['active_shards']}, Unassigned: {health['unassigned_shards']}")
    print("-" * 40)

# ----------------------------------------------
# 4. 인덱스 생성 함수 정의 (샤드 2, 복제본 1)
# ----------------------------------------------
def create_index_with_replicas():
    if es.indices.exists(index=index_name):
        es.indices.delete(index=index_name)
        time.sleep(1)

    print("인덱스 생성 중 (샤드 2, 복제본 1)...")
    es.indices.create(index=index_name, body={
        "settings": {
            "number_of_shards": 2,
            "number_of_replicas": 1
        }
    })  
    time.sleep(5)

# ----------------------------------------------
# 5. 장애 유도: 복제본 샤드 할당 비활성화
# ----------------------------------------------
def simulate_failure():
    print("장애 유도 중... (replica 할당 금지)")
    es.cluster.put_settings(body={
        "persistent": {
            "cluster.routing.allocation.enable": "primaries"
        }
    })
    time.sleep(2)

    print("인덱스 삭제 후 재생성 (replica 존재하지만 할당 안됨)...")
    es.indices.delete(index=index_name)
    time.sleep(1)
    es.indices.create(index=index_name, body={
        "settings": {
            "number_of_shards": 2,
            "number_of_replicas": 1
        }
    })
    time.sleep(5)
# ----------------------------------------------
# 6. 복구: 할당 재허용
# ----------------------------------------------
def recover():
    print("복구 중... (replica 할당 재허용)")
    # TODO: cluster.routing.allocation.enable = all 세팅
    es.cluster.put_settings(body={
        "persistent" : {
            "cluster.routing.allocation.enable": "all"
        }
    })  
    time.sleep(5)

# ----------------------------------------------
# 7. 실행 흐름
# ----------------------------------------------
show_cluster_health("시작 상태")
create_index_with_replicas()
show_cluster_health("인덱스 생성 후 (정상 상태)")

simulate_failure()
show_cluster_health("장애 유도 후 (replica 미할당)")

recover()
show_cluster_health("복구 후 (전체 샤드 재할당)")
