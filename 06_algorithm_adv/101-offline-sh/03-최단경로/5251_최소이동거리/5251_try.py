import sys
sys.stdin = open("sample_input_5251.txt")

import heapq

def dijkstra(graph, start):
    # distance 리스트 준비 + 첫번째 노드는 방문 처리해야 함
    distance = [float('inf')] * (V+1)
    distance[0] = 0
    # visited set 준비
    visited = set()
    # 최소힙 준비 + 처음 자료 넣어두기
    heap = []
    heapq.heappush(heap, (0, start))    # 거리, 시작 노드

    while heap:
        dist, current = heapq.heappop(heap)
        if current in visited or distance[current] > dist: continue
        visited.add(current)
        for next, weight in graph[current]:
            new_dist = dist + weight
            if new_dist < distance[next]:
                distance[next] = new_dist
            heapq.heappush(heap, (new_dist, next))

    return distance


T = int(input())
for tc in range(1, T+1):
    V, E = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(E)]

    # 인접리스트 형태로 그래프 바꾸기
    graph = {i: [] for i in range(V+1)}
    for s, e, w in arr:
        graph[s].append((e,w))

    result = dijkstra(graph, 0)
    ans = result[-1]
    print(ans)