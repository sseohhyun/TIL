# 파티션 개수 확인 및 변경 실습 Skeleton 파일
# 아래의 빈칸(____)을 채운 후 PySpark 환경에서 실행하세요.

from pyspark.sql import SparkSession

# SparkSession 생성
spark = SparkSession.builder.appName("PartitionApp").getOrCreate()
sc = spark.sparkContext

# 1. 1~10까지의 숫자 데이터 생성
numbers = sc.parallelize(range(1, 11))

# 기본 파티션 개수 확인
default_partitions = numbers.getNumPartitions()
print(f"기본 파티션 개수: {default_partitions}")

# 파티션 개수를 1개로 변경
repartitioned_data = numbers.repartition(1)
print(f"1개로 변경된 파티션 개수: {repartitioned_data.getNumPartitions()}")

# 2. 기존 데이터 출력
numbers.foreach(lambda x: print(x))

# 파티션 1개로 변경된 데이터 출력
repartitioned_data.foreach(lambda x: print(x))