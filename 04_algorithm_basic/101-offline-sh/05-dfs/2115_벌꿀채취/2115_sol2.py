def dfs(row, col, hap, square_hap, idx_list):
    global max_square_hap, max_idx_list

    if hap > C:
        return

    if start_j+M == col:
        if max_square_hap < square_hap:
            max_square_hap = square_hap
            max_idx_list = idx_list[:]
        return

    if arr[row][col] > 0:   # 2번째 채취 시에는 0으로 설정한 칸이 있는데 걔는 이미 선택된 거니까 선택하면 안돼서 조건 추가
        # 선택한 경우
        idx_list.append((row, col))
        dfs(row, col+1, hap + arr[row][col], square_hap + arr[row][col]**2, idx_list)
        # 선택하지 않은 경우
        idx_list.remove((row, col))
        dfs(row, col+1, hap, square_hap, idx_list)

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

    max_square_hap = 0
    max_idx_list = []

    # 첫번째 채취
    for i in range(N):
        for j in range(N-M+1):
            start_i, start_j = i, j
            dfs(start_i, start_j, 0, 0, [])
    first_max = max_square_hap

    # 해당 위치에 대한 arr 값을 0으로 바꾸기
    for i, j in max_idx_list:
        arr[i][j] = 0

    max_square_hap = 0
    max_idx_list = []

    # 두번째 채취
    for i in range(N):
        for j in range(N-M+1):
            start_i, start_j = i, j
            dfs(start_i, start_j, 0, 0, [])
    second_max = max_square_hap

    print(f'#{tc} {first_max + second_max}')