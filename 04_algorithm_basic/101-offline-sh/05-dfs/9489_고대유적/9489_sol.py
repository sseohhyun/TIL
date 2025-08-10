import sys
sys.stdin = open("input_9489.txt", "r")

# 탐색 함수
def dfs(r, c, arr, N, M):
    count = 1   # 현재 위치를 카운트
    arr[r][c] = 0 # 방문처리

    # 아래쪽 탐색
    if r+1 < N and arr[r + 1][c] == 1:
        count += dfs(r+1, c, arr, N, M)
    # 위쪽 탐색
    if c + 1 < M and arr[r][c+1] == 1:
        count += dfs(r, c+1, arr, N, M)

    return count

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    result = []

    for i in range(N):
        for j in range(M):
            if arr[i][j] == 1:  # 유적 발견
                remains = dfs(i, j, arr, N, M)
                result.append(remains)

    print(f"#{tc} {max(result) if result else 0}")


