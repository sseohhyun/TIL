# 파티션 개수 조정 및 성능 비교 실습 Answer 파일
# 아래의 빈칸(____)을 채운 후 PySpark 환경에서 실행하세요.

from pyspark import SparkContext
import time
sc = SparkContext("local", "PartitionPerformanceApp")

# 1. 1~100까지 숫자 데이터 포함 RDD 생성
num100 = sc.parallelize(range(1, 101))

# 2. 기본 파티션 개수 확인
print(f"기본 파티션 개수: {num100.getNumPartitions()}")

# 3. repartition(2n)
repartitioned_rdd = num100.repartition(num100.getNumPartitions()*2)
print(f"repartition(2n) 후 파티션 개수: {repartitioned_rdd.getNumPartitions()}")

# 4. coalesce(n/2)
coalesced_rdd = num100.coalesce(repartitioned_rdd.getNumPartitions()//2)
print(f"coalesce(n/2) 후 파티션 개수: {coalesced_rdd.getNumPartitions()}")

# 5. 병렬 처리 성능 비교 함수
def measure_time(rdd):
    start = time.time()
    rdd.count()
    end = time.time()
    return end - start

# 6. 파티션 개수별 실행 시간 측정
rdd1 = num100.repartition(1)
time1 = measure_time(rdd1)
print(f"파티션 1개 실행 시간: {time1:.6f} 초")

rdd4 = num100.repartition(4)
time4 = measure_time(rdd4)
print(f"파티션 4개 실행 시간: {time4:.6f} 초")

rdd8 = num100.repartition(8)
time8 = measure_time(rdd8)
print(f"파티션 8개 실행 시간: {time8:.6f} 초")