from elasticsearch import Elasticsearch
import time

# ----------------------------------------------
# 1. Elasticsearch 클라이언트 연결
# ----------------------------------------------
es = Elasticsearch("http://localhost:9200")
index_name = "analyzer_comparison"

# ----------------------------------------------
# 2. 기존 인덱스 삭제
# ----------------------------------------------
if es.indices.exists(index=index_name):
    es.indices.delete(index=index_name)  
    print(f"기존 인덱스 [{index_name}] 삭제 완료")
else:
    print(f"기존 인덱스 [{index_name}] 없음, 새로 생성 진행")
time.sleep(2)

# ----------------------------------------------
# 3. 다양한 Analyzer 설정 포함한 인덱스 생성
# ----------------------------------------------
print(f"인덱스 [{index_name}] 생성 및 analyzer 설정 적용")
# TODO: text 필드를 기준으로 analyzer 5개 정의 (standard, whitespace, simple, stop, keyword)
es.indices.create(index=index_name, body={
    "mappings": {
        "properties": {
            "text": {
                "type": "text",
                "analyzer": "standard",
                "fields": {
                    "whitespace": { "type": "text", "analyzer": "whitespace" },
                    "simple": { "type": "text", "analyzer": "simple" },
                    "stop": { "type": "text", "analyzer": "stop" },
                    "keyword": { "type": "keyword" }
                }
            }
        }
    }
})
time.sleep(2)

# ----------------------------------------------
# 4. 테스트 문장 정의
# ----------------------------------------------
test_text = "The QUICK brown-fox 123 jumps!!! over & lazy-dogs?"

# ----------------------------------------------
# 5. analyzer 테스트 함수 정의
# ----------------------------------------------
def analyze_with(analyzer_name):
    print(f"\n[{analyzer_name.capitalize()} Analyzer 결과]")
    # TODO: analyze API 실행
    response = es.indices.analyze(index=index_name, body={
        "analyzer": analyzer_name,
        "text": test_text
    })
    for token in response["tokens"]:
        print(f"- {token['token']}")

# ----------------------------------------------
# 6. 각 Analyzer 비교 실행
# ----------------------------------------------
# TODO: standard, whitespace, simple, stop 순서대로 테스트
analyze_with("standard")
time.sleep(1)

analyze_with("whitespace")
time.sleep(1)

analyze_with("simple")
time.sleep(1)

analyze_with("stop")
time.sleep(1)

print("\nElasticsearch 기본 Analyzer 비교 테스트 완료!")
