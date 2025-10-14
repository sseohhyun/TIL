import sys
sys.stdin = open("sample_input_4008.txt", "r")

def dfs(idx, calc_idx, ):
    global max_calc
    global min_calc

    if calc_idx == 0 :
        num[idx] + dfs(idx+1 ,,)
    elif calc_idx == 1:
        num[idx] - dfs(idx+1, )
    elif calc_idx == 2 :
CRE        num[idx] * dfs(idx+1, )
    elif calc_idx == 3 :
        num[idx] // dfs(idx+1, ,)


T = int(input())
for tc in range(1, T+1):
    N = int(input())    # 숫자 카드 개수
    calc_list = map(int, input().split())
    num = map(int, input().split())

    max_calc = 100,000,000      # 최대값 초기화
    min_calc = -100,000,000     # 최소값 초기화

    dfs(0, 0)

    print(f'#{tc} {max_calc - min_calc}')