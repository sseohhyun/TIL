# 외부 텍스트 파일 로드 및 데이터 탐색 실습 Skeleton 파일
# 아래의 빈칸(____)을 채운 후 PySpark 환경에서 실행하세요.

from pyspark.sql import SparkSession

# SparkSession 생성
spark = SparkSession.builder.appName("LoadExternalFileApp").getOrCreate()
sc = spark.sparkContext

# 1. 텍스트 파일 로드
text_data = sc.textFile("/home/ssafy/101_offline_sh/day_10_e_Spark/data_engineering1_ws_10_3/data/test.txt")

# 2. 전체 데이터 확인
print(text_data.collect())

# 3. 전체 줄 개수 확인
print(text_data.count())

# 4. 모든 문장을 대문자로 변환 후 출력
upper_case_data = text_data.map(lambda line: line.upper())
print(upper_case_data.collect())

# 5. 모든 문장을 소문자로 변환 후 출력
lower_case_data = text_data.map(lambda line: line.lower())
print(lower_case_data.collect())

# 6. 각 문장의 길이 출력
line_lengths = text_data.map(lambda line: len(line))
print(line_lengths.collect())