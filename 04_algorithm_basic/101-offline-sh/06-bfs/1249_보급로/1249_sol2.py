'''
6
011001
010100
010011
101001
010101
111010
'''

di = [ -1, 1, 0, 0]
dj = [0, 0, -1, 1]

def dfs(arr, row, col):
    case = arr[row][col]

    if row == N and col == N:
        result.append(case)
        return result

    for d in range(4):
        if 0 <= row + di[d] < N and 0 <= col + dj[d] < N:
            case += dfs(arr, row + di[d], col + dj[d])

import sys
sys.stdin = open("input_1249.txt", "r")

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    depth = [list(map(int, input())) for _ in range(N)]

    result = []
    result_list = dfs(depth, 0, 0)
    min_case = min(result_list)
    print(min_case)

    # print(f'#{tc} {dfs(N, 0, 0)}')