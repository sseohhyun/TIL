# Apache Spark RDD 저장 및 불러오기 실습 Skeleton 파일
# 아래의 빈칸(____)을 채운 후 Spark Shell에서 실행하세요.

from pyspark.sql import SparkSession

# 1. SparkSession 생성
spark = SparkSession.builder.appName("SaveLoadRDD").getOrCreate()
sc = spark.sparkContext

# 2. 숫자 데이터(1~10)를 RDD로 변환
numbers_rdd = sc.parallelize(range(1, 11))

# 데이터 확인
print(numbers_rdd.collect())

# 3. 저장 전 하나의 파티션으로 압축 (순서 보장)
numbers_rdd.coalesce(1).saveAsTextFile("output")

# 저장된 텍스트 파일을 불러와서 확인
loaded_text_rdd = sc.textFile("output")
print(loaded_text_rdd.collect())
