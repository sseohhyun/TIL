import sys
sys.stdin = open("sample_input_4831.txt")

T = int(input())

for t_c in range(1, T+1):
    K, N, M = map(int, input().split())
    charge = list(map(int, input().split()))

    # 정류소 도표화
    station = [0 for _ in range(N+1)]
    # 충전소 위치 표시
    for i in charge:
        station[i] = 1
    # print(station)

    count = 0
    now = K         # 현재 위치 -> 처음 = 0 + 최대 이동 가능 거리
    charge = 0      # 마지막 충전 위치 -> 처음 = 0

    while now < N :
        if station[now] == 1:   # 현재 위치에 충전기가 있으면
            count += 1          # 충전 횧수 += 1
            charge = now        # 마지막 충전 위치를 지금으로 변환
            now += K            # 현재 위치 += 최대 이동 거리
        else:                   # 현재 위치에 충전기가 없으면 지금 위치에서 -1
            now -=1

        # 마지막 충전 위치까지 후진했다 -> 실패
        if charge == now:
            count = 0
            break


    '''
    start = 0
    count = 0
    
    while start + K < N:  # 종점(N)에 도착할 때 까지 계속 반복
        moved = False   # 충전 여부를 나타내는 플래그

        # K부터 1까지 거꾸로 확인하면서, 충전소 있는 곳 찾기
        for i in range(K, 0, -1):
            if (start + i) in charge:
                start += i
                count += 1
                moved = True
                break

        if not moved:
            count = 0
            break
    '''

    print(f"#{t_c} {count}")