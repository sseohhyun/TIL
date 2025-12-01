from elasticsearch import Elasticsearch

# Elasticsearch 클라이언트 생성
es = Elasticsearch("http://localhost:9200")

# 사용할 인덱스 이름 지정
index_name = 'products'

# 1. 인덱스 생성
# - 인덱스가 존재하는지 확인 후, 없으면 생성
if not es.indices.exists(index=index_name):
    es.indices.create(index=index_name)
    print(f"인덱스 '{index_name}'가 생성되었습니다.")
else:
    print(f"인덱스 '{index_name}'는 이미 존재합니다.")

# 2. 문서 삽입
# - Elasticsearch에 새로운 문서를 추가하는 작업
# - `id=1`을 지정하여 문서를 삽입 (ID를 지정하지 않으면 자동 생성)
doc = {
    'product_name': 'Samsung Galaxy S25',
    'brand': 'Samsung',
    'release_date': '2025-02-07',  # 출시일 (ISO 8601 날짜 형식)
    'price': 799  # 가격 (float 형식)
}

# 문서 삽입 실행
# TODO: 지정된 ID로 문서 저장
res = es.index(index=index_name, id=1, document=doc)
print(f"문서 삽입 결과: {res['result']} (ID: {res['_id']})")

# 3. 문서 조회
# - TODO: 특정 문서를 ID(id가 1인 문서) 기반으로 조회하는 API
res = es.get(index=index_name, id=1)
print(f"문서 조회 결과: {res['_source']}")

# 4. 문서 수정 (부분 업데이트)
# - 기존 문서를 수정하는 방법으로 `update` API 사용
# - `doc` 키워드 내에 수정할 필드만 포함하면 해당 필드만 업데이트됨
doc= {
    'price': 1099.99  # 가격 수정
}


# 문서 업데이트 실행
# TODO: 특정 문서를 ID(id가 1인 문서) 기반으로 업데이트 하는 API
res = es.update(index=index_name, id=1, doc=doc)
print(f"문서 수정 결과: {res}")

# 5. 문서 삭제
# - TODO: `delete` API를 사용하여 특정 ID의 문서를 삭제
res = es.delete(index=index_name, id=1)
print(f"문서 삭제 결과: {res['result']} (ID: {res['_id']})")
