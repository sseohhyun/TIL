def depth_first_search(vertex):
    '''
        vertex : 현재 방문 정점의 index
    '''
    # 글로벌에 있는 visited 사용하겠다 명시
    global visited

    # global에 있는 visited를 방문할 때마다 , 해당 idx를 True로 바꾸고 싶음(legb룰 따름)
    # 정점 방문
    visited[vertex] = True
    print(graph[vertex])

    # 현재 정점이 진출할 숫 있을 후보군을 찾음
    # 인접 행렬의 vertex번째 리스트를 순회함
    for idx in range(N):
    # for idx in range(len(adj_matrix)):
    # for candidate in adj_matrix[vertex]:
        # print(candidate)
        # 그 진출 후보국 A ~ G 중에, 가능한 경우에 대해서만
        # 인접 행렬에서, 내 번호 (내가 진출 가능한 후보군)
            # 진출 가능한 idx인지 확인하고, 그 idx 번째가 이전에 방문한 적이 있는지 확인
        if adj_matrix[vertex][idx] and visited[idx] == False:
            # 다음 후보군을 방문함
            depth_first_search(idx)


        # 0    1    2    3    4    5    6
graph = ['A', 'B', 'C', 'D', 'E', 'F', 'G']

# 정점 수: N
N = 7

# 해당 정점 방문 여부 표시 : False로 초기화
visited = [False] * N

# 인접 행렬
adj_matrix = [
#    A, B, C, D, E, F, G
    [0, 1, 1, 0, 0, 0, 0], # A
    [1, 0, 0, 1, 1, 0, 0], # B
    [1, 0, 0, 0, 1, 0, 0], # C
    [0, 1, 0, 0, 0, 1, 0], # D
    [0, 1, 1, 0, 0, 1, 0], # E
    [0, 0, 0, 0, 1, 0, 1], # F
    [0, 0, 0, 0, 0, 1, 0], # G
]

# 시작 정점을 0번인 A부터 시작
depth_first_search(0)
# print(visited)
