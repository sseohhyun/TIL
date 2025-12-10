# Hadoop 클러스터 구조 및 상태 확인 실습

## 1. 클러스터 주요 컴포넌트 상태 확인

### NameNode, DataNode, ResourceManager, NodeManager 출력 확인
```bash
jps
```

### NameNode 입장에서 클러스터의 HDFS 상태 확인
```bash
hdfs dfsadmin -report
```

### ResourceManager 및 NodeManager 상태 확인
```bash
yarn node -list
```

---

## 2. HDFS에서 파일 업로드 및 복제 상태 확인

### 파일 업로드
```bash
hadoop fs -put input.txt /user/hadoop/input/
```

### 업로드된 파일 확인
```bash
hadoop fs -cat /user/hadoop/input/input.txt
```

### 업로드한 파일의 블록 배치 및 복제 정보 확인
```bash
hdfs fsck /user/hadoop/input/input.txt -files -blocks -locations
```

---

## 3. YARN 기반 MapReduce 실행 (내장 예제: WordCount)
```bash
hadoop jar /home/ssafy/hadoop/share/hadoop/mapreduce/hadoop-mapreduce-examples-*.jar \
  wordcount /user/hadoop/input/input.txt /user/hadoop/output/wordcount_result
```

### 실행 완료된 YARN 작업 목록 확인
```bash
yarn application -list -appStates ALL
```
