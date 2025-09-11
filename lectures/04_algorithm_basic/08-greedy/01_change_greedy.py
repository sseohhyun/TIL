'''
    거스름돈 문제 그리디로 해결
    가장 큰 거스름돈을 먼저 거슬러주고, 남은 금액을 다음 단위로 해결
'''

def get_minimum_coins(coins, change):
    # 어떤 동전이 몇 개 사용되었는가?
    result = {}
    # 가장 큰 코인부터 coins에서 빼나갈 것임 -> 오름차순
    coins.sort(reverse=True)

    # 코인 종류별로 change에서 제거
    for coin in coins:
        count = 0 # 몇 번 뺐는지 알아야 함
        while change >= coin: # 뺄 수 있으면
            change -= coin
            count += 1
            result[coin] = count
    return result

def get_minimum_coins_backtrack(coins, change):
    coins.sort(reverse=True)
    min_coins = change      # 최소 동전 개수
    result = {}     # 최적의 조건을 모은 result

    def backtrack(remain, target, curr_comb, acc):
        nonlocal min_coins, result
        """
            remain: 0으로 만들어야 하는 남은 금액
            target: 현재 어느 동전을 사용할 것이냐 index
            curr_comb: 지금까지 만들어진 조합
            acc: 지금까지 사용한 동전의 개수
        """
        # 기저 조건: 남은 금액x
        if remain == 0:
            if acc < min_coins:     # 내 누적값이 min_coins보다 작을 때만
                min_coins = acc     # 최솟값 갱신
                # curr_comb -> 딕셔너리 형태 (참조형)
                result = dict(curr_comb)
            return

        # 가지치기
        if acc >= min_coins:
            return

        # 유도 조건: 남은 동전들에 대해서 모두 시도
        for idx in range(target, len(coins)):
            coin = coins[idx]
            if coin <= remain:
                # 여기서 만큼은 그리디하게 생각했을 때,
                # 100원을 1,2,3번 반복 조사는 의미 없음
                max_count = remain // coin
                curr_comb[coin] = max_count
                backtrack(remain - coin * max_count, idx + 1, curr_comb, acc + max_count)
                curr_comb[coin] = 0
    backtrack(change, 0, {}, 0)
    return result

# coins = [1, 5, 10, 50, 100, 500]  # 동전 종류
# change = 882  # 잔돈

# 아래의 경우라면 어떨까?
coins = [1, 5, 10, 50, 100, 400, 500]  # 동전 종류
change = 882  # 잔돈

result = get_minimum_coins_backtrack(coins, change)
for coin, count in result.items():
    print(f"{coin}원: {count}개")
