# HDFS를 활용한 금융 데이터 CSV 업로드 및 다운로드 실습

## 1. HDFS 디렉토리 생성
```bash
hdfs dfs -mkdir -p /data
```

## 2. 로컬 CSV 파일 업로드 (transactions.csv)
```bash
hdfs dfs -put transactions.csv /data/
```

## 3. HDFS에서 로컬로 파일 다운로드
```bash
hdfs dfs -get /data/transactions.csv ~/ssafy_hadoop/chapter3/backup/
```

## 4. 다운로드한 파일 내용 확인
```bash
cat ~/ssafy_hadoop/chapter3/backup/transactions.csv
```

