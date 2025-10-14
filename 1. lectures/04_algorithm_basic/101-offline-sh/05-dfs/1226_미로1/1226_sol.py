di = [-1, 1, 0, 0]
dj = [0, 0, -1, 1]

def dfs(start_r, start_c, end_r, end_c, visited):
    if start_r == end_r and start_c == end_c:
        return 1

    visited.add((start_r, start_c))

    for d in range(4):
        ni, nj = start_r + di[d], start_c + dj[d]
        if 0 <= ni < 16 and 0 <= nj < 16 and (ni,nj) not in visited and arr[ni][nj] != 1:
            if dfs(ni, nj, end_r, end_c, visited):
                return 1    # 찾으면 바로 종료
    return 0

import sys
sys.stdin = open("input_1226.txt")

for _ in range(1, 11):
    tc = int(input())
    arr = [list(map(int, input().strip())) for _ in range(16)]

    for i in range(16):
        for j in range(16):
            if arr[i][j] == 2:
                start_i, start_j = i, j
            elif arr[i][j] == 3:
                end_i, end_j = i, j
    visited = set()
    result = dfs(start_i, start_j, end_i, end_j, visited)

    print(f'#{tc} {result}')
