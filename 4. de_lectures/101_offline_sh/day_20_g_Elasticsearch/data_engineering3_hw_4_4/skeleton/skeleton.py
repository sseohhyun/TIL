from elasticsearch import Elasticsearch, helpers
import json
import time
import os

# TODO: Elasticsearch 클라이언트 생성
es = Elasticsearch("http://localhost:9200")
index_name = "ecommerce"
index_name = "ecommerce"

# ----------------------------------------------
# [1] 인덱스 삭제
# ----------------------------------------------
# TODO: 인덱스 존재 여부 확인
if es.indices.exists(index=index_name):
    # TODO: 기존 인덱스 삭제
    es.indices.delete(index=index_name)
    print(f"[1] 기존 인덱스 [{index_name}] 삭제 완료")
else:
    print(f"[1] 기존 인덱스 [{index_name}] 없음, 새로 생성 진행")
time.sleep(2)

# ----------------------------------------------
# [2] 인덱스 생성 및 매핑
# ----------------------------------------------
print(f"[2] 인덱스 [{index_name}] 생성 및 매핑 적용")
# TODO: Nested products 필드 포함 인덱스 생성
es.indices.create(
    index=index_name,
    body={
        "mappings": {
            "properties": {
                "order_id": { "type": "keyword" },
                "customer_id": { "type": "integer" },
                "customer_gender": { "type": "keyword" },
                "total_price": { "type": "double" },
                "products": {
                    "type": "nested",
                    "properties": {
                        "product_id": { "type": "keyword" },
                        "category": { "type": "keyword" },
                        "price": { "type": "double" }
                    }
                }
            }
        }
    }
)
time.sleep(2)

# ----------------------------------------------
# [3] Bulk 데이터 삽입
# ----------------------------------------------
print("[3] Bulk 데이터 삽입 (ecommerce.json 사용)")
json_path = "../data/ecommerce.json"
if not os.path.exists(json_path):
    print(f"파일 없음: {json_path}")
    exit(1)

with open(json_path, "r", encoding="utf-8") as f:
    lines = f.read().splitlines()

actions = []
for i in range(0, len(lines), 2):
    action_line = json.loads(lines[i])
    doc_line = json.loads(lines[i + 1])
    
    action_type, meta = list(action_line.items())[0]
    index = meta.get("_index", index_name)
    doc_id = meta.get("_id")
    
    doc = {
        "_op_type": action_type,
        "_index": index,
        "_source": doc_line
    }
    if doc_id:
        doc["_id"] = doc_id
    
    actions.append(doc)

# TODO: Bulk 데이터 삽입
helpers.bulk(es, actions)

# TODO: 인덱스 리프레시
es.indices.refresh(index=index_name)
print("[3] Bulk 삽입 완료 및 인덱스 리프레시 완료")
time.sleep(2)

# ----------------------------------------------
# [4] Nested Bucket Aggregation
# ----------------------------------------------
print("[4] Nested Bucket Aggregation 실행 (MALE 고객의 상품 개수 및 평균 가격)")

query = {
    "size": 0,
    "query": {
        "term": {
            "customer_gender": "MALE"
        }
    },
    "aggs": {
        "products_nested": {
            "nested": { "path": "products" },
            "aggs": {
                "total_products": {
                    "value_count": {
                        "field": "products.product_id"
                    }
                },
                "avg_price": {
                    "avg": {
                        "field": "products.price"
                    }
                }
            }
        }
    }
}

# TODO: Nested Aggregation 쿼리 실행
response = es.search(index=index_name, body=query)

# ----------------------------------------------
# [5] 결과 출력
# ----------------------------------------------
print("\n[결과 요약]")
nested = response["aggregations"]["products_nested"]
print(f" - 전체 상품 수: {nested['total_products']['value']}")
print(f" - 평균 상품 가격: {nested['avg_price']['value']:.2f}")
