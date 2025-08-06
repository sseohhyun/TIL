def dfs_row(r, c, arr, N, M):
    if r >= N or arr[r][c] == 0 :
        return 0
    arr[r][c] = 0 # 방문처리
    return 1 + dfs_row(r+1, c, arr, N, M)

def dfs_col(r, c, arr, N, M):
    if c >= M or arr[r][c] == 0 :
        return 0
    arr[r][c] = 0 # 방문처리
    return 1 + dfs_col(r, c+1, arr, N, M)

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    
    mx = 0

    for i in range(N):
        for j in range(M):
            if arr[i][j] == 1:

                # 1. 가로에 대해서만 구하기
                arr_copy = [lst[:] for lst in arr]
                length_row = dfs_row(i, j, arr_copy, N, M)
                if length_row >= 2:
                    mx = max(mx, length_row)
                
                # 2. 세로에 대해서만 구하기
                arr_copy = [lst[:] for lst in arr]
                length_col = dfs_col(i, j, arr_copy, N, M)
                if length_col >= 2:
                    mx = max(mx, length_col)

    print(f'#{tc} {mx}')
