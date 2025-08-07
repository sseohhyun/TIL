import sys
sys.stdin = open("sample_input_2930.txt", "r")

import heapq


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    max_heap = []
    ans = []

    for lst in arr:
        if lst[0] == 1:
            heapq.heappush(max_heap, -lst[1])

        elif lst[0] == 2:
            if len(max_heap) != 0:
                largest = -heapq.heappop(max_heap)
                ans.append(largest)
            else :
                ans.append(-1)

    print(f'#{tc}', *ans)

