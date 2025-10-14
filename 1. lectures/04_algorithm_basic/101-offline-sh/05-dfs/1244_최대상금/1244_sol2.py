def dfs(card, cnt):
    global max_num

    if cnt == change:
        change_num = int("".join(card))
        if max_num < change_num:
            max_num = change_num
        return

    key = ("".join(card), cnt)
    if key in visited:
        return
    else:
        visited.add(key)

    for i in range(len(card)):
        for j in range(i+1, len(card)):
            card[i], card[j] = card[j], card[i] # 스왑
            dfs(card, cnt + 1)
            card[i], card[j] = card[j], card[i] # 원복

import sys
sys.stdin = open("input_1244.txt")

T = int(input())

for tc in range(1, T+1):
    lst = input().split()
    change = int(lst[1])     # change = 교환 횟수
    num_list = list(lst[0]) # card = 숫자, str형태의 리스트임 ['1', '2', '3']

    visited = set()
    max_num = 0
    dfs(num_list, 0)

    print(f'#{tc} {max_num}')
