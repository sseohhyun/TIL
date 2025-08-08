from collections import deque

T = int(input())
for tc in range(1, T+1):
    lst = list(map(int, input()))

    # 1. 정렬
    num_list = sorted(lst)
    # print(num_list)

    # 2. triplet 확인 -> 해당 숫자는 빼기 -> 또 확인 -> 없으면 run 확인하러 가기
        ## 큐를 써서 넣고 빼고 하려고 했는데, [4, 4, 4, 4, 5, 6] 같은데 그대로 나옴
        ## 중간에 팝을 해버려서 그런 듯 그렇다고 for 문 돌아가는데 remove할 수가 없어서..큐 쓰는게 아닌듯

    queue = deque()
    queue.append(num_list[0])
    for i in range(1, len(num_list)):
        if num_list[i] == num_list[i-1]:
            queue.append(num_list[i])
        else:
            for _ in range(len(queue)):
                queue.popleft()
            queue.append(num_list[i])

    if 3 <= len(queue) < 6:
        remove_num = queue.popleft()
        for _ in range(3):
            num_list.remove(remove_num)

    elif len(queue) == 6:
        num_list = []

    print(num_list)

    # 3. run 확인 -> 해당 숫자 빼기 -> 또 확인 -> 있으면 제거


    '''
    # 4. len이 0이면 true, 아니면 false를 출력하기
    if len(num_list) == 0:
        result = True
    else: result = False
        
    print(f'#{tc} {result}')
    '''