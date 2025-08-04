# import sys
# sys.stdin = open("sample_input_2382.txt", "r")
'''
input_data_example
10      
7 2 9   
1 1 7 1 
2 1 7 1
5 1 5 4
3 2 8 4 
4 3 14 1
3 4 3 3 
1 5 8 2 
3 5 100 1
5 5 1 1
'''

T = int(input())
for t_c in range(1, T+1):
    # 구역의 한 변에 있는 셀의 개수 N, 격리 시간 M, 미생물 군집의 개수 K
    N, M, K = map(int, input().split())
    microbe = [list(map(int, input().split())) for _ in range(K)]

    # 테두리를 -1로 이외의 영역을 0으로 하는 arr를 생성함
    arr = [[-1] * N] + [[-1] + [0] * (N-2) + [-1] for _ in range(N-2)] + [[-1] * N]
    di = [0, -1, 1, 0, 0]
    dj = [0, 0, 0, -1, 1]

    # arr에 [미생물 개수, 방향 타입] 값으로 들어감
    for lst in microbe:
        i_idx, j_idx, *group = lst
        arr[i_idx][j_idx] = group
    
    time = 0
    while time < M:     # M이 될 때까지 반복
        time += 1
        
        for 
        i_idx = i_idx + di[arr[i_idx][j_idx][1]]
        j_idx = j_idx + dj[arr[i_idx][j_idx][1]]
        arr[i_idx][j_idx]
    def direction()


