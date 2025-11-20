# DataFrame 스키마(schema) 정의 및 데이터 타입 변환 실습 Skeleton 파일
# 아래의 빈칸(____)을 채운 후 PySpark 환경에서 실행하세요.
from pyspark.sql import SparkSession
from pyspark.sql.types import StructType, StructField, StringType, IntegerType
from pyspark.sql.functions import col
spark = SparkSession.builder.appName("StudentsData").getOrCreate()

# 1. 스키마 정의
schema = StructType([
    StructField("Name", StringType(), True),
    StructField("Major", StringType(), True),
    StructField("Age", StringType(), True) 
])

# 2. CSV 파일 로드 (header 없음)
df = spark.read.csv("/home/ssafy/101_offline_sh/day_12_e_Spark/data_engineering2_ws_2_2/data/students.csv", schema=schema)

# 3. 전체 데이터 출력
df.show()

# 4. Age 컬럼을 정수형으로 변환
df_casted = df.withColumn("Age", col("Age").cast(IntegerType()))

# 스키마 출력
df_casted.printSchema()

# 5. Age ≥ 25 학생 필터링 (이름, 전공 출력)
df_casted.filter(col("Age") >= 25).select("Name", "Major").show()

# 6. Major 기준 그룹화 후 전공별 학생 수 출력
df_casted.groupBy("Major").count().show()
