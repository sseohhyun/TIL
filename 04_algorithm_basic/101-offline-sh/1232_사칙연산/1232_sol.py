import sys
sys.stdin = open("input_1232.txt", "r")

for t_c in range(1, 11):
    N = int(input())

    ### 1. level 구하기 ###
    n, level = N, 0
    while True:     # level을 구하기 위한 반복문
        if n < 1:
            break
        n = n // 2
        level += 1

    ### 2. 트리 생성 ###
    tree = [0] * (2 ** level)
    for _ in range(N):
        idx, value, *trash = input().split()
        tree[int(idx)] = int(value) if value.isnumeric() else value

    ### 3. 노드 계산하기 ###
    for i in range(N//2, 0, -1):
        if tree[i] == "+":
            tree[i] = tree[i * 2] + tree[i * 2 + 1]
        elif tree[i] == "-":
            tree[i] = tree[i * 2] - tree[i * 2 + 1]
        elif tree[i] == "*":
            tree[i] = tree[i * 2] * tree[i * 2 + 1]
        elif tree[i] == "/":
            tree[i] = tree[i * 2] / tree[i * 2 + 1]

    ### 4. 결과 출력하기 ###
    print(f'#{t_c} {int(tree[1])}')
