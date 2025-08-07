def dfs(idx, set_sum):
    global cnt
    if idx == N:
        return

    if set_sum == K:
        cnt += 1

    dfs(idx + 1, set_sum + lst[idx])
    dfs(idx + 1, set_sum)

import sys
sys.stdin = open("sample_input_2817.txt", "r")

T = int(input())
for tc in range(1, T+1):
    N, K = map(int, input().split())
    lst = list(map(int, input().split()))

    visited = [0] * N
    cnt = 0

    dfs(0, 0)

    print(f'#{tc} {cnt}')