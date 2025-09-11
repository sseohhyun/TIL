def dfs(idx, arr, current_set, current_prod, visited):
    if len(current_set) == N:
        result.append(current_prod)
        return

    for j in range(N):
        if visited[j] == 0:
            visited[j] = 1
            current_set.append(arr[idx][j])
            prod = current_prod * arr[idx][j]

            if prod > current_prod:
                dfs(idx + 1, arr, current_set, prod, visited)
                visited[j] = 0
                current_set.pop()

import sys
sys.stdin = open("input_1865.txt", "r")

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    work = list(zip(*arr))

    visited = [0] * N
    result = []
    dfs(0, work, [], 1, visited)
    max_prod = max(result)

    print(f'#{tc} {round(max_prod/(100 ** (N - 1)), 6):.6f}')