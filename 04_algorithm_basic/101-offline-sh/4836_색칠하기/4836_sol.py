'''
3
2
2 2 4 4 1
3 3 6 6 2
3
1 2 3 3 1
3 6 6 8 1
2 3 5 6 2
3
1 4 8 5 1
1 8 3 9 1
3 2 5 8 2
'''

T = int(input())
for t_c in range(1, T+1):
    n = int(input())
    lst = [list(map(int, input().split())) for _ in range(n)]

    arr = [[0]*10 for _ in range(10)]       # 10*10 arr를 0으로 초기화

    count = 0       # 보라색 칸 수
    for color in lst:
        r1, c1, r2, c2, color_type = color

        for i in range(r1,r2+1):
            for j in range(c1, c2+1):
                arr[i][j] += color_type     # 색 타입 별로 arr에 더하기

    for i in range(10):
        for j in range(10):
            if arr[i][j] >= 3:          # arr의 값이 3 이상인 경우만 카운트하기
                count += 1
    
    print(f'#{t_c} {count}')

