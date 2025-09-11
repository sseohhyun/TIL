di = [-1, 1, 0, 0]
dj = [0, 0, -1, 1]

def dfs(r, c, arr, long, num_str):

    if long == 7:
        result.add(num_str)
        return

    for d in range(4):
        ni, nj = r + di[d], c + dj[d]
        if 0 <= ni < 4 and 0 <= nj < 4:
            dfs(ni, nj, arr, long + 1, num_str + arr[ni][nj])


import sys
sys.stdin = open("sample_input_2819.txt")

T = int(input())
for tc in range(1, T+1):
    arr = [list(input().split()) for _ in range(4)]

    result = set()

    for i in range(4):
        for j in range(4):
            dfs(i, j, arr, 1, arr[i][j])
    ans = len(result)

    print(f'#{tc} {ans}')