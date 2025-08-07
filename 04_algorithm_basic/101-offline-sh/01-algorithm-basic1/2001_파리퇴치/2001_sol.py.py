import sys
sys.stdin = open("input_2001.txt", "r")

T = int(input())
for t_c in range(1, T+1):
    n, m = map(int, input().split())

    arr = [list(map(int, input().split())) for _ in range(n)]


    sum_list = []

    for i in range(n-m+1):
        for j in range(n-m+1):
            sum_temp = 0
            for k in range(m):
                for s in range(m):
                    sum_temp += arr[i+k][j+s]
            sum_list.append(sum_temp)

    max_sum = max(sum_list)

    print(f'#{t_c} {max_sum}')