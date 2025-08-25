def tile(n):
    dp = [0] * (n+1)
    dp[1], dp[2], dp[3] = 1, 3, 6

    for i in range(4, n+1):
        dp[i] = (dp[i-1]) + (2 * dp[i-2]) + (dp[i-3])

    return dp[n]

T = int(input())

for tc in range(1, T+1):
    N = int(input())

    print(f'#{tc} {tile(N)}')
