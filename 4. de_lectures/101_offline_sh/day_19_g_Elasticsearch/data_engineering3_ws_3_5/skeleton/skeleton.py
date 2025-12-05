from elasticsearch import Elasticsearch
import json
import time

# TODO: Elasticsearch 클라이언트 생성
es = Elasticsearch("http://localhost:9200")
index_name = "synonym_stopword_test"

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
# [2] 동의어 및 불용어 필터가 포함된 인덱스 생성
# ----------------------------------------------
print(f"[2] 인덱스 [{index_name}] 생성 및 분석기 설정 적용")
# TODO: 동의어 필터 및 불용어 필터 포함한 custom analyzer 설정
es.indices.create(
    index=index_name,
    body={
        "settings": {
            "analysis": {
                "filter": {
                    "synonym_filter": {
                        "type": "synonym",
                        "synonyms": ["quick, fast, speedy", "jumps, leaps, hops"]
                    },
                    "stopword_filter": {
                        "type": "stop",
                        "stopwords": ["the", "is", "and", "or", "an"]
                    }
                },
                "analyzer": {
                    "synonym_analyzer": {
                        "type": "custom",
                        "tokenizer": "standard",
                        "filter": ["lowercase", "synonym_filter"]
                    },
                    "stopword_analyzer": {
                        "type": "custom",
                        "tokenizer": "standard",
                        "filter": ["lowercase", "stopword_filter"]
                    }
                }
            }
        },
        "mappings": {
            "properties": {
                "text": {
                    "type": "text",
                    "analyzer": "standard",
                    "fields": {
                        "synonym": {
                            "type": "text",
                            "analyzer": "synonym_analyzer"
                        },
                        "stopword": {
                            "type": "text",
                            "analyzer": "stopword_analyzer"
                        }
                    }
                }
            }
        }
    }
)
time.sleep(2)

# ----------------------------------------------
# [3] 샘플 문서 삽입
# ----------------------------------------------
print("[3] 샘플 문서 삽입")
docs = [
    {"text": "The quick brown fox jumps over the lazy dog"},
    {"text": "Speedy rabbits leaps across the field"}
]

for i, doc in enumerate(docs, start=1):
    # TODO: 문서 색인
    es.index(index=index_name, id=i, document=doc)

# TODO: 인덱스 리프레시
es.indices.refresh(index=index_name)
time.sleep(2)

# ----------------------------------------------
# [4] 동의어 분석기 테스트
# ----------------------------------------------
print("[4] 동의어 분석기 테스트 (synonym_analyzer)")
# TODO: 동의어 분석기 분석 실행
synonym_tokens = es.indices.analyze(
    index=index_name,
    body={
        "analyzer": "synonym_analyzer",
        "text": "fast rabbits jumps quickly"
    }
)
print("토큰:", [token["token"] for token in synonym_tokens["tokens"]])
time.sleep(2)

# ----------------------------------------------
# [5] 불용어 분석기 테스트
# ----------------------------------------------
print("[5] 불용어 분석기 테스트 (stopword_analyzer)")
# TODO: 불용어 분석기 분석 실행
stopword_tokens = es.indices.analyze(
    index=index_name,
    body={
        "analyzer": "stopword_analyzer",
        "text": "The quick brown fox jumps over the lazy dog"
    }
)
print("토큰:", [token["token"] for token in stopword_tokens["tokens"]])
time.sleep(2)

# ----------------------------------------------
# [6] 동의어 검색 테스트
# ----------------------------------------------
print("[6] 동의어 검색 테스트 (fast 검색 시 quick 포함 여부)")
# TODO: synonym 필드를 대상으로 match 검색
synonym_result = es.search(
    index=index_name,
    body={
        "query": {
            "match": {
                "text.synonym": "fast"
            }
        }
    }
)
for hit in synonym_result["hits"]["hits"]:
    print(f" ID: {hit['_id']}, Text: {hit['_source']['text']}")
time.sleep(2)

# ----------------------------------------------
# [7] 불용어 제거 필드 검색 테스트
# ----------------------------------------------
print("[7] 불용어 필터 검색 테스트 ('quick brown fox')")
# TODO: stopword 필드를 대상으로 match 검색
stopword_result = es.search(
    index=index_name,
    body={
        "query": {
            "match": {
                "text.stopword": "quick brown fox"
            }
        }
    }
)
for hit in stopword_result["hits"]["hits"]:
    print(f" ID: {hit['_id']}, Text: {hit['_source']['text']}")

print("\nElasticsearch 동의어 및 불용어 사전 테스트 완료!")
