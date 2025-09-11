import sys
sys.stdin = open("sample_input_5215.txt", "r")

def dfs(idx, kcal_sum, like_sum, visited):
    global like_sum_list

    if L < kcal_sum:        # 제한 칼로리를 초과한 경우
        return
    if idx == N :           # 주어진 케이스를 모두 선택한 경우
        return

    if kcal_sum <= L:       ### L보다 "작거나 같기만" 즉시 max_sum을 업데이트하고 종료해서 안됨.. ###
        like_sum_list.add(like_sum)
        return

    visited[idx] = 1
    dfs(idx+1, kcal_sum + arr[idx][1], like_sum + arr[idx][0], visited)
    visited[idx] = 0

T = int(input())
for tc in range(1, T+1):
    # N : 재료의 수, L : 제한 칼로리
    N, L = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]

    visited = [0] * N   # 방문 처리를 하기 위한 리스트
    like_sum_list = set()      # 칼로리의 누적합을 쌓기 위한 리스트

    dfs(0, 0, 0, visited)
    max_like_sum = max(like_sum_list)
    print(max_like_sum)