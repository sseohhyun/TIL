T = int(input())
for t_c in range(1, T+1):
    # 구역의 한 변에 있는 셀의 개수 N, 격리 시간 M, 미생물 군집의 개수 K
    N, M, K = map(int, input().split())
    microbe = [list(map(int, input().split())) for _ in range(K)]

    di = [0, -1, 1, 0, 0]
    dj = [0, 0, 0, -1, 1]
    time = 0

    def change_dir(dir_type):       # 방향 전환 함수
        if dir_type == 1: dir_type = 2
        elif dir_type == 2: dir_type = 1
        elif dir_type == 3: dir_type = 4
        elif dir_type == 4: dir_type = 3
        return dir_type

    while time < M :
        for lst in microbe:
            i, j, cnt, type = lst
            lst[0] += di[type]
            lst[1] += dj[type]

            if lst[0] in (0,6) or lst[1] in (0,6):
                lst[2] = cnt//2
                lst[3] = change_dir(type)
            
            ### 여러 개 군집 합치기 ### 
            
        time += 1