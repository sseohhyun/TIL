from collections import deque


def BFS(start_vertex):
    '''
        인접 행렬로 순회 시 -> 정점의 index
        인접 리스트로 순회 시 -> 정점의 값
    '''

    # 해당 정점 방문 여부 표시할 배열이 하나 필요함
    # visited = [0] * len(nodes)
    visited = set()

    # 후보군을 저장
    # deque는 첫번째 인자로 iterable한 객체를 받음
    queue = deque([start_vertex])  # 더블 엔디드 큐 (일반적으로 큐로 자주 씀)
    visited.add(start_vertex)
    result = []  # 최종 결과값

    while queue:
        node = queue.popleft()
        result.append(node)

        # # 모든 노드들에 대해서 인덱스 조사
        # for next_index in range(len(nodes)):
        #     if next_index not in visited and adj_matrix[node][next_index]:
        #         visited.add(next_index)
        #         queue.append(next_index)

        # 내 인접 리스트에서 인접 정점 찾아서 순회
        for neighbor in adj_list.get(node, []):
            # 해당 정점 아직 방문한 적 없다면
            if neighbor not in visited:
                visited.add(neighbor)  # 방문 예정 표시
                queue.append(neighbor)  # 다음 후보군에 추가

    return result


# 정점 정보
#         0    1    2    3    4    5    6
nodes = ['A', 'B', 'C', 'D', 'E', 'F', 'G']

# 간선 정보
edges = [
    '0 1',
    '0 2',
    '1 3',
    '1 4',
    '2 4',
    '3 5',
    '4 5',
    '5 6'
]

### 1. 인접 리스트 형태 ###
'''
adj_list = {
    "a": ["b", "c"]
    ...
'''
adj_list = {node: [] for node in nodes}
# print(adj_list)
# 간선 정보와 정점의 index 정보로 adj_list 채워주기
for edge in edges:
    u, v = edge.split()  # 시작 정점, 도착 정점
    # print(nodes[int(u)], nodes[int(v)])
    # 현재 간선 정보는 '무방향' 그래프이다 -> 양쪽으로 다 갈 수 있다는 뜻
    adj_list[nodes[int(u)]].append(nodes[int(v)])
    # 반대 방향으로도 넣어줌으로써 양방향 그래프로 만들어줌
    adj_list[nodes[int(v)]].append(nodes[int(u)])
# print(adj_list)
print(BFS("A"))

### 2. 인접 행렬 형태 ###
adj_matrix = [[0] * len(nodes) for _ in range(len(nodes))]
# [[0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0]]
# print(adj_matrix)
for edge in edges:
    u, v = edge.split()
    u_index, v_index = int(u), int(v)
    # print(u_index, v_index)
    adj_matrix[u_index][v_index] = 1
    adj_matrix[v_index][u_index] = 1
# print(adj_matrix)
# print(BFS(0))
