# 상 하 좌 우 방향리스트 설정
di = [-1, 1, 0, 0]
dj = [0, 0, -1, 1]

# 방향 탐색을 위한 dfs 함수 설정
def dfs(row, col, arr, visited, cnt):
    global max_len
    # 현위치의 값을 visited 스택에 쌓음
    visited.append(arr[row][col])

    ## 종료 조건 ##
    # visited(이동한 지점이) len >= 2, 나보다 값이 큰데,
    #   cnt가 1보다 큰 경우
    #   cnt가 0이긴 하나 K(공사 가능 최대 깊이)만큼 깎아도 값이 큰 경우
    if len(visited) >= 2 and visited[-1] >= visited[-2]:
        if visited[-1] - K >= visited[-2]:
            return
        if cnt > 1:
            max_len = max(max_len, len(visited))
            return

    # 4방향을 확인하기
    for i in range(4):
        ni, nj = row + di[i], col + dj[i]

        # 다움 이동 위치의 값이 범위 안에 있고
        if 0 <= ni < N and 0 <= nj < N:
            if arr[row][col] > arr[ni][nj]:
                dfs(ni, nj, arr, visited, cnt)
            if arr[row][col] <= arr[ni][nj] and arr[row][col] > arr[ni][nj] - K and cnt == 0:
                arr[ni][nj] = arr[row][col] - 1 # K만큼 다 뺄 필요 없고 1만큼만 더 작으면 되니까 -1
                dfs(ni, nj, arr, visited, cnt + 1)

import sys
sys.stdin = open("sample_input_1949.txt")

T = int(input())
for tc in range(1, T+1):
    N, K = list(map(int, input().split()))
    arr = [list(map(int, input().split())) for _ in range(N)]

    max_height = 0
    max_height_idx = []

    # 최대값을 찾음
    for lst in arr:
        max_height = max([max_height] + lst)
    # 최대값에 해당하는 인덱스를 찾아서 리스트에 삽입
    for i in range(N):
        for j in range(N):
            if max_height == arr[i][j]:
                max_height_idx.append((i, j))
    # print(f'#{tc} max_height : {max_height}, max_height_idx : {max_height_idx}')
    # "#1 max_height : 9, max_height_idx : [(0, 0), (2, 3), (2, 4)]"

    max_len = 0
    for i_idx, j_idx in max_height_idx:
        dfs(i_idx, j_idx, arr, [], 0)

    print(f'#{tc} {max_len}')