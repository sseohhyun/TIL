def fractional_knapsack_greedy(capacity, items):
    '''
    # 무게 당 가격이 얼만지를 우선 구함
    # 가성비 따져서 넣을거라서
    items[1] / items[0]     # 무게 당 가격을 구함
    # 그 후에 그 무게당 가격이 가장 높은 대상을 먼저 사용함
    가성비 = []
    for item in items:
        무게당가격 = items[1] / items[0]
        가성비.append(무게당가격)
    가성비.sort(reverse=True)
    '''
    items.sort(key=lambda x:x[1]/x[0], reverse=True)
    result = 0
    remain_capacity = capacity

    # 가성비 높은 순으로 정렬되었으니, 차례대로 순회
    for weight, value in items:
        if remain_capacity <= 0:    # 남아 있는 무게가 없으면 종료
            break

        # 내 현재 물건을 전체 담을 수 있을 수 있는 경우
        if remain_capacity >= weight:
            remain_capacity -= weight
            result += value
        # 나눠서 담아야 하는 경우
        else:
            fraction = remain_capacity / weight
            result += value * fraction
            remain_capacity = 0
    return result

capacity = 30  # 배낭의 최대 무게
items = [(5, 50), (10, 60), (20, 140)] # (무게, 가치)
result = fractional_knapsack_greedy(capacity, items)
print(f"최대 가치: {result}")