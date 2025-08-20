import sys
sys.stdin = open("sample_input_5248.txt")

def find_set(x):
    if x == parent[x]:
        return x
    parent[x] = find_set(parent[x])
    return parent[x]

def union(x, y):
    x_root = find_set(x)
    y_root = find_set(y)
    if x_root != y_root:
        parent[y_root] = x_root

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    lst = list(map(int, input().split()))

    parent = [i for i in range(N+1)]

    for i in range(0, len(lst), 2):
        union(lst[i], lst[i+1])

    for i in range(1, N+1):
        find_set(i)

    # print(parent)

    # 0을 제외한 서로 다른 숫자를 count 하기
    ans = len(set(parent[1:]))
    print(f'#{tc} {ans}')



