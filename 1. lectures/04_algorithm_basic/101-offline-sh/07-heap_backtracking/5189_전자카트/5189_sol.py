'''
    i, j의 값이 다른 조합의 최소 합을 구하면 되는 문제인 줄 앎
    -> 동칠이의 일분배와 같은 방식으로 생각하였음
    -> but,

'''

import sys
sys.stdin = open("sample_input_5189.txt", "r")

def dfs(idx, sum_battery, visited):
    global min_sum

    if sum(visited) == N-1:
        sum_battery += arr[idx][0]
        min_sum = min(min_sum, sum_battery)
        return

    if sum_battery >= min_sum:
        return

    for j in range(N):
        if arr[idx][j] != 0 and visited[j] == 0 and j != 0:
            visited[j] = 1
            dfs(j, sum_battery + arr[idx][j], visited)
            visited[j] = 0

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    visited = [0] * N
    min_sum = 100 * N

    dfs(0, 0, visited)
    print(f'#{tc} {min_sum}')