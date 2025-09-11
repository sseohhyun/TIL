di = [-1, 1, 0, 0]
dj = [0, 0, -1, 1]

def dfs(row, col, current_cost, visited):
    # 도착점 도달
    if row == N - 1 and col == N - 1:   # 끝점에 도달
        result.append(current_cost + arr[row][col])
        return

    # 4방향 탐색
    for d in range(4):
        ni, nj = row + di[d], col + dj[d]

        if 0 <= ni < N and 0 <= nj < N and (ni, nj) not in visited: # 범위 안에 있고, 방문x
            visited.add((ni, nj))
            dfs(ni, nj, current_cost + arr[row][col], visited)
            visited.remove((ni, nj))

import sys
sys.stdin = open("input_1249.txt", "r")

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input())) for _ in range(N)]

    result = []
    visited = {(0, 0)}
    dfs(0, 0, 0, visited)

    min_cost = min(result)
    print(f'#{tc} {min_cost}')