import sys
sys.stdin = open("sample_input_2819.txt", "r")

T = int(input())

def dfs(now):
    '''
        now : 현재 방문한 정점의 index 정보
    '''

    stack = []      # 방문 대상 후보군을 stack에 삽입해서 관리
    code = []       # 7개의 숫자를 받을 리스트

    # 현재 지점 방문
    visited.add(now)
    stack.append(now)

    # 순회 : 6번 반복
    while len(code) < 7:
        target = stack.pop()
        code.append(arr[target[0]][target[1]])
        for next in graph[target]:
            if next not in visited:
                visited.add(next)
                stack.append(next)
    code_num = "".join(code)
    return code_num

for tc in range(1, T+1):
    arr = [list(map(str, input().split())) for _ in range(4)]

    N = 4   # 4 * 4 격자
    graph = {}      # 그래프 인접 리스트 생성을 위해 graph 변수 선언

    # {(0, 0) : [(1, 0), (0, 1)]    ... }  이런 형태의 graph를 생성함
    for i in range(N):
        for j in range(N):
            temp = []
            for (dx, dy) in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                ni, nj = i+dx, j+dy
                if 0 <= ni < N and 0 <= nj < N:
                    temp.append((ni, nj))
            graph[(i, j)] = temp

    visited = set()     # 방문할 정점을 저장할 집합

    num_set = set()
    for i in range(N):
        for j in range(N):
            num_set.add(dfs((i, j)))

    print(f'#{tc} {len(num_set)}')
