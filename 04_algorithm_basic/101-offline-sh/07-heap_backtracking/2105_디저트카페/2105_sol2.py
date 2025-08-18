import sys
sys.stdin = open("sample_input_2105.txt")

di = [1, 1, -1 , -1]
dj = [1, -1, -1, 1]

def dfs(idx, row, col, cnt):
    global max_len

    ni, nj = row + di[idx], col + dj[idx]

    if 0 <= ni < N and 0 <= nj < N: # 범위 안에 있다면
        # 종료 조건 명시 : 방향리스트의 끝에 도달 & 처음 시작 값이라면
        if idx == 3 and (start_i, start_j) == (ni, nj):
            max_len = max(max_len, cnt+1)
            return

        # 다음 좌표를 직진을 하거나(idx 유지), 방향을 바꾸거나(idx+1)
        if visited[arr[ni][nj]] == 0:
            visited[arr[ni][nj]] = 1
            # 직진
            dfs(idx, ni, nj, cnt+1)
            # 방향전환
            if idx < 3:
                dfs(idx+1, ni, nj, cnt+1)
            visited[arr[ni][nj]] = 0     # 백트래킹 :

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    max_len = -1

    for i in range(N-2):
        for j in range(1, N-1):
            start_i, start_j = i, j
            visited = [0] * 101
            visited[arr[start_i][start_j]] = 1
            dfs(0, start_i, start_j, 0)
            visited[arr[start_i][start_j]] = 0

    print(f'{tc} {max_len}')