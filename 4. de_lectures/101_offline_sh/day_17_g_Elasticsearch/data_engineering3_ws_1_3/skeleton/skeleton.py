from elasticsearch import Elasticsearch

# Elasticsearch 클라이언트 생성
es = Elasticsearch("http://localhost:9200")

# 사용할 인덱스 이름 지정
index_name = 'products'

# 1. 인덱스 생성
# - 인덱스가 존재하는지 확인 후, 없으면 생성
if not es.indices.exists(index=index_name):
    # TODO: 인덱스를 생성하는 코드를 작성하세요.
    es.indices.create(index=index_name)  
    print(f"인덱스 '{index_name}'가 생성되었습니다.")
else:
    print(f"인덱스 '{index_name}'는 이미 존재합니다.")

# 2. 문서 삽입
# - Elasticsearch에 새로운 문서를 추가하는 작업
doc = {
    'product_name': 'Samsung Galaxy S25',
    'brand': 'Samsung',
    'release_date': '2025-02-07',
    'price': 799
}

# TODO: 문서를 삽입하는 코드를 작성하세요.
res = es.index(index=index_name, id=1, document=doc)
print(f"문서 삽입 결과: {res['result']} (ID: {res['_id']})")

# 3. 문서 조회
# - ID가 1인 문서를 조회
# TODO: 문서를 조회하는 코드를 작성하세요.
res = es.get(index=index_name, id=1)  
print(f"문서 조회 결과: {res['_source']}")

# 4. 문서 수정 (부분 업데이트)
# - 가격을 수정하는 업데이트 수행
doc = {
    'price': 1099.99
}

# TODO: 문서를 업데이트하는 코드를 작성하세요.
res = es.update(index=index_name, id=1, doc=doc)  
print(f"문서 수정 결과: {res}")

# 5. 문서 삭제
# - ID가 1인 문서를 삭제
# TODO: 문서를 삭제하는 코드를 작성하세요.
res = es.delete(index=index_name, id=1)  
print(f"문서 삭제 결과: {res['result']} (ID: {res['_id']})")
