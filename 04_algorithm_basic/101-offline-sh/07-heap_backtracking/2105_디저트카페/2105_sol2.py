import sys
sys.stdin = open("sample_input_2105.txt")

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    for i in range(N):
        for j in range(N):
            start_i, start_j = i, j
            visited = [0] * (N+1)
            visited[arr[start_i][start_j]] = 1
            dfs(0, start_i, start_j, )