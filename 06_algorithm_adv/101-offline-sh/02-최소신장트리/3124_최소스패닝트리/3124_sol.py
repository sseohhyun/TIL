import sys
sys.stdin = open("sample_input_3124.txt")
import heapq

def prim(vertices):
    mst_weight = 0
    visited = set()
    start_vertex = vertices[0]
    min_heapq = [(w, start_vertex, e) for e, w in adj_list[start_vertex]]
    heapq.heapify(min_heapq)
    visited.add(start_vertex)

    while min_heapq and len(visited) < len(vertices):
        weight, start, end = heapq.heappop(min_heapq)
        if end in visited: continue
        visited.add(end)
        mst_weight += weight
        for next, weight in adj_list[end]:
            if next not in visited:
                heapq.heappush(min_heapq, (weight, end, next))
    return mst_weight

T = int(input())
for tc in range(1, T+1):
    V, E = map(int, input().split())
    vertices = [i for i in range(1, V + 1)]
    edges = [list(map(int, input().split())) for _ in range(E)]

    adj_list = {v: [] for v in vertices}
    for s, e, w in edges:
        adj_list[s].append((e, w))
        adj_list[e].append((s, w))

    result = prim(vertices)

    print(f'#{tc} {result}')