# Hadoop WordCount MapReduce 실습 (금융 거래 데이터 기반)

## 1. HDFS에 파일 업로드
```bash
hadoop fs -put financial_transactions_sample.csv /user/hadoop/input/
```

## HDFS 업로드 된 파일 확인
```bash
hadoop fs -ls /user/hadoop/input/
```

## 2. Mapper 단독 실행 테스트
- CSV 파일 앞 10줄을 테스트 입력으로 사용하여, `mapper_count_skeleton.py`가 제대로 동작하는지 확인 (경로를 맞춰서 실행)
- Description 필드에서 `<description, 1>` 형식으로 출력되는지 확인
```bash
head -n 10 financial_transactions_sample.csv | python3 mapper_count_skeleton.py
```

## 3. Reducer 단독 실행 테스트
- Mapper 출력 예시를 직접 입력하여 `reducer_count_skeleton.py`가 Key별로 값을 잘 집계하는지 확인
```bash
echo -e "walmart grocery	1\nwalmart grocery	1\ngrocery	1\nsubscription	1\nsubscription	1" | sort | python3 reducer_count_skeleton.py
```

## 4. Hadoop Streaming 실행
```bash
hadoop jar /home/ssafy/hadoop/share/hadoop/tools/lib/hadoop-streaming-*.jar \
  -input /user/hadoop/input/financial_transactions_sample.csv \
  -output /user/hadoop/output/description_count \
  -mapper "python3 mapper_count_skeleton.py" \
  -reducer "python3 reducer_count_skeleton.py" \
  -file mapper_count_skeleton.py \
  -file reducer_count_skeleton.py
```

## 5. 결과 확인 (거래 내역 상위 10개 출력)
```bash
hdfs dfs -cat /user/hadoop/output/description_count/part-00000 | sort -k2 -nr | head -10
```
