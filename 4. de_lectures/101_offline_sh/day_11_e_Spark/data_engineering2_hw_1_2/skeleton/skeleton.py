#  RDD 샘플링 및 분할 실습 Skeleton 파일
# 아래의 빈칸(____)을 채운 후 PySpark 환경에서 실행하세요.
from pyspark import SparkContext
sc = SparkContext("local", "SamplingSplitApp")

# 1. 1~100까지 숫자 데이터를 RDD로 생성
numbers_rdd = sc.parallelize(range(1, 101))
print(f"원본 데이터 개수: {numbers_rdd.count()}")

# 2. sample() 비복원 방식으로 20% 샘플링
sample_without = numbers_rdd.sample(False, 0.2)
print("비복원 샘플링 결과:", sample_without.collect())

# sample() 복원 방식으로 20% 샘플링
sample_with = numbers_rdd.sample(True, 0.2)
print("복원 샘플링 결과:", sample_with.collect())

# takeSample() 비복원
take_sample_without = numbers_rdd.takeSample(False, 5)
print("takeSample 비복원:", take_sample_without)

# takeSample() 복원
take_sample_with = numbers_rdd.takeSample(True, 5)
print("takeSample 복원:", take_sample_with)

# 3. randomSplit()으로 훈련/테스트 분할
train_rdd, test_rdd = numbers_rdd.randomSplit([0.8, 0.2], seed=42)
print(f"훈련 데이터 개수: {train_rdd.count()}")
print(f"테스트 데이터 개수: {test_rdd.count()}")

# 4. 비교 분석
print(f"비복원 샘플 개수: {sample_without.count()}")
print(f"복원 샘플 개수: {sample_with.count()}")
