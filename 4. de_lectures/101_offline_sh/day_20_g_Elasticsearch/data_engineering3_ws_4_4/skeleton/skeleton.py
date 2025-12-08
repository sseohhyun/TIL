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
    # TODO: 기존 인덱스 삭제
    es.indices.delete(index=index_name)
    print(f"[1] 기존 인덱스 [{index_name}] 삭제 완료")
else:
    print(f"[1] 기존 인덱스 없음, 새로 생성 진행")
time.sleep(2)

# ----------------------------------------------
# [2] 인덱스 생성 및 custom analyzer 설정
# ----------------------------------------------
print(f"[2] 인덱스 [{index_name}] 생성 및 분석기 설정 적용")
# TODO: custom analyzer가 포함된 인덱스 생성
es.indices.create(
    index=index_name,
    body={
        "settings": {
            "analysis": {
                "analyzer": {
                    "custom_standard": {
                        "type": "custom",
                        "tokenizer": "standard",
                        "filter": ["lowercase", "stop"]
                    }
                }
            }
        },
        "mappings": {
            "properties": {
                "customer_full_name": { "type": "text", "analyzer": "custom_standard" },
                "manufacturer": { "type": "text", "analyzer": "custom_standard" },
                "category": { "type": "keyword" },
                "order_date": { "type": "date" },
                "products": {
                    "type": "nested",
                    "properties": {
                        "product_name": { "type": "text", "analyzer": "custom_standard" },
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

# TODO: Bulk 삽입 수행
helpers.bulk(es, actions)

# TODO: 인덱스 리프레시
es.indices.refresh(index=index_name)
print("[3] Bulk 삽입 완료 및 인덱스 리프레시 완료")
time.sleep(2)

# ----------------------------------------------
# [4] 검색 실행 함수 정의
# ----------------------------------------------
def run_query(label, query):
    print(f"\n{label}")
    # TODO: 검색 실행
    res = es.search(index=index_name, body=query)
    for hit in res["hits"]["hits"]:
        print(f"\n ID: {hit['_id']}, Score: {hit['_score']}")
        print(json.dumps(hit["_source"], indent=2, ensure_ascii=False))

# ----------------------------------------------
# [4-1] Match Query: 고객 이름
# ----------------------------------------------
run_query("Match Query - 고객 이름 'Eddie Underwood'", {
    "_source": ["customer_full_name", "email"],
    "query": {
        "match": { "customer_full_name": "Eddie" }
    },
    "size": 3
})

# ----------------------------------------------
# [4-2] Nested + Multi-Match Query: 상품명
# ----------------------------------------------
run_query("Nested Multi-Match - 상품명 'T-shirt'", {
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
# [4-3] Multi-Match (cross_fields): 고객명 + 상품명 통합 검색
# ----------------------------------------------
run_query("Multi-Match (cross_fields) - 'Eddie T-shirt'", {
    "_source": ["customer_full_name", "products.product_name"],
    "query": {
        "multi_match": {
            "query": "Eddie T-shirt",
            "fields": ["customer_full_name", "products.product_name"],
            "type": "cross_fields"
        }
    },
    "size": 3
})

# ----------------------------------------------
# [4-4] Match with Operator AND: category
# ----------------------------------------------
run_query("Match Query with Operator (AND) - 'Men Clothing'", {
    "_source": ["category"],
    "query": {
        "match": {
            "category": {
                "query": "Men Clothing",
                "operator": "and"
            }
        }
    },
    "size": 3
})

print("\nElasticsearch Match & Multi-Match Query 테스트 완료!")
