from collections import deque
import sys
sys.stdin = open('input.txt')

dx = [-1 ,1, 0, 0]
dy = [0, 0, -1, 1]

def get_road_move_time(row, col):
    # queue = deque([(0, 0)]) # 리스트안에 튜플 형태로 넣어야지 iterable해짐
    queue = deque()
    queue.append((0, 0))        #시작 정점 후보군에 삽입
    distance[0][0] = 0

    # BFS 탐색
    while queue:    # 후보군이 있는 동안
        row, col = queue.popleft()
        # 이 위치에서 4 방향에 대한 탐색
        for k in range(4):
            nx = row + dx[k]
            ny = col + dy[k]
        # 이제 그 다음 탐색지 data[nx][ny] 번째가 이동 가능한지 판별 -> 리스트 범위 안? 방문한적x(-1) ?
        # 그 위치가 길 이어야 함 -> 1은 길 0 은 벽
            if 0 <= nx < N and 0 <= ny < M and distance[nx][ny] == -1 and data[nx][ny]:
                queue.append((nx, ny))
                # 다음 위치까지 도달하는 비용은, 내 위치보다 1 증가한 값
                distance[nx][ny] = distance[row][col] + 1
                # 도착지점에 도착하면, BFS 특성상 가장 빠르게 도착한 길이니
                # 그때까지의 비용을 할당하고 종료
                if nx == N-1 and ny == M-1:     #도착지임
                    return
    # 모든 후보군을 다 탐색했지만, return 되어서 함수가 종료된 적이 없이 코드가 이곳까지 도달했다면?
    # 도착할 수 없음을 의미함
    return -1



# 데이터 입력
# row : N, col : M
N, M = map(int, input().split())
data = [list(map(int, input())) for _ in range(N)]
# print(data)   # [[1, 0, 1, 1, 1, 1], [1, 0, 1, 0, 1, 0], [1, 0, 1, 0, 1, 1], [1, 1, 1, 0, 1, 1]]

# 방문 표시를 할 것 -> 우리의 최종 목적 -> 해당 위치까지 도달하는데 걸린 비용이 얼만지 기록
distance = [[-1] * M for _ in range(N)]
# print(distance)  # [[-1, -1, -1, -1, -1, -1], [-1, -1, -1, -1, -1, -1], [-1, -1, -1, -1, -1, -1], [-1, -1, -1, -1, -1, -1]]

get_road_move_time(0, 0)
print(distance[N-1][M-1])
for dis in distance:
    print(*dis)