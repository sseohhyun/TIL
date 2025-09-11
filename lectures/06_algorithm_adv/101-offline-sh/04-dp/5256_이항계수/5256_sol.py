def binom(n, k):
    dp = [[0] * (k+1) for _ in range(n+1)]

    for i in range(n+1):
        for j in range(min(i, k) + 1):
            if j == 0 or i == j:
                dp[i][j] = 1
            else:
                dp[i][j] = dp[i-1][j-1] + dp[i-1][j]

    return dp[n][k]

T = int(input())
for tc in range(1, T+1):
    n, k, _ = map(int, input().split())

    print(f'#{tc} {binom(n, k)}')