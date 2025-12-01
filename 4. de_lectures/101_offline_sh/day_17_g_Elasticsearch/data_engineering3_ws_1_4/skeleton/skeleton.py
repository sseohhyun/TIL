from elasticsearch import Elasticsearch, NotFoundError, helpers
import json

# Elasticsearch 클라이언트 생성
es = Elasticsearch("http://localhost:9200")

# 1. 기존 'products' 인덱스 삭제
try:
    # TODO: 'products' 인덱스를 삭제하는 코드를 작성하세요.
    es.indices.delete(index="products")  
    print("1. 'products' 인덱스 삭제 완료")
except NotFoundError:
    print("1. 삭제할 인덱스가 없음 (이미 삭제된 상태)")

# 2. 'products' 인덱스 생성
# TODO: 샤드와 복제본 설정 포함하여 인덱스를 생성하세요.
es.indices.create(
    index="products",
    body={
        "settings": {
            "number_of_shards": 1,
            "number_of_replicas": 0
        }
    }
)
print("2. 'products' 인덱스 생성 완료")

# 3. Bulk Insert 실행
bulk_insert_data = [
    {"_index": "products", "_id": "1", "_source": {
        "product_name": "Samsung Galaxy S25", "brand": "Samsung", "release_date": "2025-02-07", "price": 799}},
    {"_index": "products", "_id": "2", "_source": {
        "product_name": "iPhone 15 Pro", "brand": "Apple", "release_date": "2024-10-13", "price": 1199}},
    {"_index": "products", "_id": "3", "_source": {
        "product_name": "Google Pixel 8", "brand": "Google", "release_date": "2023-10-12", "price": 260}},
]

# TODO: helpers.bulk를 사용하여 bulk 문서를 삽입하세요.
helpers.bulk(es, bulk_insert_data)

# 강제로 색인 refresh
es.indices.refresh(index="products")
print("3. Bulk 문서 삽입 완료")

# 4. 삽입된 문서 조회
print("4. 삽입된 문서:")
res = es.search(index="products", query={"match_all": {}})
for hit in res["hits"]["hits"]:
    print(hit["_source"])

# 5. Bulk Update 실행
bulk_update_data = [
    {"_op_type": "update", "_index": "products", "_id": "1", "doc": {"price": 1099.99}},
    {"_op_type": "update", "_index": "products", "_id": "2", "doc": {"price": 1249.99}},
]

# TODO: helpers를 이용하여 bulk update 실행
helpers.bulk(es, bulk_update_data)  
print("5. Bulk 문서 가격 수정 완료")

# 6. 업데이트된 문서 확인
print("6. 업데이트된 문서:")
# TODO: 다시 전체 문서 조회
res = es.search(index="products", query={"match_all": {}})  
for hit in res["hits"]["hits"]:
    print(hit["_source"])

# 7. 'ecommerce' 인덱스 삭제
try:
    # TODO: 'ecommerce' 인덱스를 삭제
    es.indices.delete(index="ecommerce")  
    print("7. 'ecommerce' 인덱스 삭제 완료")
except NotFoundError:
    print("7. 삭제할 인덱스가 없음 (이미 삭제된 상태)")

# 8. 'ecommerce' 인덱스 생성
try:
    # TODO: 샤드 수 1, 복제본 수 0으로 인덱스 생성
    es.indices.create(index="ecommerce",
        body={
            "settings": {
                "number_of_shards": 1,
                "number_of_replicas": 0
            }})  
    print("8. 'ecommerce' 인덱스 생성 완료")
except Exception as e:
    print("8. 인덱스 생성 오류:", e)

# 9. Bulk Insert (파일 기반)
print("9. 'ecommerce.json' 파일을 이용한 Bulk 삽입")
try:
    with open("../data/ecommerce.json", "r", encoding="utf-8") as f:
        bulk_data_lines = f.readlines()

    actions = []
    for i in range(0, len(bulk_data_lines), 2):
        action = json.loads(bulk_data_lines[i])
        doc = json.loads(bulk_data_lines[i + 1])
        index = action["index"]["_index"]
        doc_id = action["index"]["_id"]
        actions.append({
            "_index": index,
            "_id": doc_id,
            "_source": doc
        })

    # TODO: helpers.bulk를 이용해 파일 기반 bulk 삽입
    helpers.bulk(es, actions)  
    # 강제로 색인 refresh
    es.indices.refresh(index="ecommerce")
    print("9. Bulk 파일 삽입 완료")

except FileNotFoundError:
    print("'ecommerce.json' 파일이 존재하지 않습니다.")

# 10. 특정 문서 확인 (ID=5)
try:
    # TODO: ID가 5인 문서를 조회
    doc = es.get(index="ecommerce", id=5)  
    print("10. ID가 5인 문서 내용:", doc["_source"])
except NotFoundError:
    print("10. ID 5 문서가 존재하지 않습니다.")
