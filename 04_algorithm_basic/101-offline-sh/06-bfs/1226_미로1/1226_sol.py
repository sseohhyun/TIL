di = [-1, 1, 0, 0]
dj = [0, 0, -1, 1]

from collections import deque

def bfs(row, col, row_end, col_end, arr):
    visited = [[-1] * 16 for _ in range(16)]
    queue = deque()
    queue.append((row, col))
    visited[row][col] = 1   # visited 방문처리

    while queue:
        row, col = queue.popleft()
        if row == row_end and col == col_end:
            return 1

        for d in range(4):
            ni, nj = row + di[d], col + dj[d]
            if 0 <= ni < 16 and 0 <= nj < 16 and visited[ni][nj] == -1 and arr[ni][nj] != 1:
                visited[ni][nj] = 1
                queue.append((ni, nj))
    return 0s

import sys
sys.stdin = open("input_1226.txt", "r")

for tc in range(1, 11):
    T = int(input())
    miro = [list(map(int, input())) for _ in range(16)]

    start_i, start_j, end_i, end_j = 0, 0, 0, 0
    for i in range(16):
        for j in range(16):
            if miro[i][j] == 2:
                start_i, start_j = i, j
            if miro[i][j] == 3:
                end_i, end_j = i, j

    ans = bfs(start_i, start_j, end_i, end_j, miro)

    print(f'#{tc} {ans}')