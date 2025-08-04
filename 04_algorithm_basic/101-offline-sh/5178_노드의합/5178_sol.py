import sys
sys.stdin = open("sample_input_5178.txt", "r")

T = int(input())
for t_c in range(1, T+1):
    N, M, L = list(map(int, input().split()))

    ### 1. 노드의 level 구하기 ###
    n, level = N, 0
    while True:     # level 구하기 위한 반복문
        if n < 1:   # 만약 n이 1보다 작으면 중단함
            break
        n = n // 2  # 예를 들어 n이 10일 경우 5 -> 2 -> 1로 몫을 재할당
        level += 1  # 한 번 나눌 때 마다 level을 1씩 증가시킴

    ### 2. tree 생성 ###
    tree = [0] * (2 ** level)   # 해당 level의 최대 노드 수만큼 tree를 생성함
    for _ in range(M):      # 각 노드의 값을 입력 받아서 tree에 인덱싱으로 값을 넣음
        node, value = list(map(int, input().split()))
        tree[node] = value

    ### 3. 노드의 합 구하기 ###
    for i in range(N//2,0,-1):
        if tree[i] == 0 :
            tree[i] = tree[i*2] + tree[i*2+1]
        else:
            pass

    ### 4. L 위치에 해당하는 결과 출력하기 ###
    print(f'#{t_c} {tree[L]}')