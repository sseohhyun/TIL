from collections import deque

import sys
sys.stdin = open("input_16546.txt", "r")

def babygin(num_list):
    global result

    # 1. triplet
    for num in num_list:
        if num_list.count(num) >= 3:
            for _ in range(3):
                num_list.remove(num)
    if len(num_list) == 0:
        result = "true"
        return

    # 2.  run
    for _ in range(len(num_list)//3):
        min_num = min(num_list)
        if min_num + 1 in num_list and min_num + 2 in num_list:
            num_list.remove(min_num)
            num_list.remove(min_num+1)
            num_list.remove(min_num+2)
    if len(num_list) == 0:
        result = "true"
        return

T = int(input())
for tc in range(1, T+1):
    lst = list(map(int, input()))
    result = "false"

    card = sorted(lst)
    babygin(card)
    print(f'#{tc} {result}')


'''
    # 3. run 확인
    ## num_list가 3, 6인 경우에 따라 다르게 확인
    minus = [0] * len(num_list)
    for i in range(1, len(num_list)):
        minus[i] = num_list[i] - num_list[i-1]
    # print(minus)

    if max(minus, default=0) <= 1:
        num_list = []

    
    if len(num_list) == 0:
        result = "true"
    else:
        result = "false"

    print(f'#{tc} {result}')
'''






