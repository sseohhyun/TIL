import heapq

def prim(vertices, edges):
    mst = []        # 최소 신장 트리를 그릴 수 있는 간선 목록
    visited = set()     # 한 번 방문한 정점은 안감
    # 시작 정점이 무엇이든 상관없음
    start_vertex = vertices[0]

    # 시작 정점에서 갈 수 있는 모든 정점들에 대한 간선 정보를 heapq에 삽입
    # print(adj_list[start_vertex])
    # 가중치, 시작정점, 종료정점
    min_heapq = [(w, start_vertex, e) for e, w in adj_list[start_vertex]]
    print(min_heapq)
    heapq.heapify(min_heapq)
    # print(min_heapq)
    visited.add(start_vertex)

    while min_heapq:    # 모든 후보군 순회 완료할 때 까지
        weight, start, end = heapq.heappop(min_heapq)
        # 이미 방문한 적이 있으면 건너뛰기
        if end in visited: continue

        visited.add(end)        # 새로운 정점 방문
        mst.append((start, end, weight))    # 이 간선 정보 mst에 추가

        for next, weight in adj_list[end]:
            # 현재의 도착 정점에서 이어진 인접 정점이
            # 즉 다음에 방문 할 예정이었던 정점이 이미 방문한 적이 있다면
            # 후보군에 넣을 필요x
            if next in visited: continue
            heapq.heappush(min_heapq, (weight, end, next))

    return mst
'''
    가중치 그래프 형상
         1
      ¹ / \ ²
       2---3
         ³
'''
vertices = [1, 2, 3]
edges = [[1, 2, 1], [2, 3, 3], [1, 3, 2]]
# 이 그래프 기준 ,인접 정점 정보를 가지고 있어야 함
# 즉, 인접 행렬 혹은 인접 리스트가 필요함
adj_list = {v: [] for v in vertices}
for s, e, w in edges:
    adj_list[s].append((e, w))
    adj_list[e].append((s, w))
print(adj_list)

'''
    MST 구성 결과
         1
      ¹ / \ ²
       2   3
'''
mst = prim(vertices, edges)  # [(1, 2, 1), (1, 3, 2)]
print(mst)


# 교재 간선 정보
edges = [
    (0, 1, 32),
    (0, 2, 31),
    (0, 5, 60),
    (0, 6, 51),
    (1, 2, 21),
    (2, 4, 46),
    (2, 6, 25),
    (3, 4, 34),
    (3, 5, 18),
    (4, 5, 40),
    (4, 6, 51),
]
vertices = list(range(7))  # 정점 집합
adj_list = {v: [] for v in vertices}
for s, e, w in edges:
    adj_list[s].append((e, w))
    adj_list[e].append((s, w))
print(adj_list)

result = prim(vertices, edges)
print(result) # [(0, 2, 31), (2, 1, 21), (2, 6, 25), (2, 4, 46), (4, 3, 34), (3, 5, 18)]