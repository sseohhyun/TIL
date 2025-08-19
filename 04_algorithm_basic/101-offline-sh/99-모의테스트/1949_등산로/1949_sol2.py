di, dj = [-1,1,0,0],[0,0,-1,1]

def dfs(r,c,length,used):
    global ans
    ans = max(ans,length)
    for d in range(4):
        nr, nc = r+di[d], c+dj[d]
        if 0<=nr<N and 0<=nc<N and not v[nr][nc]:
            if arr[nr][nc] < arr[r][c]:
                v[nr][nc] = 1
                dfs(nr,nc,length+1,used)
                v[nr][nc] = 0
            elif not used and arr[nr][nc]-K < arr[r][c]:
                h = arr[nr][nc]
                arr[nr][nc] = arr[r][c]-1   # 깎기
                v[nr][nc] = 1
                dfs(nr,nc,length+1,1)
                v[nr][nc] = 0
                arr[nr][nc] = h             # 복구

T = int(input())
for tc in range(1,T+1):
    N,K = map(int,input().split())
    arr = [list(map(int,input().split())) for _ in range(N)]
    top = max(map(max,arr))
    ans = 0
    v = [[0]*N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if arr[i][j] == top:     # 최고봉에서만 출발
                v[i][j] = 1
                dfs(i,j,1,0)
                v[i][j] = 0
    print(f"#{tc} {ans}")
