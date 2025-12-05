from elasticsearch import Elasticsearch
from elasticsearch.exceptions import NotFoundError
import time

# Elasticsearch 클라이언트 연결
es = Elasticsearch("http://localhost:9200")

index_name = "logs-000001"
alias_name = "logs-alias"

# ----------------------------------------------
# 1. 기존 인덱스 삭제
# ----------------------------------------------
print("기존 인덱스 확인 및 삭제")
if es.indices.exists(index=index_name):
    es.indices.delete(index=index_name)  
    print(f"기존 인덱스 [{index_name}] 삭제 완료")
else:
    print(f"기존 인덱스 [{index_name}] 없음. 새로 생성 진행.")
print()
time.sleep(1)

# ----------------------------------------------
# 2. 인덱스 생성
# ----------------------------------------------
print(f"인덱스 [{index_name}] 생성")
# TODO: 복제본 수 0으로 설정하여 인덱스 생성
es.indices.create(
    index=index_name,
    body={
        "settings": {
            "number_of_replicas": 0
        }
    }
)  
print(f"인덱스 [{index_name}] 생성 완료")
time.sleep(1)

# ----------------------------------------------
# 3. 앨리어스 추가
# ----------------------------------------------
print(f"앨리어스 [{alias_name}] 추가 → 인덱스 [{index_name}]")
# TODO: update_aliases API를 사용해 앨리어스 추가
es.indices.update_aliases(body={
    "actions": [
        {"add" : {"index": index_name, "alias": alias_name}}
    ]
})  
print(f"앨리어스 [{alias_name}] 추가 완료")
print()
time.sleep(1)

# ----------------------------------------------
# 4. 현재 모든 앨리어스 조회
# ----------------------------------------------
print("logs-* 패턴에 해당하는 앨리어스만 조회")
aliases = es.cat.aliases(format="json")
for alias in aliases:
    if alias["alias"].startswith("logs-"):
        print(f'{alias["alias"]:<45} {alias["index"]}')
print()
time.sleep(1)


# ----------------------------------------------
# 5. 특정 앨리어스로 인덱스 조회
# ----------------------------------------------
print("앨리어스를 이용하여 해당하는 인덱스 찾기")
try:
    alias_info = es.indices.get_alias(name=alias_name)  
    for idx in alias_info:
        print(f"{alias_name} → {idx}")
except NotFoundError:
    print(f"앨리어스 [{alias_name}]를 찾을 수 없습니다.")
print()
time.sleep(1)

# ----------------------------------------------
# 6. 앨리어스 삭제
# ----------------------------------------------
print(f"앨리어스 [{alias_name}] 삭제 → 인덱스 [{index_name}]")
# TODO: alias를 제거하는 update_aliases 호출
es.indices.update_aliases(body={
    "actions": [
        {"remove": {"index": index_name, "alias": alias_name}}
    ]
})  
print(f"앨리어스 [{alias_name}] 삭제 완료")
print()
time.sleep(1)

# ----------------------------------------------
# 7. 삭제 후 앨리어스 다시 조회
# ----------------------------------------------
print("앨리어스 삭제 후 조회")
aliases_after = es.cat.aliases(format="json")
for alias in aliases_after:
    if alias["alias"].startswith("logs-"):
        print(f'{alias["alias"]:<45} {alias["index"]}')
print()

print("인덱스 및 앨리어스 관리 작업 완료")
