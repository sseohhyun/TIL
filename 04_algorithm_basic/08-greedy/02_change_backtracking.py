# 사용 예시
coins = [1, 5, 10, 50, 100, 400, 500]  # 동전 종류
change = 882  # 잔돈

result = get_minimum_coins_backtrack(coins, change)
for coin, count in result.items():
    if count > 0:
        print(f"{coin}원: {count}개")
    