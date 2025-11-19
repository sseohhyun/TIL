# 고객 이탈 데이터 분석 실습 Skeleton 파일
# 아래의 빈칸(____)을 채운 후 PySpark 환경에서 실행하세요.

from pyspark import SparkContext
sc = SparkContext("local", "PartitionPerformanceApp")

# 1. CSV 파일 로드 및 데이터 확인
# CSV 파일을 RDD로 변환
raw_rdd = sc.textFile("/home/ssafy/101_offline_sh/day_11_e_Spark/data_engineering2_ws_1_5/data/Customer-Churn-Records.csv")

# 헤더 
header = raw_rdd.first()
data_rdd = raw_rdd.filter(lambda line: line != header)

# 헤더 제거 후 상위 5개 데이터
print("\n[헤더 제거 후 상위 5개 데이터]")
for row in data_rdd.take(5):
    print(row)

# 3. 신용 점수(CreditScore)별 고객 이탈률 분석
def parse_credit(line):
    cols = line.split(",")
    if cols[3].strip() == "" or cols[13].strip() == "":
        return None
    credit_score = (int(cols[3]) // 100) * 100
    exited = int(cols[13])
    return (f"{credit_score}점대", exited)

credit_rdd = data_rdd.map(parse_credit).filter(lambda x: x is not None)
credit_avg_rdd = credit_rdd.groupByKey().mapValues(lambda vals: sum(vals)/len(vals)*100)

print("\n[신용 점수대별 평균 이탈률]")
for item in credit_avg_rdd.collect():
    print(item)

# 4. 연령(Age)대별 고객 이탈률 분석
def parse_age(line):
    cols = line.split(",")
    if cols[6].strip() == "" or cols[13].strip() == "":
        return None
    age_group = (int(cols[6]) // 10) * 10
    exited = int(cols[13])
    return (f"{age_group}대", exited)

age_rdd = data_rdd.map(parse_age).filter(lambda x: x is not None)
age_avg_rdd = age_rdd.groupByKey().mapValues(lambda vals: sum(vals)/len(vals)*100)

print("\n[연령대별 평균 이탈률]")
for item in age_avg_rdd.collect():
    print(item)

# 5. 카드 유형(Card Type)별 고객 이탈률 분석
def parse_card(line):
    cols = line.split(",")
    if cols[16].strip() == "" or cols[13].strip() == "":
        return None
    card_type = cols[16].strip()
    exited = int(cols[13])
    return (card_type, exited)

card_rdd = data_rdd.map(parse_card).filter(lambda x: x is not None)
card_avg_rdd = card_rdd.groupByKey().mapValues(lambda vals: sum(vals)/len(vals)*100)

print("\n[카드 유형별 평균 이탈률]")
for item in card_avg_rdd.collect():
    print(item)
