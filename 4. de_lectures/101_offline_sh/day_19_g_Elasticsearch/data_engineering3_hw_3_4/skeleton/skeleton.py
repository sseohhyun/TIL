from elasticsearch import Elasticsearch
from elasticsearch.exceptions import NotFoundError
import time
import json

# ----------------------------------------------
# 1. Elasticsearch 클라이언트 연결
# ----------------------------------------------
# TODO: 클러스터에 연결
es = Elasticsearch("http://localhost:9200")
index_name = "korean_nori"

# ----------------------------------------------
# 2. Nori 플러그인 설치 여부 확인
# ----------------------------------------------
print("Nori 플러그인 설치 여부 확인")
node_info = es.nodes.info()
nori_installed = any(
    "analysis-nori" in plugin["name"]
    for node in node_info["nodes"].values()
    for plugin in node.get("plugins", [])
)

if not nori_installed:
    print("Nori 플러그인이 설치되지 않음. 설치 후 다시 실행하세요.")
    exit(1)
else:
    print("Nori 플러그인이 설치됨.\n")

time.sleep(2)

# ----------------------------------------------
# 3. 기존 인덱스 삭제
# ----------------------------------------------
print("기존 인덱스 확인 및 삭제")
if es.indices.exists(index=index_name):
    es.indices.delete(index=index_name)  
    print(f"기존 인덱스 [{index_name}] 삭제 완료!\n")
else:
    print(f"기존 인덱스 [{index_name}] 없음, 새로 생성 진행.\n")

time.sleep(2)

# ----------------------------------------------
# 4. Nori 분석기 적용 인덱스 생성
# ----------------------------------------------
print(f"Nori 분석기를 적용한 인덱스 [{index_name}] 생성")
es.indices.create(index=index_name, body={
    "settings": {
        "analysis": {
            "tokenizer": {
                "nori_user_dict": {
                    "type": "nori_tokenizer",
                    "decompound_mode": "mixed"
                }
            },
            "analyzer": {
                "korean_nori_analyzer": {
                    "type": "custom",
                    "tokenizer": "nori_tokenizer",
                    "filter": ["nori_part_of_speech"]
                }
            }
        }
    },
    "mappings": {
        "properties": {
            "text": {
                "type": "text",
                "analyzer": "korean_nori_analyzer"
            }
        }
    }
})
print("인덱스 생성 완료\n")
time.sleep(2)

# ----------------------------------------------
# 5. 문서 색인 (한국어 문장)
# ----------------------------------------------
print("한국어 문장 색인")
docs = [
    {"text": "엘라스틱서치는 검색 기능을 제공합니다."},
    {"text": "한국어 형태소 분석을 위해 Nori를 활용할 수 있습니다."}
]

# TODO: 두 개 문서 색인
for i, doc in enumerate(docs, start=1):
    es.index(index=index_name, id=i, document=doc)  
print("문서 색인 완료\n")
time.sleep(2)

# ----------------------------------------------
# 6. 검색 테스트 (match_phrase)
# ----------------------------------------------
print("Nori를 활용한 검색 테스트")
query = {
    "query": {
        "match_phrase": {
            "text": "검색 기능"
        }
    }
}

# TODO: 검색 실행
result = es.search(index=index_name, query=query['query'])
for hit in result["hits"]["hits"]:
    print(f"ID: {hit['_id']}, Score: {hit['_score']}, Text: {hit['_source']['text']}")

print("\nNori 기반 한국어 분석 작업 완료!")
