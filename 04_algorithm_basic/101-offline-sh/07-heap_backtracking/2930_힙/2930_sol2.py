import sys
sys.stdin = open("sample_input_2930.txt", "r")

class MaxHeap:
    def __init__(self):
        self.heap = []  # 힙을 저장할 빈 리스트 초기화
        self.length = 0  # 힙의 길이 초기화

    # 힙에 새로운 요소를 추가
    def heappush(self, item):
        self.heap.append(item)  # 새로운 요소를 리스트의 끝에 추가
        self.length += 1  # 힙의 길이 증가
        self._siftup(self.length - 1)  # 가장 마지막에 삽입된 요소의 index를 넘김

    def _siftup(self, idx):
        parent = (idx -1) //2
        while idx > 0 and self.heap[idx] > self.heap[parent]:
            self.heap[idx], self.heap[parent] = self.heap[parent], self.heap[idx]
            idx = parent
            parent = (idx - 1) // 2

    # 힙에서 최대 요소를 제거하고 반환
    def heappop(self):
        if self.length == 0:
            return -1
        if self.length == 1:
            self.length -= 1
            return self.heap.pop()

        root = self.heap[0]
        self.heap[0] = self.heap.pop()
        self.length -= 1
        self._siftdown(0)
        return root

    def _siftdown(self, idx):
        largest = idx
        left = 2 * idx + 1
        right = 2 * idx + 2

        if left < self.length and self.heap[left] > self.heap[largest]:
            largest = left
        if right < self.length and self.heap[right] > self.heap[largest]:
            largest = right
        if largest != idx:
            self.heap[largest], self.heap[idx] = self.heap[idx], self.heap[largest]
            self._siftdown(largest)


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    max_heap = MaxHeap()
    result = []

    for lst in arr:
        if lst[0] == 1:
            max_heap.heappush(lst[1])
        elif lst[0] == 2:
            result.append(max_heap.heappop())

    print(f'#{tc}', *result)
