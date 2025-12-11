# HDFS 파일 업로드, 조회, 삭제, 목록 확인 실습

## 1. HDFS에 transactions.csv 내용 확인
```bash
hdfs dfs -cat /data/transactions.csv
# hdfs dfs -cat /user/local/hadoop_data/transactions.csv

```

## 2. HDFS에 note.txt 업로드
```bash
hdfs dfs -put note.txt /data/
# hdfs dfs -put note.txt /user/local/hadoop_data/
```

## 3. 업로드된 note.txt 내용 확인
```bash
hdfs dfs -cat /data/note.txt
# hdfs dfs -cat /user/local/hadoop_data/note.txt

```

## 4. note.txt 파일 삭제
```bash
hdfs dfs -rm /data/note.txt
# hdfs dfs -rm /user/local/hadoop_data/note.txt
```

## 5. /data 디렉토리 내 파일 목록 확인
```bash
hdfs dfs -ls /data/
# hdfs dfs -ls /user/local/hadoop_data/
```

### 출력 예시:
```
Found 1 items
-rw-r--r--   1 futura supergroup        453 2025-08-12 23:53 /data/transactions.csv
```
