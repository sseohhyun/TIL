# 로컬 WSL Hadoop 데몬 실행 및 상태 확인 실습

## 1. Hadoop 데몬 실행

### HDFS 데몬(NameNode, DataNode) 실행
```bash
start-dfs.sh
```

### YARN 데몬(ResourceManager, NodeManager) 실행
```bash
start-yarn.sh
```

## 2. Hadoop 데몬 상태 확인
```bash
jps
```

### (정상 출력 예시)
```
NameNode
DataNode
ResourceManager
NodeManager
Jps
```

## 3. Hadoop 데몬 중지

### HDFS 데몬 중지
```bash
stop-dfs.sh
```

### YARN 데몬 중지
```bash
stop-yarn.sh
```

## 4. Hadoop 데몬 중지됐는지 확인
```bash
jps
```

### (정상 출력 예시: 관련 프로세스 미출력 시 정상 종료)
```
# 아무 관련 데몬 출력 없음
Jps
```
