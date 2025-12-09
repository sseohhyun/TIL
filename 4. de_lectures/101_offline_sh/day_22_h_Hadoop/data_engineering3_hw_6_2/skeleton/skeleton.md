# HDFS 실습

## 0. docker namenode 접속
```bash
docker exec -it namenode bash
```

## 1. 로컬 파일 생성
```bash
# "Hadoop HDFS 실습입니다."라는 문자열을 가진 파일 생성
echo "Hadoop HDFS 실습입니다." > test.txt
```

## 2. HDFS에 디렉토리 생성 및 업로드
```bash
# TODO: HDFS에 디렉토리 생성
hadoop fs -mkdir -p /user/hadoop/test/

# TODO: 로컬 파일을 HDFS로 업로드
hadoop fs -put test.txt /user/hadoop/test/

# TODO: 업로드된 파일 확인
hadoop fs -ls /user/hadoop/test/
```

## 3. 파일 내용 추가 후 확인
```bash
# TODO: 표준 입력으로부터 받은 내용을 기존 HDFS 파일에 추가
echo "두 번째 줄입니다." | hadoop fs -appendToFile - /user/hadoop/test/test.txt

# TODO: 파일 내용 확인
hadoop fs -cat /user/hadoop/test/test.txt
```

## 4. 존재하지 않는 파일 삭제 시도
```bash
# TODO: 존재하지 않는 파일 삭제 시도
echo "에러 테스트: 존재하지 않는 파일 삭제 시도"
hadoop fs -rm /user/hadoop/nonexistentfile.txt
# -> Error: No such file or directory
```

## 5. HDFS에 "test.txt" 파일 삭제
```bash
# TODO: 파일 삭제
hadoop fs -rm /user/hadoop/test/test.txt
```
