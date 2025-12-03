from elasticsearch import Elasticsearch
import time
import pprint

# Elasticsearch 클라이언트 연결
es = Elasticsearch("http://localhost:9200")

# ----------------------------------------------
# 1. 기존 인덱스 삭제
# ----------------------------------------------
print("기존 인덱스(my_index) 삭제 중...")
if es.indices.exists(index="my_index"):
    es.indices.delete(index="my_index")  
print("삭제 완료\n")

# ----------------------------------------------
# 2. 인덱스 생성 (샤드 3, 복제본 1)
# ----------------------------------------------
print("새로운 인덱스(my_index) 생성 중...")
es.indices.create(
    index="my_index",
    body={
        "settings": {
            "index": {
                "number_of_shards": 3,
                "number_of_replicas": 1
            }
        }
    }
)
print("생성 완료\n")
print("생성 완료\n")

# ----------------------------------------------
# 3. 테스트 데이터 삽입
# ----------------------------------------------
print("테스트 데이터 삽입 중...")
docs = [
    {
        "id": "1",
        "body": {
            "product_name": "Samsung Galaxy S25",
            "brand": "Samsung",
            "release_date": "2025-02-07",
            "price": 799
        }
    },
    {
        "id": "2",
        "body": {
            "product_name": "iPhone 15 Pro",
            "brand": "Apple",
            "release_date": "2024-10-13",
            "price": 1199
        }
    }
]

# TODO: 두 문서를 my_index에 삽입
for doc in docs:
    es.index(index="my_index", id=doc["id"], document=doc["body"])  
print("삽입 완료\n")

# ----------------------------------------------
# 4. 현재 샤드 배치 확인
# ----------------------------------------------
print("현재 샤드 배치 확인 중... (my_index)")
shards_info = es.cat.shards(format="json")  
for shard in shards_info:
    if shard["index"] == "my_index":
        print(f"Index: {shard['index']}, Shard: {shard['shard']}, Node: {shard['node']}, State: {shard['state']}")
print()

# ----------------------------------------------
# 5. 강제 샤드 이동 요청 (es01 노드로 집중)
# ----------------------------------------------
print("샤드 이동: es01 노드로 이동 요청 중...")
es.cluster.put_settings(body={
    "transient": {
        "cluster.routing.allocation.include._name": "es01"
    }
})
print("설정 완료\n")

# ----------------------------------------------
# 6. 샤드 이동 대기
# ----------------------------------------------
print("샤드 이동 중... (5초 대기)")
time.sleep(5)

# ----------------------------------------------
# 7. 샤드 이동 결과 확인
# ----------------------------------------------
print("샤드 이동 후 배치 상태 확인... (my_index)")
shards_info = es.cat.shards(format="json")  
for shard in shards_info:
    if shard["index"] == "my_index":
        print(f"Index: {shard['index']}, Shard: {shard['shard']}, Node: {shard['node']}, State: {shard['state']}")
print()

# ----------------------------------------------
# 8. 자동 할당 재설정 (특정 노드 제약 해제)
# ----------------------------------------------
print("데이터 자동 재배치 설정 초기화...")
es.cluster.put_settings(body={
    "transient": {
        "cluster.routing.allocation.include._name": None
    }
})
print("초기화 완료\n")

# ----------------------------------------------
# 9. 데이터 재배치 대기
# ----------------------------------------------
print("데이터 재배치 중... (5초 대기)")
time.sleep(5)

# ----------------------------------------------
# 10. 최종 샤드 배치 확인
# ----------------------------------------------
print("최종 샤드 배치 확인... (my_index)")
shards_info = es.cat.shards(format="json")    
for shard in shards_info:
    if shard["index"] == "my_index":
        print(f"Index: {shard['index']}, Shard: {shard['shard']}, Node: {shard['node']}, State: {shard['state']}")
print("샤드 이동 및 데이터 재배치 완료!")
