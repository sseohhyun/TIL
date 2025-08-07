import sys
sys.stdin = open("sample_input_5215.txt", "r")

def dfs(idx, arr, like_sum, kcal_sum):
    global max_sum

    if kcal_sum > L:  # 제한 칼로리 초과 시 종료
        return

    if idx == N:    # 끝까지 도달 했다면, max_sum과 지금까지 계산한 like_sum을 비교해서 max 값 반환
        max_sum = max(max_sum, like_sum)
        return

    dfs(idx + 1, arr, like_sum + arr[idx][0], kcal_sum + arr[idx][1])     # 선택한 경우
    dfs(idx + 1, arr, like_sum, kcal_sum)       # 선택하지 않는 경우


T = int(input())
for tc in range(1, T+1):
    # N : 재료의 수, L : 제한 칼로리
    N, L = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]

    max_sum = 0

    dfs(0, arr, 0, 0)
    print(f'#{tc} {max_sum}')
'''
import sys
sys.stdin = open('sample_input_5215.txt')

from itertools import combinations

T = int(input())    # 테스트 케이스 수
for t in range(1, T+1):
    N, L = map(int, input().split())
    scores = []     # 재료에 대한 점수 담을 리스트
    cals = []   # 해당 재료의 칼로리를 담을 리스트

    for _ in range(N):  # 점수, 칼로리 입력
        temp = list(map(int, input().split()))
        scores.append(temp[0])
        cals.append(temp[1])

    print("scores:", scores)
    print("cals:", cals)

    max_score = 0   # max_score 낮은 값으로 미리 설정
    for r in range(1, N+1):     # 뽑을 갯수
        for comb in combinations(range(N), r):
            print("scores와 cals에서 뽑을 인덱스:",comb)
            total_score = sum(scores[i] for i in comb)
            total_cal = sum(cals[i] for i in comb)
            if total_cal <= L:
                max_score = max(max_score, total_score)

    print(f"#{t} {max_score}")
'''