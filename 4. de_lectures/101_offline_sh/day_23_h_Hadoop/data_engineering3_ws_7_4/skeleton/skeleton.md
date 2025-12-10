# YARN 작업 상태 확인 및 장애 상황 분석 실습 - Answer

## 1. NodeManager 장애 유도 및 로그 분석

### jps로 NodeManager PID 확인 후 종료
```bash
jps
kill -9 <NodeManager PID>
jps
```

### 장애 유도를 위한 작업 실행
```bash
hadoop jar $HADOOP_HOME/share/hadoop/mapreduce/hadoop-mapreduce-examples-*.jar pi 20 10000
```

## 2. NodeManager 재시작 후 상태 확인
```bash
start-yarn.sh
jps
```

### 실패 또는 대기 상태에서 로그 확인
```bash
yarn application -list -appStates RUNNING,ACCEPTED,FAILED
yarn logs -applicationId <application_id> # application_1756269082638_0001
```

## 3. 동일한 작업 재실행
```bash
hadoop jar $HADOOP_HOME/share/hadoop/mapreduce/hadoop-mapreduce-examples-*.jar pi 20 10000
```

### YARN 애플리케이션 상태 확인
```bash
yarn application -list -appStates ALL
```
