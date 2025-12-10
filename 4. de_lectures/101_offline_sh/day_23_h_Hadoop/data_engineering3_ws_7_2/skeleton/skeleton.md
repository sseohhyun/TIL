# Hadoop MapReduce (Split → Map → Shuffle & Sort → Reduce → 최종 출력) 실습

## 1. 로컬 파일을 HDFS에 업로드
```bash
hadoop fs -put input.txt /user/hadoop/input/
```

### 파일 목록 및 크기 확인
```bash
hadoop fs -ls /user/hadoop/input/
```

## 2. Split 정보 확인
```bash
hdfs fsck /user/hadoop/input/input.txt -files -blocks
```

## 3. WordCount 실행 (Mapper + Reducer)
```bash
hadoop jar /home/ssafy/hadoop/share/hadoop/mapreduce/hadoop-mapreduce-examples-3.3.5.jar \
    wordcount /user/hadoop/input/input.txt /user/hadoop/output/map_output
```

## 4. 결과 확인 (최종 출력)
```bash
hadoop fs -cat /user/hadoop/output/map_output/part-r-00000
```
