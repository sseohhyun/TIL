import sys
sys.stdin = open("s_input_7465.txt")


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
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(M)]

    parent = [i for i in range(N + 1)]
    rank = [0] * (N + 1)

    for person_1, person_2 in arr:
        union(person_1, person_2)

    reverse_arr = list(reversed(arr))
    for person_1, person_2 in reverse_arr:
        union(person_1, person_2)

    ans = len(set(parent[1:]))
    print(f'#{tc} {ans}')

