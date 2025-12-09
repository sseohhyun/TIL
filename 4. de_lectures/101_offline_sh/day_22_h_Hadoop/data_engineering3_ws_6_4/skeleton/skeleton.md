# Hadoop HDFS 기본 명령어 실습
- start-dfs.sh, start-yarn.sh 실행 정상 상태에서

## 1. HDFS 디렉터리 생성
```bash
hadoop fs -mkdir -p /user/hadoop/input/
```

## 2. 파일(test.txt)을 HDFS 경로로 업로드 (데이터가 있는 위치에서)
```bash
hadoop fs -put test.txt /user/hadoop/input/
```

## 3. 업로드된 HDFS 파일(test.txt)의 내용 확인
```bash
hadoop fs -cat /user/hadoop/input/test.txt
```

## 4. HDFS 파일을 로컬 /home/ssafy/hadoop/test 경로로 다운로드
```bash
# 로컬 /home/ssafy/hadoop/경로에 test 폴더 생성
mkdir -p /home/ssafy/hadoop/test

# 파일 다운로드
hadoop fs -get /user/hadoop/input/test.txt /home/ssafy/hadoop/test
```

## 5. 로컬에 다운로드 된 (“test.txt”) 파일이 있는지 목록 확인
```bash
ls /home/ssafy/hadoop/test
```

## 6. HDFS 경로 내 파일 및 디렉터리 목록 확인
```bash
hadoop fs -ls /user/hadoop/input
```

## 7. HDFS에서 test.txt 파일 삭제
```bash
hadoop fs -rm /user/hadoop/input/test.txt
```

## 8. HDFS 경로 내 test.txt 파일이 삭제됐는지 디렉터리 목록 확인
```bash
hadoop fs -ls /user/hadoop/input
```
