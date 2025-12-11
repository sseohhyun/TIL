import pandas as pd
from elasticsearch import Elasticsearch

# HDFS에 적재한 데이터를 꺼내서 적용합니다.

# 1. CSV 파일 로딩
df = pd.read_csv("/home/ssafy/hadoop_data/transactions.csv")  # ← 파일 경로

# 2. JSON 형태로 변환
records = df.to_dict(orient='records')  # ← 딕셔너리 변환 옵션

# 3. Elasticsearch 연결
es = Elasticsearch("http://localhost:9200")  # ← 호스트 URL

# 4. 데이터 업로드
for record in records:
    es.index(index="finance-transaction", document=record)  # ← 인덱스 이름
