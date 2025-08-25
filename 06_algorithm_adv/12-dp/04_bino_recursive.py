def bino(n, k):
    if k == 0 or k == n:
        return 1
    return bino(n-1, k) + bino(n-1, k-1)

n = 1000
k = 2
print(bino(n, k))  # 출력: 10
