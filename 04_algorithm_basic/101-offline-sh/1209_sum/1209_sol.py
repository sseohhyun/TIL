for _ in range(10):
    tc = int(input())
    arr = [list(map(int, input().split())) for _ in range(100)]

    # 각 행마다 가진 값들을 더함
    # 각 열마다 가진 값들을 더함
    # 대각선 값들을 더함
    # max 금지

    row_sum = []
    column_sum = []

    for i in range(100):
        temp1, temp2 = 0, 0
        for j in range(100):
            temp1 += arr[i][j]
            temp2 += arr[j][i]
        row_sum.append(temp1)
        column_sum.append(temp2)

    temp3, temp4 = 0, 0
    cross_sum = []
    for i in range(100):
        temp3 += arr[i][i]
        temp4 += arr[i][99 - i]
    cross_sum.append(temp3)
    cross_sum.append(temp4)

    mx = 0
    for hap in (row_sum + column_sum + cross_sum):
        if hap >= mx:
            mx = hap

    print(f'#{tc} {mx}')
