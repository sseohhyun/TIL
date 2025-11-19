# RDD 연산 최적화 실습 Skeleton 파일
# 아래의 빈칸(____)을 채운 후 PySpark 환경에서 실행하세요.
from pyspark import SparkContext
import time
sc = SparkContext("local", "RDDOptimization")

# 1. 파티션 개수 지정
num_partitions = 8

# 2. 1~1,000,000까지의 숫자 데이터를 포함하는 RDD 생성
rdd = sc.parallelize(range(1, 1000001), num_partitions)

# 3. 수행 시간 측정 함수 정의
def measure_time(fn):
    start = time.time()
    result = fn()
    end = time.time()
    return result, end - start

# 4. map+filter 연산
map_filter_result, t1 = measure_time(lambda: rdd.filter(lambda x: x % 2 == 0).map(lambda x: x * 2).collect())
print("[map + filter] 개수:", len(map_filter_result))
print("[map + filter] 샘플:", map_filter_result[:5])
print("[map + filter] 시간:", round(t1, 4), "초")

# 5. flatMap 연산
flatmap_result, t2 = measure_time(lambda: rdd.flatMap(lambda x: [x * 2] if x % 2 == 0 else []).collect())
print("[flatMap] 개수:", len(flatmap_result))
print("[flatMap] 샘플:", flatmap_result[:5])
print("[flatMap] 시간:", round(t2, 4), "초")

# 6. mapPartitions 연산
def transform_partition(iterator):
    return (x * 2 for x in iterator if x % 2 == 0)

mappart_result, t3 = measure_time(lambda: rdd.mapPartitions(transform_partition).collect())
print("[mapPartitions] 개수:", len(mappart_result))
print("[mapPartitions] 샘플:", mappart_result[:5])
print("[mapPartitions] 시간:", round(t3, 4), "초")