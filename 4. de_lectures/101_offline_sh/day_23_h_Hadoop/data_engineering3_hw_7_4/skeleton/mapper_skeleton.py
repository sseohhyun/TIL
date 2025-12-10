#!/usr/bin/env python3
import sys
import re

for line in sys.stdin:
    try:
        # 라인 정리 및 CSV 분할
        fields = line.strip().replace('\r', '').split(',')

        # 헤더 행 스킵 및 최소 필드 개수 확인
        if len(fields) < 3 or fields[0].lower() == "transaction id":
            continue

        # 3번째 필드(Product) 추출 및 소문자 변환
        product = fields[2].strip().lower()

        # 알파벳 단어만 추출하여 <word, 1> 형태로 출력
        words = re.findall(r'\b[a-z]+\b', product)
        for word in words:
            print(f"{word}\t1")
    except:
        continue

