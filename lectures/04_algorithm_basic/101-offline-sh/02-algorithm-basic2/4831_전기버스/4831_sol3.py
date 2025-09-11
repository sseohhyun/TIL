import sys
sys.stdin = open("sample_input_4831.txt")

'''
3 10 5
1 3 5 7 9
'''
T = int(input())
for t_c in range(1, T+1):
    k, n, m = map(int, input().split())
    charge = list(map(int, input().split()))

    start = 0
    cnt = 0

    charge_len = [0] * m
    for idx in range(1,m):
        charge_len[idx] = charge[idx] - charge[idx - 1]

    while True:
        if start + k >= n:
            break

        if max(charge_len) > k:
            break

        for i in range(start+k, start-1, -1):
            if i in charge:
                start = i
                # print(f"{start}에서 충전 한 번 합니당")
                cnt += 1
                break

    print(f'#{t_c} {cnt}')