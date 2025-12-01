from elasticsearch import Elasticsearch, NotFoundError

# Elasticsearch 클라이언트 생성
es = Elasticsearch("http://localhost:9200")

index_name = "products"
doc_id = 1

# 1. 기존 문서 삭제 (Upsert 테스트 준비)
try:
    # TODO: 문서를 삭제하는 코드를 작성하세요.
    es.delete(index=index_name, id=doc_id)  
    print("1. 기존 문서 삭제 완료 (업서트 테스트 준비)")
except NotFoundError:
    print("1. 삭제할 문서가 없음 (이미 삭제된 상태)")

# 2. Upsert 실행 - 문서가 없으면 삽입
upsert_body_1 = {
    "doc": {
        "price": 999.99
    },
    "doc_as_upsert": True
}
# TODO: upsert 기능을 호출하는 코드를 작성하세요.
response_1 = es.update(index=index_name, id=doc_id, body=upsert_body_1)
print("2. 업서트 (없으면 삽입):", response_1["result"])

# 3. 문서 조회
# TODO: 문서를 조회하는 코드를 작성하세요.
doc = es.get(index=index_name, id=doc_id)
print("3. 문서 내용:", doc["_source"])