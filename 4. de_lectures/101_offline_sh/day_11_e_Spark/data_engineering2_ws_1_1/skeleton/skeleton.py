# PySpark RDD 생성 및 변환 실습 Skeleton 파일
# 아래의 빈칸(____)을 채운 후 PySpark 환경에서 실행하세요.

from pyspark import SparkContext
sc = SparkContext("local", "RDDTransformations")

# 1. 1~5까지의 리스트 데이터를 RDD로 변환
numbers_rdd = sc.parallelize(range(1, 6))
print(numbers_rdd.collect())

# 2. 짝수 데이터만 필터링
num_filtered_rdd = numbers_rdd.filter(lambda x: x % 2 == 0)
print(num_filtered_rdd.collect())

# 3. 모든 숫자를 2배로 변환
doubled_rdd = numbers_rdd.map(lambda x: x * 2)
print(doubled_rdd.collect())

# 4. 외부 텍스트 파일 로드
text_rdd = sc.textFile("/home/ssafy/101_offline_sh/day_11_e_Spark/data_engineering2_ws_1_1/data/test.txt")
print(text_rdd.collect())

# 5. "Spark"가 포함된 문장 필터링
filtered_rdd = text_rdd.filter(lambda line: "Spark" in line)
print(filtered_rdd.collect())

# 6. 문장을 단어 단위로 분해
words_rdd = text_rdd.map(lambda line: line.split(" "))
print(words_rdd.collect())

# 7. Lazy Evaluation 실습
lazy_rdd = numbers_rdd.map(lambda x: x * 2).filter(lambda x: x > 5)

# 8. 생성 완료 후 잠시 대기
print("RDD 생성 완료. 아직 연산이 실행되지 않았습니다.")

# 9. 실제 연산 실행 (collect 호출)
print(lazy_rdd.collect())