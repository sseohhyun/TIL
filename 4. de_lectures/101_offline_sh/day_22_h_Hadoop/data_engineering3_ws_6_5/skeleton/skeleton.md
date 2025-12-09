# 입력 데이터 준비 및 분할 구조 이해

## 1. HDFS에 파일 업로드
```bash
hadoop fs -put input_large.txt /user/hadoop/input/
```

## 2. 업로드 확인
```bash
hadoop fs -ls /user/hadoop/input/
```

## 3. 파일 블록 분할 구조 확인
```bash
hdfs fsck /user/hadoop/input/input_large.txt -files -blocks
```

- 파일 크기: 102,842,857 bytes (~98MB)
- HDFS replication factor: 1 (복제본 1개 → 싱글 노드 환경이라 정상)
- 블록 개수: 1 block
- 파일 자체 상태: OK