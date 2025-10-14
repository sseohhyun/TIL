'''
24 2
100 17 39 22 100 8 100 7 7 100 2 7 2 15 15 4 6 2 11 6 4 10 4 2
'''

from collections import deque

def bfs(start_node, dct_list):
    # 방문했는지 확인 + 몇 번째로 방문한지를 확인하기 위해 리스트 선언
    visited = [-1] * 101
    # 시작점은 처음에 방문하므로 0으로 변경
    visited[start_node] = 0
    queue = deque()
    queue.append(start_node)

    while queue:
        node = queue.popleft()
        for neighbor in dct_list.get(node, []):
            # 연결된 번호를 for문으로 돌면서 해당 번호가 방문하지 않았다면 (-1이라면)
            if visited[neighbor] == -1:
                # 전에 방문했던 visited의 값보다 1 증가시킨 값으로 넣어줌
                visited[neighbor] = visited[node] + 1
                queue.append(neighbor)
    return visited

import sys
sys.stdin = open("input_1238.txt", "r")

for tc in range(1, 11):
    # n : 입력받는 lst의 총 길이, start : 시작점
    n, start = map(int, input().split())
    lst = list(map(int, input().split()))

    # 인접리스트를 만들기 위한 빈 딕셔너리 선언
    dct = {lst[i]: set() for i in range(0, n, 2)}

    # lst의 데이터를 dct에 반영하기
    for idx in range(0, n, 2):
        dct[lst[idx]].add(lst[idx + 1])

    # visited 리스트를 반환함
    result_lst = bfs(start, dct)
    # visited 리스트에서 최대값에 해당하는 인덱스를 반환함
    idx_mx = [i for i, val in enumerate(result_lst) if val == max(result_lst)]
    # 인덱스 중에서 최대값을 ans에 할당
    ans = max(idx_mx)
    print(f'#{tc} {ans}')