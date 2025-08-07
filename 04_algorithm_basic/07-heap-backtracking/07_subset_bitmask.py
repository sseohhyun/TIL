nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
target_sum = 10
result = []
n = len(nums)

for i in range(1 << n):
    current_subset = []
    current_sum = 0
    for j in range(10):
        if i & (1 << j):
            current_subset.append(nums[j])
            current_sum += nums[j]
        if current_sum > target_sum:
            break
    if current_sum == target_sum:
        result.append(current_subset)
print(result)