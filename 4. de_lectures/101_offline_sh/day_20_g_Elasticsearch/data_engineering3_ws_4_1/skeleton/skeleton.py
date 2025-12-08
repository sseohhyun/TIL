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
# TODO: Nested + geoip 포함한 인덱스 생성
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

# TODO: Bulk 삽입 실행
helpers.bulk(es, actions)

# TODO: 인덱스 리프레시
es.indices.refresh(index=index_name)
print("[3] Bulk 삽입 완료 및 인덱스 리프레시 완료")
time.sleep(2)

# ----------------------------------------------
# [4] 검색 테스트 함수 정의
# ----------------------------------------------
def print_query_string_result(label, q, size=1, from_=None, sort=None):
    print(f"\n{label}")
    params = {
        "q": q,
        "size": size
    }
    if from_ is not None:
        params["from"] = from_
    if sort is not None:
        params["sort"] = sort

    # TODO: 검색 실행 (_search API 사용)
    res = es.search(index=index_name, params=params)

    for hit in res["hits"]["hits"]:
        source = hit["_source"]
        print(f"\nID: {hit['_id']}, Score: {hit['_score']}")
        print(f"  고객명: {source.get('customer_full_name', '-')}")
        print(f"  주문일: {source.get('order_date', '-')}")
        print(f"  제조사: {source.get('manufacturer', '-')}")
        if "products" in source:
            print(f"  ▶ 상품 목록:")
            for p in source["products"]:
                print(f"    - {p.get('product_name', '')} / {p.get('price', '')}원")

# ----------------------------------------------
# [4-1~4-5] 다양한 쿼리 테스트
# ----------------------------------------------
print_query_string_result("고객 이름 검색 - 'Eddie Underwood'", "customer_full_name:Eddie Underwood")
print_query_string_result("상품명 검색 - 'T-shirt'", "products.product_name:T-shirt")
print_query_string_result("제조사 검색 - 'Elitelligence*'", "manufacturer:Elitelligence*")
print_query_string_result("최신 주문 정렬 (order_date DESC)", "*", sort="order_date:desc")
print_query_string_result("페이징 검색 (from: 2, size: 3)", "*", from_=2, size=3)

print("\nElasticsearch _search API 테스트 완료")
