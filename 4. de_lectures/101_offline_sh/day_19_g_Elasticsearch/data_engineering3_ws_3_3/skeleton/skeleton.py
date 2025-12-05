from elasticsearch import Elasticsearch
import time

# ----------------------------------------------
# 1. Elasticsearch 클라이언트 연결 및 인덱스 정의
# ----------------------------------------------
es = Elasticsearch("http://localhost:9200")
index_name = "ecommerce"

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
# 3. 인덱스 생성 및 매핑 설정
# - title: text / category: keyword
# ----------------------------------------------
print("인덱스 생성 및 매핑 설정 적용")
# TODO: 두 필드의 타입을 각각 text와 keyword로 설정
es.indices.create(index=index_name, body={
    "mappings": {
        "properties": {
            "title": {
                "type": "text",
                "analyzer": "standard"
            },
            "category": {
                "type": "keyword"
            }
        }
    }
})
time.sleep(2)

# ----------------------------------------------
# 4. 샘플 데이터 삽입
# ----------------------------------------------
docs = [
    {"title": "Elasticsearch Mapping Setup", "category": "search_engine"},
    {"title": "Data Analysis with Elasticsearch", "category": "data"}
]

# TODO: 문서 색인
for i, doc in enumerate(docs, start=1):
    es.index(index=index_name, id=i, document=doc)  
print("샘플 데이터 삽입 완료")
time.sleep(2)

# ----------------------------------------------
# 5. `text` 필드 match 검색
# ----------------------------------------------
print("\n[text 필드 match 검색: title contains 'Search']")
text_query = {
    "query": {
        "match": {
            "title": "Search"
        }
    }
}
# TODO: 검색 실행
text_result = es.search(index=index_name, query=text_query['query'])  
for hit in text_result["hits"]["hits"]:
    print(f"Match → ID: {hit['_id']}, Title: {hit['_source']['title']}")

time.sleep(2)

# ----------------------------------------------
# 6. `keyword` 필드 term 검색
# ----------------------------------------------
print("\n[keyword 필드 term 검색: category = 'search_engine']")
keyword_query = {
    "query": {
        "term": {
            "category": "search_engine"
        }
    }
}
# TODO: term 검색 실행
kw_result = es.search(index=index_name, query=keyword_query['query'])  
for hit in kw_result["hits"]["hits"]:
    print(f"Term Match → ID: {hit['_id']}, Category: {hit['_source']['category']}")

time.sleep(2)

# ----------------------------------------------
# 7. `keyword` 필드 정렬
# ----------------------------------------------
print("\n[keyword 필드 기준 정렬 (오름차순)]")
sort_query = {
    "sort": [
        {"category": {"order": "asc"}}
    ]
}
# TODO: 정렬 쿼리 실행
sort_result = es.search(index=index_name, sort=sort_query['sort'])  
for hit in sort_result["hits"]["hits"]:
    print(f"Sorted → ID: {hit['_id']}, Category: {hit['_source']['category']}")

print("\nElasticsearch 문자열 필드 타입 분석 완료!")
