import sys
sys.stdin = open("sample_input_4008.txt", "r")

def dfs(idx, calc):
    global max_calc
    global min_calc

    if idx == N:    # N개의 카드를 모두 조사했으면 종료
        min_calc = min(min_calc, calc)
        max_calc = max(max_calc, calc)
        return

    for i in range(sum(calc_list)):
        dfs(idx+1, calc )


T = int(input())
for tc in range(1, T+1):
    N = int(input())    # 숫자 카드 개수
    calc_list = map(int, input().split())
    num = map(int, input().split())

    max_calc = 100,000,000      # 최대값 초기화
    min_calc = -100,000,000     # 최소값 초기화

    dfs(0, 0)

    print(f'#{tc} {max_calc - min_calc}')