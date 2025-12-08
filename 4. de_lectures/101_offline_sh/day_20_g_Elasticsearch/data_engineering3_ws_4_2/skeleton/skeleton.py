from elasticsearch import Elasticsearch, helpers
import json
import time
import os

# TODO: Elasticsearch 클라이언트 생성
es = Elasticsearch("http://localhost:9200")
index_name = "ecommerce"

# ----------------------------------------------
# [1] 기존 인덱스 삭제
# ----------------------------------------------
# TODO: 인덱스 존재 여부 확인
if es.indices.exists(index=index_name):
    # TODO: 인덱스 삭제
    es.indices.delete(index=index_name)
    print("[1] 기존 인덱스 삭제 완료")
else:
    print("[1] 기존 인덱스 없음, 새로 생성 진행")
time.sleep(2)

# ----------------------------------------------
# [2] 인덱스 생성 및 매핑
# ----------------------------------------------
print("[2] 인덱스 생성 및 매핑 적용")
# TODO: Nested 및 geoip 필드 포함 매핑 적용
es.indices.create(
    index=index_name,
    body={
        "mappings": {
            "properties": {
                "customer_full_name": { "type": "text" },
                "manufacturer": { "type": "keyword" },
                "category": { "type": "keyword" },
                "order_date": { "type": "date" },
                "products": {
                    "type": "nested",
                    "properties": {
                        "product_name": { "type": "text" },
                        "category": { "type": "keyword" },
                        "price": { "type": "double" }
                    }
                },
                "geoip": {
                    "properties": {
                        "city_name": { "type": "text" }
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
    print(f" 파일 없음: {json_path}")
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
print("[3] Bulk 삽입 완료 및 리프레시")
time.sleep(2)

# ----------------------------------------------
# [4] 검색 테스트 함수 정의
# ----------------------------------------------
def run_query(label, query):
    print(f"\n {label}")
    # TODO: Query DSL 실행 (search API)
    result = es.search(index=index_name, body=query)
    for hit in result["hits"]["hits"]:
        print(f"\n ID: {hit['_id']}, Score: {hit['_score']}")
        print(json.dumps(hit["_source"], indent=2, ensure_ascii=False))

# ----------------------------------------------
# [4-1] 고객 이름 match query
# ----------------------------------------------
run_query("고객 이름 검색 (match query) - 'Eddie Underwood'", {
    "_source": ["customer_full_name", "email"],
    "query": {
        "match": { "customer_full_name": "Eddie" }
    },
    "size": 3
})

# ----------------------------------------------
# [4-2] 상품명 nested + multi_match query
# ----------------------------------------------
run_query("상품명 검색 (nested + multi_match) - 'T-shirt'", {
    "_source": ["products.product_name", "products.price"],
    "query": {
        "nested": {
            "path": "products",
            "query": {
                "multi_match": {
                    "query": "T-shirt",
                    "fields": ["products.product_name"]
                }
            },
            "inner_hits": {
                "_source": ["products.product_name", "products.price"]
            }
        }
    },
    "size": 3
})

# ----------------------------------------------
# [4-3] 최신 주문 정렬
# ----------------------------------------------
run_query("최신 주문 정렬 (order_date DESC)", {
    "_source": ["customer_full_name", "order_date"],
    "query": { "match_all": {} },
    "sort": [{ "order_date": "desc" }],
    "size": 3
})

# ----------------------------------------------
# [4-4] 제조사 wildcard 검색
# ----------------------------------------------
run_query("제조사 검색 (wildcard query) - 'Elitelligence*'", {
    "_source": ["manufacturer"],
    "query": {
        "wildcard": {
            "manufacturer": "Elitelligence*"
        }
    },
    "size": 3
})

print("\nElasticsearch Query DSL 테스트 완료!")
