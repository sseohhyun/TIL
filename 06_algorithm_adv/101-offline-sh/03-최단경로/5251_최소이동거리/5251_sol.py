import sys
sys.stdin = open("sample_input_5251.txt")

import heapq, math
INF = math.inf

def bellman_ford(graph, start):
    distance = {v: INF for v in graph}
    distance[start] = 0

    for _ in range(N-1):
        updated = False
        for u in graph:
            for v, weight in graph[u]:
                if distance[u] != INF and distance[u] + weight < distance[v]:
                    distance[v] = distance[u] + weight
                    updated = True
        if updated == False:
            break

    for u in graph:
        for v, weight in graph[u]:
            if distance[u] != INF and distance[u] + weight < distance[v]:
                print("음수사이클")
                return False

    return distance[N]

T = int(input())
for tc in range(1, T+1):
    N, E = map(int, input().split())
    adj_list = {v: [] for v in range(N+1)}

    # 인접 리스트로 만들기
    for _ in range(E):
        s, e, w = map(int, input().split())
        adj_list[s].append((e,w))

    result = bellman_ford(adj_list, 0)
    print(f'#{tc} {result}')



