import sys
sys.stdin = open("sample_input_5099.txt")

from collections import deque

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    lst = list(map(int, input().split()))
    num_lst = [[num + 1, val] for num, val in enumerate(lst)] # (피자 번호, 치즈 양) 형태로 리스트에 넣음

    wait_queue = deque(num_lst)
    cook_queue = deque()

    # 화덕 사이즈에 맞춰 피자 넣기 => cook_queue에 넣기
    for _ in range(N):
        cook_queue.append(wait_queue.popleft())
    # print("이건 처음 쿡큐", cook_queue)
    # print("이건 대기 큐", wait_queue)


    while len(cook_queue) > 1:
        pizza = cook_queue.popleft()

        pizza[1] //= 2
        if pizza[1] == 0:
            if wait_queue:
                cook_queue.append(wait_queue.popleft())
        else:
            cook_queue.append(pizza)

    print(f"#{tc} {cook_queue[0][0]}")