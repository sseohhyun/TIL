import sys
sys.stdin = open("sample_input_3289.txt")

def parent_calc(x):
    if x == parent[x]:
        return x
    parent[x] = parent_calc(parent[x])
    return parent[x]

def union(x, y):
    root_x = parent_calc(x)
    root_y = parent_calc(y)

    if root_x != root_y:
        parent[root_y] = root_x

T = int(input())
for tc in range(1, T+1):
    n, m = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(m)]

    parent = [i for i in range(n+1)]
    result = []

    for lst in arr:
        if lst[0] == 0:
            union(lst[1], lst[2])
        elif lst[0] == 1:
            parent_1 = parent_calc(lst[1])
            parent_2 = parent_calc(lst[2])

            if parent_1 == parent_2:
                result.append("1")
            else:
                result.append("0")

    ans = "".join(result)

    print(f'#{tc} {ans}')

