from elasticsearch import Elasticsearch, helpers
import json
import time
import os

# TODO: Elasticsearch 클라이언트 생성
es = Elasticsearch("http://localhost:9200")
index_name = "ecommerce"

# ----------------------------------------------
# 1. 기존 인덱스 삭제
# ----------------------------------------------
# TODO: 인덱스 존재 여부 확인
if es.indices.exists(index=index_name):
    # TODO: 기존 인덱스 삭제
    es.indices.delete(index=index_name)
    print(f"1. 기존 인덱스 [{index_name}] 삭제 완료")
else:
    print(f"1. 기존 인덱스 [{index_name}] 없음, 새로 생성 진행")
time.sleep(2)

# ----------------------------------------------
# 2. 인덱스 생성 (Nested 매핑 포함)
# ----------------------------------------------
print(f"2. 인덱스 [{index_name}] 생성 및 매핑 적용")
# TODO: Nested 필드를 포함한 인덱스 생성
es.indices.create(
    index=index_name,
    body={
        "settings": {
            "number_of_shards": 1,
            "number_of_replicas": 0
        },
        "mappings": {
            "properties": {
                "customer_full_name": { "type": "text" },
                "order_id": { "type": "keyword" },
                "order_date": { "type": "date" },
                "total_quantity": { "type": "integer" },
                "total_unique_products": { "type": "integer" },
                "products": {
                    "type": "nested",
                    "properties": {
                        "product_name": { "type": "text" },
                        "price": { "type": "double" },
                        "category": { "type": "keyword" },
                        "manufacturer": { "type": "keyword" }
                    }
                }
            }
        }
    }
)
time.sleep(2)

# ----------------------------------------------
# 3. Bulk 데이터 삽입
# ----------------------------------------------
print("3. 'ecommerce.json' 파일을 이용한 Bulk 삽입")

json_path = "../data/ecommerce.json"
if not os.path.exists(json_path):
    print(f"파일 없음: {json_path}")
    exit(1)

with open(json_path, "r", encoding="utf-8") as f:
    bulk_data_lines = f.readlines()

actions = []
for i in range(0, len(bulk_data_lines), 2):
    action = json.loads(bulk_data_lines[i])
    doc = json.loads(bulk_data_lines[i + 1])
    index = action["index"]["_index"]
    doc_id = action["index"].get("_id")
    action_doc = {"_index": index, "_source": doc}
    if doc_id:
        action_doc["_id"] = doc_id
    actions.append(action_doc)

# TODO: Bulk 문서 색인 수행
helpers.bulk(es, actions)

# TODO: 인덱스 refresh
es.indices.refresh(index=index_name)

print("3. Bulk 삽입 완료 및 refresh")
time.sleep(2)

# ----------------------------------------------
# 4. Nested Query 실행
# ----------------------------------------------
print("4. Nested Query 실행 (제조사가 'Elitelligence'인 제품 검색)")

query = {
    "size": 3,
    "query": {
        "nested": {
            "path": "products",
            "query": {
                "bool": {
                    "must": [
                        { "match": { "products.manufacturer": "Elitelligence" } }
                    ]
                }
            },
            "inner_hits": {}
        }
    }
}

# TODO: Nested 쿼리 실행
response = es.search(index=index_name, body=query)

# ----------------------------------------------
# 5. 검색 결과 출력
# ----------------------------------------------
print("5. 검색 결과 출력")
for hit in response["hits"]["hits"]:
    customer = hit["_source"].get("customer_full_name", "(이름 없음)")
    print(f"\n고객: {customer}")
    inner_hits = hit.get("inner_hits", {}).get("products", {}).get("hits", {}).get("hits", [])
    for inner in inner_hits:
        p = inner["_source"]
        print(f"  → 제품명: {p['product_name']}, 제조사: {p['manufacturer']}")

print("\nElasticsearch Nested Query 테스트 완료!")
