from elasticsearch import Elasticsearch

# Elasticsearch 클라이언트 생성
es = Elasticsearch("http://localhost:9200")

# 사용할 인덱스 이름 지정
index_name = 'products'

# ----------------------------------------------
# 1. 인덱스 생성
# - 인덱스가 존재하는지 확인 후, 없으면 생성
# ----------------------------------------------
if not es.indices.exists(index=index_name):
    # TODO: 인덱스를 생성하는 코드를 작성하세요.
    es.indices.create(index=index_name)
    print(f"인덱스 '{index_name}'가 생성되었습니다.")
else:
    print(f"인덱스 '{index_name}'는 이미 존재합니다.")

# ----------------------------------------------
# 2. 인덱스 목록 확인 (_cat/indices?v)
# - curl -X GET "localhost:9200/_cat/indices?v"
# - 현재 클러스터의 모든 인덱스 목록 출력
# - 인덱스 이름, 상태, 샤드 수, 문서 수 등 포함
# ----------------------------------------------
print("2. 인덱스 목록 확인")
# TODO: 인덱스 목록을 출력하는 코드를 작성하세요.
indices = es.cat.indices(format="json")  
for idx in indices:
    print(f"인덱스: {idx['index']}, 상태: {idx['status']}, 샤드: {idx['pri']}, 문서 수: {idx['docs.count']}")
print()

# ----------------------------------------------
# 3. 특정 인덱스의 설정 정보 조회
# - curl -X GET "localhost:9200/products/_settings?pretty"
# - 인덱스 'products'의 샤드 수, 복제본 등 확인
# ----------------------------------------------
print("3. 'products' 인덱스의 설정 정보 조회")
try:
    # TODO: 인덱스 설정을 조회하는 코드를 작성하세요.
    settings = es.indices.get_settings(index=index_name)  
    print(settings["products"]["settings"])
except Exception as e:
    print(f"[오류] 설정 조회 실패: {e}")
print()
