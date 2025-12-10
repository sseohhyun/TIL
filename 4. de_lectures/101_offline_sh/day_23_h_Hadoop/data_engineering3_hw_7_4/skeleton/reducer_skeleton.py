#!/usr/bin/env python3
import sys

# 초기화: 현재 집계 중인 Key와 그 누적 Count 값을 저장할 변수
current_word = None
current_count = 0

# 표준 입력에서 데이터 읽기 및 단어 빈도 집계
for line in sys.stdin:
    try:
        # 탭을 기준으로 key와 value로 분리
        word, count = line.strip().split('\t')
        count = int(count)

        # 동일한 단어의 빈도 합산
        if current_word == word:
            current_count += count
        else:
            if current_word:
                print(f"{current_word}\t{current_count}")
            # 새로운 Key로 초기화
            current_word = word
            current_count = count
    except:
        continue

# 마지막 단어 출력
if current_word:
    print(f"{current_word}\t{current_count}")
