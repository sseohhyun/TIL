# 데이터 생성 및 변환 실습 Skeleton 파일
# 아래의 빈칸(____)을 채운 후 PySpark 환경에서 실행하세요.
from pyspark.sql import SparkSession

# SparkSession 생성
spark = SparkSession.builder.appName("WordLengthApp").getOrCreate()
sc = spark.sparkContext

# 1. 단어 길이 변환 및 필터링
# 문자열 데이터 생성("Spark", "Parallel", "Machine", "Learning", "Hadoop", "Kafka", "Big Data")
words = sc.parallelize(["Spark", "Parallel", "Machine", "Learning", "Hadoop", "Kafka", "Big Data"])

# 생성한 문자열 데이터 확인
print(words.collect())

# 각 단어의 길이 계산
word_lengths = words.map(lambda word: len(word))
print(word_lengths.collect())

# 6글자 이상 단어만 필터링
long_words = words.filter(lambda word: len(word) >= 6)
print(long_words.collect())

# 6글자 이상 단어 개수
long_words_count = long_words.count()
print(f"6글자 이상 단어 개수: {long_words_count}")

# 2. 짝수/홀수 필터링 및 합산 연산
# 1~20까지 숫자 데이터를 생성
numbers = sc.parallelize(range(1, 21))

# 짝수 필터링 후 데이터 확인
even = numbers.filter(lambda x: x % 2 == 0)
print("짝수:", even.collect())

# 홀수 필터링 후 데이터 확인
odd = numbers.filter(lambda x: x % 2 != 0)
print("홀수:", odd.collect())

# 3.소문자 변환 및 "is" 포함 문장 필터링
# 문자열 데이터 생성
sentences = sc.parallelize([
    "Spark is a powerful analytics engine",
    "Big Data is transforming industries",
    "Data Science is revolutionizing decision making",
    "Machine Learning and AI are the future"
])

# 모든 문장을 소문자로 변환하여 데이터 확인
lower = sentences.map(lambda line: line.lower())
print("소문자 변환:", lower.collect())

# "is"라는 단어가 포함된 문장만 필터링 후 데이터 확인
contains_is = sentences.filter(lambda line: "is" in line.lower())
print('"is" 포함 문장:', contains_is.collect())


