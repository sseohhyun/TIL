import heapq

numbers = [10, 1, 5, 3, 8, 7, 4]  # 초기 리스트

# 리스트를 최소 힙으로 변환
heapq.heapify(numbers)
print(numbers)      # [1, 3, 4, 10, 8, 7, 5]

heapq.heappush(numbers, -1)
print(numbers)      # [-1, 1, 4, 3, 8, 7, 5, 10]

smallest = heapq.heappop(numbers)
print(smallest)     # -1
print(numbers)      # [1, 3, 4, 10, 8, 7, 5]


# 주의사항
# heap으로 만든 numbers를 리스트처럼 그냥 append 하면 곤란함
numbers.append(-1)
print(numbers)