from elasticsearch import Elasticsearch
import time
from pprint import pprint

# Elasticsearch 클라이언트 연결
es = Elasticsearch("http://localhost:9200")

# 인덱스 이름 정의
static_index = "static_mapping_index"
dynamic_index = "dynamic_mapping_index"

# ----------------------------------------------
# 인덱스 삭제 함수
# ----------------------------------------------
def delete_index(index_name):
    if es.indices.exists(index=index_name):
        es.indices.delete(index=index_name)  
        print(f"기존 인덱스 [{index_name}] 삭제 완료")
    else:
        print(f"기존 인덱스 [{index_name}] 없음, 새로 생성 진행")

# ----------------------------------------------
# 정적 매핑 인덱스 생성 함수
# ----------------------------------------------
def create_static_index():
    # TODO: id, name, age, email, signup_date를 명시적으로 정의
    es.indices.create(index=static_index, body={
        "mappings": {
            "properties": {
                "id": { "type": "integer" },
                "name": { "type": "text", "analyzer": "standard" },
                "age": { "type": "integer" },
                "email": { "type": "keyword" },
                "signup_date": { "type": "date", "format": "yyyy-MM-dd" }
            }
        }
    })
    print(f"[{static_index}] 생성 완료")

# ----------------------------------------------
# 동적 매핑 인덱스 생성 함수
# ----------------------------------------------
def create_dynamic_index():
    # TODO: dynamic: true 설정만 포함
    es.indices.create(index=dynamic_index, body={
        "mappings": {
            "dynamic": True
        }
    })
    print(f"[{dynamic_index}] 생성 완료")

# ----------------------------------------------
# 데이터 색인 함수
# ----------------------------------------------
def index_sample_data():
    # TODO: 정적 인덱스에 문서 삽입
    es.index(index=static_index, id=1, document={
        "id": 1,
        "name": "Alice",
        "age": 28,
        "email": "alice@example.com",
        "signup_date": "2024-01-15"
    })

    # TODO: 동적 인덱스에 새로운 필드 포함하여 삽입
    es.index(index=dynamic_index, id=1, document={
        "id": 1,
        "name": "Bob",
        "age": 30,
        "email": "bob@example.com",
        "signup_date": "2025-02-23",
        "new_field": "This field was dynamically added!"
    })

    print("샘플 데이터 색인 완료")

# ----------------------------------------------
# 매핑 정보 출력 함수
# ----------------------------------------------
def print_mappings():
    # TODO: 정적, 동적 인덱스의 매핑 정보 출력
    print("\n[정적 매핑 인덱스 매핑 정보]")
    static_index_mapping = es.indices.get_mapping(index=static_index)
    pprint(static_index_mapping)
    
    print("\n[동적 매핑 인덱스 매핑 정보]")
    dynamic_index_mapping = es.indices.get_mapping(index=dynamic_index)
    pprint(dynamic_index_mapping)

# ----------------------------------------------
# 색인된 문서 출력 함수
# ----------------------------------------------
def print_documents():
    print("\n[정적 매핑 인덱스 데이터]")
    result = es.search(index=static_index, query={"match_all": {}})  
    for hit in result["hits"]["hits"]:
        print(hit["_source"])

    print("\n[동적 매핑 인덱스 데이터]")
    result = es.search(index=dynamic_index, query={"match_all": {}})  
    for hit in result["hits"]["hits"]:
        print(hit["_source"])

# ----------------------------------------------
# 실행 흐름
# ----------------------------------------------
print("Elasticsearch 정적 매핑 vs 동적 매핑 비교")
delete_index(static_index)
delete_index(dynamic_index)
time.sleep(1)

create_static_index()
create_dynamic_index()
time.sleep(1)

index_sample_data()
time.sleep(1)

print_mappings()
print_documents()

print("\n비교 완료!")
