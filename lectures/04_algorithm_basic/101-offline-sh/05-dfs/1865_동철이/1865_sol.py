'''
4
71 51 30 1
29 63 32 93
84 94 33 21
56 40 80 31
'''

def dfs(idx, arr, current_prod, visited):
    global max_prod

    if idx == N:
        max_prod = max(max_prod, current_prod)
        return

    # 가지치기 추가
    if current_prod <= max_prod:
        return

    for j in range(N):
        if visited[j] == 0:
            visited[j] = 1
            dfs(idx + 1, arr, current_prod * arr[idx][j], visited)
            visited[j] = 0


import sys
sys.stdin = open("input_1865.txt", "r")

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    work = list(zip(*arr))  # 행열 바꾸기
    work = [[x / 100 for x in row] for row in work] # 퍼센트로 바꾸기

    visited = [0] * N
    max_prod = 0
    dfs(0, work, 1, visited)

    print(f'#{tc} {max_prod * 100:.6f}')