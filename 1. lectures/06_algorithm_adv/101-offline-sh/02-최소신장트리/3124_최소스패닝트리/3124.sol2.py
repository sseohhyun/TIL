def find_set(x):
    if x != parent[x]:
        parent[x] = find_set(parent[x])
    return parent[x]

def union(x, y):
    root_x = find_set(x)
    root_y = find_set(y)

    if root_x != root_y:
        if rank[root_x] < rank[root_y]:
            parent[root_x] = root_y
        elif rank[root_x] > rank[root_y]:
            parent[root_y] = root_x
        else:
            parent[root_y] = root_x
            rank[root_x] += 1
        return True
    return False

import sys
sys.stdin = open("sample_input_3124.txt")

T = int(input())
for tc in range(1, T+1):
    V, E = map(int, input().split())
    vertices = [i for i in range(1, V + 1)]
    edges = [list(map(int, input().split())) for _ in range(E)]

    parent = [i for i in range(V+1)]
    rank = [0] * (V+1)

    edges.sort(key=lambda x: x[2])

    mst_weight = 0
    edge_count = 0

    for s, e, w in edges:
        if union(s, e):
            mst_weight += w
            edge_count += 1
            if edge_count == V - 1:
                break

    print(f'#{tc} {mst_weight}')
