arr =[1, 2, 3]
n = len(arr)
subsets = []
# 모든 경우의 수에 대해서 조회
# for idx in range(2**n):
for idx in range(1 << n):
    # 이번 경우의 수의 부분집합
    tmp_subset = []
    for j in range(n):  # j번째 요소가 이번 경우의 수에 사용되었는지 판별
        '''
            idx = 0    => 000
            j   = 0    => 001   & -> 0
            
            idx = 3    => 011 
            j   = 0    => 001   & -> True
            j   = 1    => 010   & -> True 
        '''
        if idx & (1 << j):
            # j번째 요소가 이번 경우의 수에 사용되었음

            tmp_subset.append(arr[j])
    # 필요 하다면, 이곳에 추가 조건을
    if sum(tmp_subset) == 3:
        subsets.append(tmp_subset)
print(subsets)