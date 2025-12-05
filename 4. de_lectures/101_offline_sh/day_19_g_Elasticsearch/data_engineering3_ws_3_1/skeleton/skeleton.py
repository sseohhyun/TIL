from elasticsearch import Elasticsearch
from elasticsearch.exceptions import NotFoundError
import time

# ----------------------------------------------
# 1. Elasticsearch 클라이언트 연결
# ----------------------------------------------
# TODO: 클러스터 연결
es = Elasticsearch("http://localhost:9200")
index_name = "dataset_index"

# ----------------------------------------------
# 2. 기존 인덱스 확인 및 삭제
# ----------------------------------------------
print("기존 인덱스 확인 및 삭제")
if es.indices.exists(index=index_name):
    es.indices.delete(index=index_name)  
    print(f"기존 인덱스 [{index_name}] 삭제 완료!")
else:
    print(f"기존 인덱스 [{index_name}] 없음, 새로 생성 진행.")
time.sleep(2)

# ----------------------------------------------
# 3. 인덱스 생성 및 매핑 설정
# ----------------------------------------------
print(f"새로운 인덱스 [{index_name}] 생성 및 매핑 설정 적용")
# id, title, description, category, price, release_date에 대해 매핑 설정
es.indices.create(index=index_name, body={
    "mappings": {
        "properties": {
            "id": {"type": "integer"},
            "title": {"type": "text", "analyzer": "standard"},
            "description": {"type": "text", "analyzer": "standard"},
            "category": {"type": "keyword"},
            "price": {"type": "integer"},
            "release_date": {"type": "date", "format": "yyyy-MM-dd"}
        }
    }
})
time.sleep(2)

# ----------------------------------------------
# 4. 샘플 데이터 색인
# ----------------------------------------------
print("샘플 데이터 색인")
docs = [
    {
        "id": 1,
        "title": "Elasticsearch Mapping Setup",
        "description": "This document explains how to configure mappings in Elasticsearch.",
        "category": "tech",
        "price": 50000,
        "release_date": "2024-01-15"
    },
    {
        "id": 2,
        "title": "Data Analysis with Elasticsearch",
        "description": "Learn how to analyze and search data efficiently.",
        "category": "data",
        "price": 70000,
        "release_date": "2023-12-25"
    }
]

# TODO: 각 문서를 색인
for i, doc in enumerate(docs, start=1):
    es.index(index=index_name, id=i, document=doc)

time.sleep(2)

# ----------------------------------------------
# 5. 매핑 확인
# ----------------------------------------------
print("인덱스 매핑 설정 확인")
# TODO: 매핑 정보 조회
mapping = es.indices.get_mapping(index=index_name)
print(mapping)

# ----------------------------------------------
# 6. 색인된 데이터 조회
# ----------------------------------------------
print("색인된 데이터 조회")
# TODO: 검색 쿼리 실행 및 결과 출력
result = es.search(index=index_name, query={"match_all": {}})  
for hit in result["hits"]["hits"]:
    print(f"ID: {hit['_id']}, Title: {hit['_source']['title']}")

print("Elasticsearch 데이터셋 매핑 설정 완료!")
