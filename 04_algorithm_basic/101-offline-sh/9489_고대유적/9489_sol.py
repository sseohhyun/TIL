import sys
sys.stdin = open("input_9489.txt", "r")

# 탐색 함수
def dfs(r, c):
    if r+1 < N :
        if arr[r + 1][c] == 1:
            remains.append(1)
            dfs(r + 1,c)

    if c + 1 < M:
        if arr[r][c+1] == 1:
            remains.append(1)
            dfs(r, c+1)

    return remains

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]

    result = [] # remain을 쌓기 위한 리스트 선언

    for i in range(N):
        remains = []    # 1(유적)을 쌓기 위해 변수 선언(한줄을 쌓기 위함)
        for j in range(M):
            if arr[i][j] == 1:
                remains = [1]
                arr[i][j] = 0
                result.append(len(dfs(i, j)))

    print(f"#{tc} {max(result)}")


