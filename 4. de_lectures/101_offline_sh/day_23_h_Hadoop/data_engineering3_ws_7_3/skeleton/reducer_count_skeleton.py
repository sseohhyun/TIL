#!/usr/bin/env python3
import sys

# 초기화: 현재 집계 중인 Key와 그 누적 Count 값을 저장할 변수
current_key = None
current_count = 0

for line in sys.stdin:
    try:
        # 탭을 기준으로 key와 value로 분리
        key, value = line.strip().split('\t')
        value = int(value)

        if key == current_key:
            # 이전 Key와 동일하다면 누적 합산
            current_count += value
        else:
            if current_key is not None:
                # 새로운 Key가 등장한 경우, 이전 Key의 누적값 출력
                print(f"{current_key}\t{current_count}")
            # 새로운 Key로 초기화
            current_key = key
            current_count = value
    except:
        continue

# 마지막 키 출력
if current_key:
    print(f"{current_key}\t{current_count}")