import sys
sys.stdin = open("input_1220.txt")

for tc in range(1, 11):
    N = int(input())
    arr = list(map(int, input().split()) for _ in range(100))

    arr_t = list(zip(*arr)) # arr 전치
    cnt = 0 # 교착 상태 개수를 세기 위한 변수

    for lst in arr_t:
        stack = []  # 1(N극)을 쌓기 위한 리스트 선언
        for j in range(100):
            if lst[j] == 1:
                stack.append(1)
            elif lst[j] == 2:
                if stack:
                    stack = []
                    cnt += 1
    print(f'{tc} {cnt}')