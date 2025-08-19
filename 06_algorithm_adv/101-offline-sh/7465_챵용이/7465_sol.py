import sys
sys.stdin = open("s_input_7465.txt")

def parent_calc(x):
    if x == parent[x]:
        return x
    return parent_calc(parent[x])

def union(x, y):
    root_x = parent_calc(x)
    root_y = parent_calc(y)

    if root_x != root_y:
        if rank[root_x] > rank[root_y]:
            parent[root_y] = root_x
        elif rank[root_x] < rank[root_y]:
            parent[root_x] = root_y
        else:
            parent[root_y] = root_x
            rank[root_x] += 1

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())

    parent = [i for i in range(N+1)]
    rank = [0] * (N+1)

    for _ in range(M):
        person_1,  person_2 = map(int, input().split())
        union(person_1, person_2)

    # ans = len(set(parent[1:]))
    # print(f'#{tc} {ans}')

    print(parent)
