# 사용자 정의 WordCount 실행 실습

## 1. 입력 파일 업로드
```bash
hadoop fs -put shopping_transactions.csv /user/hadoop/input/
hadoop fs -ls /user/hadoop/input/
hadoop fs -cat /user/hadoop/input/shopping_transactions.csv | head -10
```

## 2. 사용자 정의 WordCount 실행 (Product 기준)

### mapper_answer.py
- CSV의 3번째 필드(Product)를 기준으로 `<product, 1>` 출력

### reducer_answer.py
- 동일한 key별로 개수 합산

```bash
hadoop jar /home/ssafy/hadoop/share/hadoop/tools/lib/hadoop-streaming-*.jar \
  -input /user/hadoop/input/shopping_transactions.csv \
  -output /user/hadoop/output/wordcount_custom \
  -mapper "python3 mapper_answer.py" \
  -reducer "python3 reducer_answer.py" \
  -file /home/ssafy/hadoop/input/mapper_answer.py \
  -file /home/ssafy/hadoop/input/reducer_answer.py
```
- 실제 사용 코드
```bash
hadoop jar /home/ssafy/hadoop/share/hadoop/tools/lib/hadoop-streaming-*.jar \
  -files mapper_skeleton.py,reducer_skeleton.py \
  -input /user/hadoop/input/shopping_transactions.csv \
  -output /user/hadoop/output/wordcount_custom \
  -mapper "python3 mapper_skeleton.py" \
  -reducer "python3 reducer_skeleton.py"
```

## 3. 결과 확인
```bash
hadoop fs -cat /user/hadoop/output/wordcount_custom/part-* | sort -k2 -nr | head -10
```

## 4. 차이 비교
따로 mapper와 reducer를 설정을 했다보니 결과 출력이 깔끔하게 단어로만 구성된 것을 확인할 수 있었습니다.