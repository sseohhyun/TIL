import sys
sys.stdin = open("sample_input_5189.txt", "r")

def dfs(idx, sum_battery, visited):
    global max_sum

    if idx == N-1:
        max_sum = max(max_sum, sum_battery)
        return

    if sum_battery < max_sum:
        return

    for j in range(N):
        if j != idx and visited[idx] == 0:
            visited[idx] = 1
            dfs(idx + 1, sum_battery + arr_t[idx][j], visited)
            visited[idx] = 0

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    arr_t = list(zip(*arr))

    visited = [[0] * N]
    max_sum = 0

    dfs(0, 0, visited)
    print(f'#{tc} {max_sum}')