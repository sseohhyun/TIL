# 데이터 유형 변환 및 형식 변경 실습 Skeleton 파일
# 아래의 빈칸(____)을 채운 후 PySpark 환경에서 실행하세요.
from pyspark.sql import SparkSession
from pyspark.sql.functions import col, to_date
from pyspark.sql.types import IntegerType
spark = SparkSession.builder.appName("CastAndDateFormat").getOrCreate()

# 1. 데이터 준비
data = [
    ("Alice", "25-12-2023", "3500"),
    ("Bob", "10-01-2024", "4500"),
    ("Charlie", "05-02-2024", "5000"),
    ("David", "15-03-2024", "6000")
]

columns = ["Customer", "OrderDate", "Price"]

# DataFrame 생성
df = spark.createDataFrame(data, columns)

# 2. 원본 스키마 출력
print("원본 스키마:")
df.printSchema()

# 3. Price 컬럼을 정수형으로 변환하여 새 컬럼 "Price_Int" 추가
df = df.withColumn("Price_Int", col("Price").cast(IntegerType()))

# 4. OrderDate 문자열을 날짜(Date) 형식으로 변환하여 새 컬럼 추가
df = df.withColumn("Order_Date_Format", to_date(col("OrderDate"), "dd-MM-yyyy"))
  
# 5. 변경된 스키마 출력
print("변환된 스키마:")
df.printSchema()

# 7. 최종 결과 출력
df.show(truncate=False)