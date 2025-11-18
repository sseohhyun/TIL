# 텍스트 데이터 로드 및 탐색 실습 Skeleton 파일
# 아래의 빈칸(____)을 채우세요

from pyspark.sql import SparkSession

# SparkSession 생성
spark = SparkSession.builder.appName("TextDataAnalysis").getOrCreate()
sc = spark.sparkContext

# 텍스트 파일 로드
text_data = sc.textFile("/home/ssafy/101_offline_sh/day_10_e_Spark/data_engineering1_hw_10_4/data/test_1.txt")

# 전체 텍스트 출력
print(text_data.collect())

# 줄 수 출력
print("전체 줄 개수:", text_data.count())

# 'data'가 포함된 문장 필터링
contains_data = text_data.filter(lambda line: "data" in line.lower())
print(text_data.collect())

# 포함된 줄 수 출력
print("전체 줄 개수:", text_data.count())

# 대문자로 변환
upper_case_data = text_data.map(lambda line: line.upper())
print(upper_case_data.collect())

# 소문자로 변환
lower_case_data = text_data.map(lambda line: line.lower())
print(lower_case_data.collect())

# 기본 파티션 개수 확인
print("기본 파티션 개수:", text_data.getNumPartitions())

# 파티션 4개로 재설정 후 확인
repartitioned_data = text_data.repartition(4)
print("변경된 파티션 개수:", repartitioned_data.getNumPartitions())
