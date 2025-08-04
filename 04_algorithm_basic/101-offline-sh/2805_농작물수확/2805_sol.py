import sys
sys.stdin = open("input_2805.txt", "r")

T = int(input())
for t_c in range (1, T+1):
    N = int(input())
    arr = [list(map(int, input())) for _ in range(N)]

    n = N // 2 # 가운데를 나타낼 인덱스
    get_sum = 0 # 최종 결과 : 농작물의 가치의 총합

    for i in range(N):
        if i <= n:
            for j in range(n-i, n+i+1):
                get_sum += arr[i][j]
        else:
            for j in range(i-n, N-i+n):
                get_sum += arr[i][j]
    
    print(f'#{t_c} {get_sum}')
