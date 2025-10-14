import sys
sys.stdin = open("re_sample_input_1251.txt")

import heapq

def prim(adj_list):
    mst = 0
    start_vertex = 0

    visited = set()
    visited.add(start_vertex)

    min_heapq = [(w, start_vertex, e) for e, w in adj_list[start_vertex]]
    heapq.heapify(min_heapq)

    while min_heapq:
        weight, start, end = heapq.heappop(min_heapq)
        if end in visited: continue

        visited.add(end)
        mst += weight

        for next, weight in adj_list[end]:
            if next in visited: continue
            heapq.heappush(min_heapq, (weight, end, next))

    return mst

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(float, input().split())) for _ in range(2)]
    E = float(input())
    loc = list(zip(*arr))

    adj_list = {v: [] for v in range(N)}

    for i in range(N):
        for j in range(N):
            if i == j : continue
            else:
                length = E * (abs(loc[i][0] - loc[j][0]))**2 + E * (abs(loc[i][1] - loc[j][1]))**2
                adj_list[i].append((j, length))
    # print(edges)
    result = int(round(prim(adj_list), 0))
    print(f'#{tc} {result}')