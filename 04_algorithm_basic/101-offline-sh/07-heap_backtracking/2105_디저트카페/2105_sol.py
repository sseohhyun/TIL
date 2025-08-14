di = [1, 1, -1, -1]
dj = [1, -1, -1, 1]

def dfs(idx, r, c, cnt):
    global max_len

    # 방향 전환은 4번까지 가능 (0, 1, 2, 3)
    # 현재 방향으로 계속 이동
    ni, nj = r + di[idx], c + dj[idx]

    if 0 <= ni < N and 0 <= nj < N:
        if ni == start_i and nj == start_j and idx == 3:
            # 네 번째 방향으로 이동하여 출발점으로 돌아온 경우
            max_len = max(max_len, cnt + 1)
            return

        if visited[arr[ni][nj]] == 0:
            visited[arr[ni][nj]] = 1

            dfs(idx, ni, nj, cnt + 1)   # 같은 방향으로 계속 이동

            if idx < 3:
                dfs(idx + 1, ni, nj, cnt + 1)   # 방향 전환 (idx=3이면 방향 전환 불가)

            visited[arr[ni][nj]] = 0

import sys
sys.stdin = open("sample_input_2105.txt")

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    max_len = -1

    for i in range(N-2):
        for j in range(1, N-1):
            start_i, start_j = i, j  # 출발 지점 변수에 저장

            visited = [0] * 101
            visited[arr[i][j]] = 1 # 방문 기록

            dfs(0, start_i, start_j, 0)    # dfs 함수 실행 -> 해당 지점에서 max_len 업데이트

    print(f'#{tc} {max_len}')