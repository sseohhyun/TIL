#!/usr/bin/env python3
import sys

for line in sys.stdin:
    try:
        line = line.strip().replace('\r', '')
         # CSV 파일은 쉼표로 구분되므로 split(',') 사용
        columns = line.split(',')  
         # 최소 컬럼 수 확인 (Description 필드가 있는지) + 헤더 행("Transaction ID") 제외 처리
        if len(columns) < 3 or columns[0].lower() == "transaction id":
            continue
        # 3번째 컬럼인 Description 필드를 소문자로 변환 및 앞뒤 공백 제거
        description = columns[2].strip().lower()
        # 출력 형식: <description> \t 1
        # Hadoop에서는 각 Mapper 출력이 <Key> \t <Value> 형태여야 하며, 탭으로 구분됨
        print(f"{description}\t1")
    except:
        continue