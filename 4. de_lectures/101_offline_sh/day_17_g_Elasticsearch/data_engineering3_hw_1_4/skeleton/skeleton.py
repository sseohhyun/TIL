from elasticsearch import Elasticsearch, NotFoundError

# Elasticsearch 클라이언트 생성
# - Elasticsearch 인스턴스와 연결을 설정하는 함수
def create_es_client():
    return Elasticsearch(
        "http://localhost:9200"
    )

# 인덱스 존재 여부 확인 및 생성
# - 존재하지 않으면 새롭게 생성
def create_index(es, index_name):
    if not es.indices.exists(index=index_name):
        # TODO: 인덱스를 생성하는 코드를 작성하세요.
        es.indices.create(index=index_name)  
        print(f"인덱스 '{index_name}'가 생성되었습니다.")
    else:
        print(f"인덱스 '{index_name}'는 이미 존재합니다.")

# 문서 삽입
# - 특정 `doc_id`를 지정하여 문서를 인덱스에 추가
def insert_document(es, index_name, doc_id, doc):
    # TODO: 문서를 삽입하는 코드를 작성하세요.
    res = es.index(index=index_name, id=doc_id, document=doc)
    print(f"문서 삽입 결과(ID {doc_id}): {res['result']}") if res else print("문서 삽입 실패")

# 문서 조회
# - 특정 ID의 문서를 검색하여 반환
def get_document(es, index_name, doc_id):
    try:
        # TODO: 문서를 조회하는 코드를 작성하세요.
        res = es.get(index=index_name, id=doc_id)
        print(f"문서 조회 결과(ID {doc_id}): {res['_source']}")
        return res['_source']
    except NotFoundError:
        print(f"문서(ID {doc_id})가 존재하지 않습니다.")
        return None

# 문서 수정 (부분 업데이트)
# - 특정 필드만 업데이트 가능 (`doc` 키워드 사용)
def update_document(es, index_name, doc_id, update_fields):
    try:
        # TODO: 문서를 수정하는 코드를 작성하세요.
        res = es.update(index=index_name, id=doc_id, body={"doc": update_fields}) 
        print(f"문서 수정 결과(ID {doc_id}): {res['result']}") if res else print("문서 수정 실패")
    except NotFoundError:
        print(f"문서(ID {doc_id})가 존재하지 않아 수정할 수 없습니다.")

# Upsert 기능 (문서가 없으면 삽입, 있으면 수정)
# - 기존 문서가 없으면 새롭게 생성 (`doc_as_upsert=True`)
def upsert_document(es, index_name, doc_id, update_fields):
    # TODO: Upsert를 수행하는 코드를 작성하세요.
    res = es.update(index=index_name, id=doc_id, body={"doc": update_fields, "doc_as_upsert": True}) 
    print(f"Upsert 결과(ID {doc_id}): {res['result']}") if res else print("Upsert 실패")

# 문서 삭제
# - 특정 ID를 가진 문서를 삭제
def delete_document(es, index_name, doc_id):
    try:
        # TODO: 문서를 삭제하는 코드를 작성하세요.
        res = es.delete(index=index_name, id=doc_id) 
        print(f"문서 삭제 결과(ID {doc_id}): {res['result']}") if res else print("문서 삭제 실패")
    except NotFoundError:
        print(f"문서(ID {doc_id})가 존재하지 않아 삭제할 수 없습니다.")

# 실행 흐름 (메인 함수)
if __name__ == "__main__":
    es = create_es_client()  # Elasticsearch 클라이언트 생성
    index_name = "products"
    doc_id = 1

    # 예제 문서
    document = {
        "product_name": "Samsung Galaxy S25",
        "brand": "Samsung",
        "release_date": "2025-02-07",
        "price": 1199.99
    }
    
    # 1. 인덱스 생성
    create_index(es, index_name)

    # 2. 문서 삽입
    insert_document(es, index_name, doc_id, document)

    # 3. 문서 조회
    get_document(es, index_name, doc_id)

    # 4. 문서 수정 (가격 변경)
    update_document(es, index_name, doc_id, {"price": 1099.99})

    # 5. 문서 조회 (수정된 데이터 확인)
    get_document(es, index_name, doc_id)

    # 6. Upsert (문서가 없으면 생성, 있으면 업데이트)
    upsert_document(es, index_name, doc_id, {"price": 999.99})

    # 7. 문서 조회 (Upsert 확인)
    get_document(es, index_name, doc_id)

    # 8. 문서 삭제
    delete_document(es, index_name, doc_id)

    # 9. 문서 조회 (삭제 확인)
    get_document(es, index_name, doc_id)

    # 10. Upsert (문서가 없으면 생성, 있으면 업데이트)
    upsert_document(es, index_name, doc_id, {"price": 1399.99})

    # 11. 문서 조회 (Upsert 확인)
    get_document(es, index_name, doc_id)
