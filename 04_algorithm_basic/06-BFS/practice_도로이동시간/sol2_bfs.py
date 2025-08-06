import sys
sys.stdin = open('input.txt')

from collections import deque

dx = [-1 ,1, 0, 0]
dy = [0, 0, -1, 1]

def get_road_move_time(road, N, M):
    # 후보군에 단순 좌표만 넣었다면, 이번에는
    # 후보군에, 그 후보군이 얼만큼의 누적 시간을 가지고 있는지도 기록
    queue = deque()
    # x, y, cnt
    queue.append((0, 0, 0))
    # 물론 후보군에 cnt 넣는거랑 별개로 visited는 필요함
    visited = [0 * M for _ in range(N)]
    visited[0][0] = 1 # 시작 정점 방문 처리

    while queue:
        row, col, dist = queue.popleft()
        for k in range(4):
            nx = row + dx[k]
            ny = col + dy[k]

            # 범위를 벗어났으면 조사 못함
            if nx < 0 or nx >= N or ny < 0 or ny >= M:
                continue

            # 이미 방문한 경우
            if visited[nx][ny]:
                continue

            # 길이 아닌 경우
            if road[nx][ny] == 0:
                continue

            # 도착 지점인 경우
            if nx == N-1 and ny == M-1:
                return dist + 1

            # 위 조건들에 충족 안되면 후보군에 등록해야함
            visited[nx][ny] = 1
            queue.append((nx, ny, dist+1))
    return -1

# 도로의 크기 N * M 입력 받기
N, M = map(int, input().split())
road = [list(map(int, input())) for _ in range(N)]
result = get_road_move_time(road, N, M)
print(result)
