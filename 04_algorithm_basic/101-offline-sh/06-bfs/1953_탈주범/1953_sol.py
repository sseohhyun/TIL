from collections import deque

def bfs(manhole_i, manhole_j):
    if arr[manhole_i][manhole_j] == 0:  # 시작점이 터널이 아닌 경우
        return 0

    visited = set()
    visited.add((manhole_i, manhole_j))
    queue = deque()
    queue.append((manhole_i, manhole_j))

    time = 1

    while time < L and queue:
        next_queue = deque()

        while queue:
            i, j = queue.popleft()
            dct_key = arr[i][j]

            if dct_key in dct:
                for di, dj in dct[dct_key]:
                    ni, nj = i + di, j + dj
                    if 0 <= ni < N and 0 <= nj < M and (ni, nj) not in visited and arr[ni][nj] != 0:

                        # 양방향 연결 확인
                        next_tunnel_type = arr[ni][nj]
                        if next_tunnel_type in dct:
                            # 목적지에서 현재 위치로 돌아올 수 있는지 확인
                            if (-di, -dj) in dct[next_tunnel_type]:
                                visited.add((ni, nj))
                                next_queue.append((ni, nj))

        queue = next_queue
        time += 1

    return len(visited)

import sys
sys.stdin = open("sample_input_1953.txt")

T = int(input())
for tc in range(1, T+1):
    N, M, R, C, L = list(map(int, input().split()))
    arr = [list(map(int, input().split())) for _ in range(N)]

    dct = {
        1: [(-1, 0), (1, 0), (0, -1), (0, 1)],
        2: [(-1, 0), (1, 0)],
        3: [(0, -1), (0, 1)],
        4: [(-1, 0), (0, 1)],
        5: [(1, 0), (0, 1)],
        6: [(1, 0), (0, -1)],
        7: [(-1, 0), (0, -1)]
    }

    print(f'#{tc} {bfs(R, C)}')