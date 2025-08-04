import sys
sys.stdin = open("input_1210.txt","r")

for _ in range(10):
    t_c = int(input())
    arr = [[0] + list(map(int, input().split())) + [0] for _ in range(100)]
    # 좌우에 0으로 한줄씩 더 패딩해줌 -> 인덱싱을 벗어나지 않게 하기 위함

    moving_point_i, moving_point_j = 0, 0
    for j in range(102):  # 마지막 줄에서 '2' 찾기
        if arr[99][j] == 2:
            moving_point_i = 99  # 2인 경우 moving_point의 i, j 인덱스 설정
            moving_point_j = j
            arr[moving_point_i][moving_point_j] = 0  # moving_point가 도착했으면 0으로 값을 초기화

    while moving_point_i > 0:
        if arr[moving_point_i][moving_point_j - 1] == 1:  # 현재 위치를 기준으로 왼쪽이 1인 경우 moving point 이동
            moving_point_j -= 1
            arr[moving_point_i][moving_point_j] = 0

        elif arr[moving_point_i][moving_point_j + 1] == 1:  # 현재 위치를 기준으로 오른쪽이 1인 경우 moving point 이동
            moving_point_j += 1
            arr[moving_point_i][moving_point_j] = 0

        else:
            moving_point_i -= 1  # 위로 이동
            arr[moving_point_i][moving_point_j] = 0

    print(f'#{t_c} {moving_point_j - 1}')