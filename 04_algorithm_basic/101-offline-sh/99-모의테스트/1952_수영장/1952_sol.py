def dfs(idx, hap):
    global vs_month3_price, min_price

    if idx >= 12:
        if min_price > hap:
            min_price = hap
        return

    # 3달치 가격을 선택한 경우
    dfs(idx+3, hap + month3)

    # 1일치, 1달이 비교된 가격을 선택한 겨애우
    dfs(idx+1, hap + vs_month3_price[idx])

import sys
sys.stdin = open("sample_input_1952.txt")

T = int(input())
for tc in range(1, T+1):
    day1, month1, month3, year1 = list(map(int, input().split()))
    swim = list(map(int, input().split()))

    # day_1, month_1 가격 비교 후 더 적은 금액으로 리스트에 삽입하기
    day1_vs_month1_price = [0] * 12
    for i in range(12):
        if swim[i] * day1 <= month1:     # 1일치 가격보다 1달 가격이 더 비싼 경우
            day1_vs_month1_price[i] = swim[i] * day1    # 1일치 가격으로 리스트에 삽입
        else:
            day1_vs_month1_price[i] = month1    # 반대의 경우 한달치 가격으로 리스트에 삽입

    # print(day1_vs_month1_price)   [0, 0, 20, 40, 10, 40, 0, 0, 0, 0, 0, 0]

    # 3달치 가격과 비교하기
    vs_month3_price = day1_vs_month1_price[:]       # 이전 리스트 복사해서 사용
    min_price = float('inf')
    dfs(0, 0)

    # 1년 가격과 (1일,1달,3달) 비교해서 합한 가격을 비교
    if year1 < min_price:
        min_price = year1

    print(f'#{tc} {min_price}')