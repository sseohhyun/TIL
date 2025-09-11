def depth_first_search(node):
    '''
        node : 현재 방문 노드
    '''
    # 현재 노드를 방문
    print(node)

    # 자식 노드가 없으면 순회하지 않도록
    if node not in adj_list:
        return

    # node가 가진 모든 자식 노드들에 대해서 순회하여 동일한 깊이 우선 탐색
    for next in adj_list.get(node):
        depth_first_search(next)

adj_list = {
    "A": ["B", "C", "D"],
    "B": ["E", "F"],
    "C": [],
    "D": ["G", "H", "I"]
}

depth_first_search("A")