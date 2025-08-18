def dfs(idx, height, current_sum):
    global min_minus

    if idx == N:
        if 0 <= current_sum - B <= min_minus:
            min_minus = current_sum - B
        return

    dfs(idx + 1, height, current_sum + height[idx])
    dfs(idx + 1, height, current_sum)


import sys
sys.stdin = open("input_1486.txt")

T = int(input())

for tc in range(1, T+1):
    N, B = map(int, input().split()) # N: 직원수, B: 최소 탑 높이
    height = list(map(int, input().split()))

    min_minus = float('inf')

    dfs(0, height, 0)
    print(f'#{tc} {min_minus}')