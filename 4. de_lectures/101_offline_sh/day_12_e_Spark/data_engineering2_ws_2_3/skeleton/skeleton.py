# DataFrame을 활용한 데이터 집계 및 변형 실습 Skeleton 파일
# 아래의 빈칸(____)을 채운 후 PySpark 환경에서 실행하세요.
from pyspark.sql import SparkSession
from pyspark.sql.functions import avg, sum, max, min, count, col, when
spark = SparkSession.builder.appName("DataFrameAggregation").getOrCreate()

# 1. 데이터 생성
data = [
    ("Alice", "Data Science", 25, 4000),
    ("Bob", "Machine Learning", 30, 5000),
    ("Charlie", "Data Engineering", 35, 4500),
    ("David", "Data Science", 40, 5500),
    ("Eva", "Machine Learning", 28, 6000),
    ("Frank", "Data Engineering", 32, 4800)
]
columns = ["Name", "Department", "Age", "Salary"]

# DataFrame 생성
df = spark.createDataFrame(data, columns)

# 2. 부서별 집계 (평균 나이, 평균 급여, 급여 합계, 최고 급여, 최저 급여, 직원 수)
df.groupBy("Department").agg(
    avg("Age").alias("Avg_Age"),
    avg("Salary").alias("Avg_Salary"),
    sum("Salary").alias("Total_Salary"),
    max("Salary").alias("Max_Salary"),
    min("Salary").alias("Min_Salary"),
    count("*").alias("Employee_Count")
).show()

# 3. 급여가 5000 이상인 직원 필터 후 부서별 평균 나이
df.filter(df['Salary'] >= 5000).groupBy("Department").agg(avg("Age")).show()

# 4. 연봉을 월급으로 변환하여 새로운 컬럼 추가
df_monthly = df.withColumn("Monthly_Salary", col("Salary") / 12)
df_monthly.show()

# 5. Department 값이 "Data Science" → "AI Research"로 변경
df_changed = df_monthly.withColumn(
    "Department",
    when(col("Department") == "Data Science", "AI Research").otherwise(col("Department"))
)
df_changed.show()

# 6. 최종 변형된 데이터를 기준으로 부서별 직원 수 및 평균 월급 출력
df_changed.groupBy("Department").agg(
    count("*").alias("Num_Employees"),
    avg("Monthly_Salary").alias("Avg_Monthly_Salary")
).show()
