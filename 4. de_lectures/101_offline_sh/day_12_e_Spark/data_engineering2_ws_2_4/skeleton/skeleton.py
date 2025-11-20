# Spark SQL을 활용한 데이터 조회 실습 Skeleton 파일
# 아래의 빈칸(____)을 채운 후 PySpark 환경에서 실행하세요.
from pyspark.sql import SparkSession
spark = SparkSession.builder.appName("SparkSQLPractice").getOrCreate()

# 1. 데이터 준비
data = [
    ("Alice", "Data Science", 25, 4000),
    ("Bob", "Machine Learning", 30, 5000),
    ("Charlie", "Data Engineering", 35, 4500),
    ("David", "Data Science", 40, 5500),
    ("Eva", "Machine Learning", 28, 6000),
    ("Frank", "Data Engineering", 32, 4800)
]
columns = ["Name", "Department", "Age", "Salary"]

df = spark.createDataFrame(data, columns)

# 2. Temporary View 등록
df.createOrReplaceTempView("employee")

# SQL 쿼리 실행
# 3. 직원 전체 데이터 조회
spark.sql("SELECT * FROM employee").show()

# 4. 급여 5000 이상인 직원 조회
spark.sql("SELECT Name, Department FROM employee WHERE Salary >= 5000").show()

# 5. 나이 기준 내림차순 정렬
spark.sql("SELECT * FROM employee ORDER BY Age DESC").show()

# 6. 부서별 직원 수, 평균 급여
spark.sql("""
    SELECT Department,
           COUNT(*) AS Employee_Count,
           AVG(Salary) AS Avg_Salary
    FROM employee
    GROUP BY Department
""").show()
