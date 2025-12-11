# HDFS 파일 정보 확인 실습

## 1. finance.csv 파일 내용 확인
```bash
hdfs dfs -mkdir -p /data
hdfs dfs -put finance.csv /data/
hdfs dfs -cat /data/finance.csv
```

## 2. finance.csv 파일 메타 정보 확인

### (1) 블록 수, 파일 수, 용량 확인
```bash
hdfs dfs -count /data/finance.csv
```

### 출력 예시
```
0          1           453 /data/finance.csv
```

### (2) 파일 용량 확인 (요약)
```bash
hdfs dfs -du -s /data/finance.csv
```

### 출력 예시
```
453  453  /data/finance.csv
```

### (3) 파일 상태 확인 (최종 수정 시간 등)
```bash
hdfs dfs -stat /data/finance.csv
```

### 출력 예시
```
2025-05-12 14:53:32
```
