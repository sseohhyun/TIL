import sys
sys.stdin = open("sample_input_5258.txt")

def pack(size, price, max_size):
    K = [[0 for _ in range(max_size + 1)] for _ in range(M + 1)]

    for i in range(1, M+1):
        for s in range(1, max_size + 1):
            if size[i-1] > s:
                K[i][s] = K[i-1][s]
            else:
                K[i][s] = max(price[i-1] + K[i-1][s-size[i-1]], K[i-1][s])

    return K[M][max_size]


T = int(input())
for tc in range(1, T+1):
    max_size, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(M)]

    zip_arr = list(zip(*arr))
    size = zip_arr[0]
    price = zip_arr[1]

    max_value = pack(size, price, max_size)

    print(f'#{tc} {max_value}')