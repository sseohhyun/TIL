import pandas as pd
from elasticsearch import Elasticsearch

# 과제 Lv2에서 만들었던 데이터를 해당 위치로 이동 시켜 진행해야 합니다.

# CSV 파일 로드 및 변환
df = pd.read_csv("/home/ssafy/hadoop_data/transactions.csv")
records = df.to_dict(orient='records')

# Elasticsearch 클라이언트 생성
es = Elasticsearch("http://localhost:9200")

# 문서 인덱싱
for record in records:
    es.index(index="finance-index", document=record)


# category가 "food"인 문서 검색
query = {
    "query": {
        "match": {"transaction_date": "2024-01-08"}
    }
}

response = es.search(index='finance-index', body=query)

# 검색 결과 출력
for hit in response['hits']['hits']:
    print(hit['_source'])


# 인덱싱 후, Kibana Dev tools를 통해서 데이터를 확인하고 캡쳐하여 같이 업로드합니다.