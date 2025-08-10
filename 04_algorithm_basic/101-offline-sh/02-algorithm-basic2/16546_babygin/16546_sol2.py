from collections import deque

import sys
sys.stdin = open("input_16546.txt", "r")

T = int(input())
for tc in range(1, T+1):
    lst = list(map(int, input()))

    # 1. 정렬
    num_list = sorted(lst)

    # 2. triplet 제거
    cnt = [0] * 6   # 같은 숫자가 몇개인지 세기 위한 cnt 리스트 생성
    cnt[0] = 1

    for i in range(1, len(num_list)):
        if num_list[i] == num_list[i-1]:
            cnt[i] = cnt[i-1] + 1
        else:
            cnt[i] = 1

    ## cnt에 3이 있는 경우
    for i in range(6):
        if cnt[i] == 6:
            for idx in range(6):
                cnt[idx] = -1

        if cnt[i] == 3:
            for idx in range(i, i-3, -1):
                cnt[idx] = -1

    num_list = [num_list[i] for i in range(6) if cnt[i] != -1]
    # print(num_list)

    # 3. run 확인
    ## num_list가 3, 6인 경우에 따라 다르게 확인
    minus = [0] * len(num_list)
    for i in range(1, len(num_list)):
        minus[i] = num_list[i] - num_list[i-1]
    # print(minus)

    if max(minus, default=0) <= 1:
        num_list = []

    # 4. result 출력
    if len(num_list) == 0:
        result = "true"
    else:
        result = "false"

    print(f'#{tc} {result}')







