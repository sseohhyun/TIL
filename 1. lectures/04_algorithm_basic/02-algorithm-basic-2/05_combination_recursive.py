def comb(arr, n):
   # 최종 결과값
   result = []
   if n == 1:  # 선택할 요소의 수가 1인 경우
      # n이 1이리마녀 더 이상 조합할 요소가 필요 없어진다.
      # 각 요소 자체가 하나의 조합이 된다.
      return [[i] for i in arr]

   # 배열의 모든 요소를 일단 순회
   for idx in range(len(arr)):
      # 요소 하나를 선택
      select_item = arr[idx]
      # 현재 선택한 그 요소 이후의 나머지 요소들
      # 즉, n-1 개의 요소들로 조합을 재귀로 다시 구성
      for rest in comb(arr[idx + 1:], n-1):
         result.append([select_item] + rest)

   return result

print(comb([1, 2, 3, 4], 3))  # [1, 2, 3], [1, 2, 4], [1, 3, 4], [2, 3, 4] 출력
