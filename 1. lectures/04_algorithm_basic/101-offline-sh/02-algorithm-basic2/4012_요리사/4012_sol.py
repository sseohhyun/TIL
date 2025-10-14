import sys
sys.stdin = open("sample_input_4012.txt")

from itertools import combinations

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    min_minus = float('inf')
    for a_set in combinations(range(N), N//2):
        a_sum, b_sum = 0, 0

        ## a_sum 구하기
        for i in range(len(a_set)):
            for j in range(i+1, len(a_set)):
                a_sum += arr[a_set[i]][a_set[j]]
                a_sum += arr[a_set[j]][a_set[i]]
        # print(a_set, a_sum)

        # b_set 계산
        ## b_set list 만들기
        b_set = [i for i in range(N)]
        for remove_idx in a_set:
            b_set.remove(remove_idx)

        ## b_sum 구하기
        for i in range(len(b_set)):
            for j in range(i+1, len(b_set)):
                b_sum += arr[b_set[i]][b_set[j]]
                b_sum += arr[b_set[j]][b_set[i]]
        # print(b_set, b_sum)

        minus = abs(a_sum - b_sum)
        min_minus = min(min_minus, minus)

    print(f"#{tc} {min_minus}")