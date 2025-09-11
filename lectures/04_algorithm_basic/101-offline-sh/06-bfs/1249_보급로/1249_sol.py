
import sys
sys.stdin = open("input_1249.txt", "r")

from collections import deque

di = [ -1, 1, 0, 0]
dj = [0, 0, -1, 1]

def bfs(n, row, col):
    visited = [[-1] * n for _ in range(n)]
    visited[row][col] = arr[row][col]
    queue = deque()
    queue.append((row, col))

    while queue:
        row, col = queue.popleft()

        for d in range(4):
            ni, nj = row + di[d], col + dj[d]

            if 0 <= ni < n and 0 <= nj < n:
                cost = visited[row][col] + arr[ni][nj]

                if visited[ni][nj] == -1 or visited[ni][nj] > cost:
                    visited[ni][nj] = cost
                    queue.append((ni, nj))

    return visited[n - 1][n - 1]

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input())) for _ in range(N)]

    print(f'#{tc} {bfs(N, 0, 0)}')
