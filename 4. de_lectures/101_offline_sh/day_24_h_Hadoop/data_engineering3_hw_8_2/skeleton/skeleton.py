import time
import os
import shutil
from pyspark.sql import SparkSession

'''
해당 실습을 위해서 HDFS는 로컬에서 띄워야 합니다.
docker 컨테이너 기반 Hadoop을 실행하는 경우 네트워크 이슈가 발생할 수 있습니다.
'''

# SparkSession 생성
spark = SparkSession.builder \
    .appName("Read HDFS CSV") \
    .master("local[*]") \
    .getOrCreate()

# HDFS의 CSV 파일 읽기
# HDFS에 파일이 올라가 있어야 함.
# hdfs dfs -mkdir -p /user/local/hadoop_data
# hdfs dfs -put /data/transactions.csv /user/local/hadoop_data/

df = spark.read.option("header", "true").csv("hdfs://localhost:9000/user/local/hadoop_data/transactions.csv")

# 데이터 출력 (검증용)
df.show()

# 필요한 컬럼만 선택
df_selected = df.select("transaction_date", "amount")

# 로컬 디스크에 CSV로 저장 (Spark는 디렉토리 + part 파일 형태로 저장)
output_dir = "/home/ssafy/hadoop_data/transactions"
final_file = "/home/ssafy/hadoop_data/transactions.csv"

df_selected.write.mode("overwrite").option("header", "true").csv(f"file://{output_dir}")

# 저장 완료될 때까지 대기
time.sleep(2)

# part 파일을 찾아 단일 파일로 rename
files = os.listdir(output_dir)
for f in files:
    if f.startswith("part-") and f.endswith(".csv"):
        shutil.move(os.path.join(output_dir, f), final_file)

# 디렉토리 정리 (선택 사항)
for f in os.listdir(output_dir):
    path = os.path.join(output_dir, f)
    if os.path.isfile(path):
        os.remove(path)
os.rmdir(output_dir)

print(f"저장 완료: {final_file}")
