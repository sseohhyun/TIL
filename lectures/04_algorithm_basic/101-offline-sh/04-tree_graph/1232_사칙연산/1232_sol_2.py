import sys
sys.stdin = open("input_1232.txt", "r")

for t_c in range(1, 11):
    N = int(input())

    tree = [0] * (N+1)
    children = {}

    for _ in range(N):
        input_list = input().split()
        if len(input_list) == 2:
            key, value = input_list
            tree[int(key)] = int(value)
        else:
            key, value, left, right = input_list
            tree[int(key)] = value
            children[int(key)] = (int(left), int(right))

    def calc(idx):
        if isinstance(tree[idx], int):
            return tree[idx]    # 만약 tree[idx]가 정수(int)라면, 그 값을 그대로 반환
        children_left, children_right = children[idx]

        if tree[idx] == '+':
            return calc(children_left) + calc(children_right)
        elif tree[idx] == '-':
            return calc(children_left) - calc(children_right)
        elif tree[idx] == '*':
            return calc(children_left) * calc(children_right)
        elif tree[idx] == '/':
            return calc(children_left) / calc(children_right)

    print(f'#{t_c} {int(calc(1))}')