# 내장 WordCount 실행 실습

## 1. 입력 파일 업로드
```bash
hadoop fs -put shopping_transactions.csv /user/hadoop/input/
hadoop fs -ls /user/hadoop/input/
hadoop fs -cat /user/hadoop/input/shopping_transactions.csv | head -10
```

## 2. 내장 WordCount 실행
```bash
hadoop jar /home/ssafy/hadoop/share/hadoop/mapreduce/hadoop-mapreduce-examples-*.jar \
  wordcount /user/hadoop/input/shopping_transactions.csv /user/hadoop/output/wordcount_builtin
```

## 3. 결과 확인
```bash
hadoop fs -cat /user/hadoop/output/wordcount_builtin/part-* | sort -k2 -nr | head -10
```

## 4. 분석의 한계점
WordCount는 이게 날짜인지, 상품명인지, 가격인지 구분을 하지 않고 그냥 모든 글자를 다 섞어서 카운트를 하기 때문에 결과에 시간이 출력되었습니다.
WordCount는 띄어쓰기 단위로 자르기 때문에 쉼표가 포함된 Lamp,Home이 결과로 출력되었습니다.
