import sys
sys.stdin = open("sample_input_5249.txt")

import heapq

def prim(vertices):
    mst = []    # 가중치만 담을 리스트
    visited = set()
    start_vertex = vertices[0]

    min_heapq = [(w, start_vertex, e) for e, w in adj_list[start_vertex]]
    heapq.heapify(min_heapq)
    visited.add(start_vertex)

    while min_heapq:
        weight, start, end = heapq.heappop(min_heapq)
        if end in visited: continue

        visited.add(end)
        mst.append(weight)

        for next, weight in adj_list[end]:
            if next in visited: continue
            heapq.heappush(min_heapq,(weight, end, next))

    return mst


T = int(input())
for tc in range(1, T+1):
    V, E = map(int, input().split())
    vertices = [i for i in range(V+1)]
    edges = [list(map(int, input().split())) for _ in range(E)]

    adj_list = {i: [] for i in range(V+1)}
    for s, e, w in edges:
        adj_list[s].append((e, w))
        adj_list[e].append((s, w))
    # print(adj_list)

    mst = prim(vertices)
    print(f'#{tc} {sum(mst)}')