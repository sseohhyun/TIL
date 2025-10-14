def check_sum_arr(arr, calc, index):  # 제곱합 arr, idx를 누적한 arr 생성 함수
    for i in range(N):
        for j in range(N):
            check = M
            back = 0
            each_sum = 0

            while True:
                if check < 1:
                    break
                if 0 > j - back:
                    break
                if each_sum + arr[i][j - back] > C:
                    break

                each_sum += arr[i][j - back]
                calc[i][j] += arr[i][j - back] ** 2
                index[i][j].append((i, j - back))
                check -= 1
                back += 1

def max_arr(arr):       # 계산한 제곱합 arr에서 최대값에 해당하는 i,j 값 반환
    mx = 0
    max_i, max_j = 0, 0
    for i in range(N):
        for j in range(N):
            if mx < arr[i][j]:
                mx = arr[i][j]
                max_i, max_j = i, j
    return [max_i, max_j]

def check_idx_zero(i, j, index, calc):   # idx를 누적한 arr에 접근해서 해당 위치의 값을 0으로 만듦
    for idx_i, idx_j in index[i][j]:
        calc[idx_i][idx_j] = 0

import sys
sys.stdin = open("sample_input_2115.txt")


T = int(input())
for tc in range(1, T+1):
    '''
        N = 벌통들의 크기
        M = 선택할 수 있는 벌통의 개수
        C = 꿀을 채취할 수 있는 최대 양
    '''
    N, M, C = list(map(int, input().split()))
    arr = [list(map(int, input().split())) for _ in range(N)]

    calc_arr = [[0] * N for _ in range(N)]
    index_arr = [[[] for _ in range(N)] for _ in range(N)]

    check_sum_arr(arr, calc_arr, index_arr)
    # 첫 번째 최대값 구하기
    mx_i_1, mx_j_1 = max_arr(calc_arr)
    result = calc_arr[mx_i_1][mx_j_1]
    check_idx_zero(mx_i_1, mx_j_1, index_arr, calc_arr)

    # 두 번째 최대값 구하기
    mx_i_2, mx_j_2 = max_arr(calc_arr)
    result += calc_arr[mx_i_2][mx_j_2]

    print(f'#{tc} {result}')

