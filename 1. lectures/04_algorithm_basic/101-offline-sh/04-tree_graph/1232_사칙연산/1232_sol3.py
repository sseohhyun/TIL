import sys
sys.stdin = open("input_1232.txt", "r")

for tc in range(1, 11):
    N = int(input())
    arr = [list(map(lambda i: int(i) if i.isnumeric() else i, input().split())) for _ in range(N)]
    dct = {i: [] for i in range(1, N+1)}
    # print(dct)

    calc_stack = []
    for lst in arr:
        if len(lst) == 2:
           dct[lst[0]] = lst[1]

        else:
            calc_stack.append(lst)

    while calc_stack:
        now_calc = calc_stack.pop()
        key, calc, left_key, right_key = now_calc

        if calc == "+":
            dct[key] = dct[left_key] + dct[right_key]
        elif calc == "-":
            dct[key] = dct[left_key] - dct[right_key]
        elif calc == "*":
            dct[key] = dct[left_key] * dct[right_key]
        elif calc == "/":
            dct[key] = dct[left_key] / dct[right_key]

    print(f'#{tc} {int(dct[1])}')