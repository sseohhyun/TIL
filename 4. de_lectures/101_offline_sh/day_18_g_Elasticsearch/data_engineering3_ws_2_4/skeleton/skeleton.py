from elasticsearch import Elasticsearch
import time

# TODO: 반드시 기존에 쓰던 도커 파일이 아닌, 해당 과제와 같이 주어진 docker-compose.yml 파일을 사용해야 합니다.
# 이 도커 환경은 node별 role(tier)이 다르게 설정되어 있어야 합니다.

# ----------------------------------------------
# 1. Elasticsearch 클라이언트 연결
# ----------------------------------------------
# TODO: 클러스터에 연결
es = Elasticsearch("http://localhost:9200")

# ----------------------------------------------
# 2. 인덱스 이름 지정
# ----------------------------------------------
index_name = "logs-000001"

# ----------------------------------------------
# 3. 노드 역할 확인
# ----------------------------------------------
print("노드 역할 확인 (name, roles):")
# TODO: 노드 이름과 역할을 출력하는 cat API 호출
print(es.cat.nodes(format="text", h="name, roles"))

# ----------------------------------------------
# 4. 기존 인덱스 삭제 (있다면)
# ----------------------------------------------
if es.indices.exists(index=index_name):
    print(f"기존 인덱스 {index_name} 삭제 중...")
    es.indices.delete(index=index_name)  
    print("삭제 완료\n")

# ----------------------------------------------
# 5. 인덱스 생성 (Hot tier에 배치)
# ----------------------------------------------
print(f"인덱스 {index_name} 생성 중 (Hot tier)...")
# Hot tier에 배치되도록 인덱스 생성
es.indices.create(index=index_name, body={
    "settings": {
        "index.number_of_replicas": 0,
        "index.routing.allocation.include._tier_preference": "data_hot"
    }
})
print("생성 완료\n")

# ----------------------------------------------
# 6. 샤드 배치 상태 확인 (Hot tier)
# ----------------------------------------------
print("Hot tier 배치 상태 (샤드 위치):")
# TODO: 샤드 상태 출력
print(es.cat.shards(index=index_name, format="text"))

# ----------------------------------------------
# 7. 1분 대기 후 Warm tier로 이동
# ----------------------------------------------
print("1분 대기 중... 이후 Warm tier로 이동합니다.")
time.sleep(60)
# TODO: Warm tier로 이동 설정
es.indices.put_settings(index=index_name, body={
    "index.routing.allocation.include._tier_preference": "data_warm"
})
print("Warm tier 이동 설정 완료\n")
time.sleep(10)

# ----------------------------------------------
# 8. 샤드 배치 상태 확인 (Warm tier)
# ----------------------------------------------
print("Warm tier 배치 상태 (샤드 위치):")
# TODO: 샤드 상태 출력
print(es.cat.shards(index=index_name, format="text"))

# ----------------------------------------------
# 9. 1분 대기 후 Cold tier로 이동
# ----------------------------------------------
print("다시 1분 대기... 이후 Cold tier로 이동합니다.")
time.sleep(60)
# TODO: Cold tier로 이동 설정
es.indices.put_settings(index=index_name, body={
    "index.routing.allocation.include._tier_preference": "data_cold"
})
print("Cold tier 이동 설정 완료\n")
time.sleep(10)

# ----------------------------------------------
# 10. 샤드 배치 상태 확인 (Cold tier)
# ----------------------------------------------
print("Cold tier 배치 상태 (샤드 위치):")
# TODO: 샤드 상태 출력
print(s.cat.shards(index=index_name, format="text"))

print("전체 티어 이동 완료: Hot → Warm → Cold 확인" )
