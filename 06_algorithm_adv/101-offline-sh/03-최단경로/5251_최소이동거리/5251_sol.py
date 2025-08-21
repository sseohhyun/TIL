import sys
sys.stdin = open("sample_input_5251.txt")

import heapq


def dijkstra(graph, start):
    distance = {v: float('inf') for v in graph}
    distance[start] = 0

    heap = []
    heapq.heappush(heap, [0, start]) # [weight, start]
    visited = set()

    while heap:
        dist, current = heapq.heappop(heap)
        # 방문한적이 있거나, 기존 거리보다 갱신된 거리가 더 크면 넘어가라~~
        if current in visited or distance[current] < dist: continue
        visited.add(current)
        for next, weight in graph[current]:
            next_distance = dist + weight
            if next_distance < distance[next]:
                distance[next] = next_distance
                heapq.heappush(heap, [next_distance, next])
    return distance

T = int(input())
for tc in range(1, T+1):
    V, E = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(E)]

    graph = {i: [] for i in range(V+1)}
    for s, e, w in arr:
        graph[s].append((e, w))

    print(graph)
    result = dijkstra(graph, 0)
    print(f'#{tc} {result[V]}')