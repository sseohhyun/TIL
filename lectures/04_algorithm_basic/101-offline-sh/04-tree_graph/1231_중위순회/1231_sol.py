import sys
sys.stdin = open("input_1231.txt", "r")

for t_c in range(1,11):
    N = int(input())
    input_data = [list(input().split()) for _ in range(N) ]

    for lst in input_data:      # 리스트 별로 돌기
        for i in range(len(lst)):   # 리스트의 인덱스 별로 돌기
            if lst[i].isnumeric():      # 숫자라면 int로 형변환
                lst[i] = int(lst[i])

    ### 1. 트리 생성 ###
    tree = [0] * (N+1)
    for lst in input_data:      # tree 리스트 생성
        tree[lst[0]] = lst[1]

    ### 2. 중위 순회 ###
    answer_list = []    # 순서        대로 리스트에 누적할 용도
    def inorder_traversal(idx):
        if idx <= N:
            inorder_traversal(idx * 2)  # 왼쪽 서브 트리
            answer_list.append(tree[idx])   # 왼쪽 서브 트리 순회 후 조사
            inorder_traversal(idx * 2 + 1)  # 오른쪽 서브 트리
        return answer_list
    answer = "".join(inorder_traversal(1))  # 리스트를 조인함

    print(f'#{t_c} {answer}')


