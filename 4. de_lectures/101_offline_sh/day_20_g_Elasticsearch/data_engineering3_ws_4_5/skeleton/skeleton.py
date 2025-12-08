from elasticsearch import Elasticsearch, helpers
import json
import time
import os

# TODO: Elasticsearch 클라이언트 생성
es = Elasticsearch("http://localhost:9200")
index_name = "ecommerce"

# 공통 실행 함수
def run_query(label, body, show_hits=True):
    print(f"\n{label}")
    # TODO: 쿼리 실행
    res = es.search(index=index_name, body=body)
    if show_hits:
        for hit in res["hits"]["hits"]:
            print(f" ID: {hit['_id']}, 고객명: {hit['_source'].get('customer_full_name', '-')}")
    else:
        print(json.dumps(res.get("aggregations", {}), indent=2, ensure_ascii=False))

# ----------------------------------------------
# [1] 기존 인덱스 삭제
# ----------------------------------------------
# TODO: 인덱스 존재 여부 확인
if es.indices.exists(index=index_name):
    # TODO: 인덱스 삭제
    es.indices.delete(index=index_name)
    print(f"[1] 기존 인덱스 [{index_name}] 삭제 완료")
else:
    print(f"[1] 기존 인덱스 없음, 새로 생성 진행")
time.sleep(2)

# ----------------------------------------------
# [2] 인덱스 생성 및 매핑
# ----------------------------------------------
print(f"[2] 인덱스 [{index_name}] 생성 및 매핑 적용")
# TODO: custom analyzer 및 nested 필드 포함 인덱스 생성
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
                "manufacturer": { "type": "keyword" },
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
print("[3] Bulk 데이터 삽입 (ecommerce.json)")
json_path = "../data/ecommerce.json"
if not os.path.exists(json_path):
    print(f" 파일 없음: {json_path}")
    exit(1)

with open(json_path, "r", encoding="utf-8") as f:
    lines = f.read().splitlines()

actions = []
for i in range(0, len(lines), 2):
    action_meta = json.loads(lines[i])
    doc = json.loads(lines[i + 1])
    meta = list(action_meta.values())[0]
    actions.append({
        "_index": meta.get("_index", index_name),
        "_id": meta.get("_id"),
        "_source": doc
    })

# TODO: Bulk 삽입 실행
helpers.bulk(es, actions)

# TODO: 인덱스 리프레시
es.indices.refresh(index=index_name)
print("[3] 데이터 삽입 및 인덱스 리프레시 완료")
time.sleep(2)

# ----------------------------------------------
# [4] Nested Exists Query
# ----------------------------------------------
run_query("[4] Nested Query - products.price 존재 여부 확인", {
    "size": 3,
    "_source": ["customer_full_name", "products.product_name", "products.price"],
    "query": {
        "nested": {
            "path": "products",
            "query": {
                "exists": { "field": "products.price" }
            }
        }
    }
})

# ----------------------------------------------
# [5] Stats Aggregation
# ----------------------------------------------
run_query("[5] Stats Aggregation - products.price", {
    "size": 0,
    "aggs": {
        "products_nested": {
            "nested": { "path": "products" },
            "aggs": {
                "stats_price": {
                    "stats": { "field": "products.price" }
                }
            }
        }
    }
}, show_hits=False)

# ----------------------------------------------
# [6] Extended Stats Aggregation
# ----------------------------------------------
run_query("[6] Extended Stats Aggregation - products.price", {
    "size": 0,
    "aggs": {
        "products_nested": {
            "nested": { "path": "products" },
            "aggs": {
                "extended_stats_price": {
                    "extended_stats": { "field": "products.price" }
                }
            }
        }
    }
}, show_hits=False)

# ----------------------------------------------
# [7] Percentiles Aggregation
# ----------------------------------------------
run_query("[7] Percentiles Aggregation - products.price", {
    "size": 0,
    "aggs": {
        "products_nested": {
            "nested": { "path": "products" },
            "aggs": {
                "percentiles_price": {
                    "percentiles": {
                        "field": "products.price",
                        "percents": [50, 75, 95, 99]
                    }
                }
            }
        }
    }
}, show_hits=False)

print("\nElasticsearch Nested Aggregation 테스트 완료!")
