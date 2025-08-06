import sys
sys.stdin = open("sample_input_2819.txt", "r")

# 상하좌우 배열 설정
di = [-1, 1, 0, 0]
dj = [0, 0, -1, 1]

def dfs(r, c, path):
    if len(path) == 7:  # 문자열의 길이가 7인 경우 dfs 종료함
        num_set.add(path)   # 숫자 조합 set에 추가하기
        return

    for d in range(4):
        ni, nj = r + di[d], c + dj[d]
        if 0 <= ni < N and 0 <= nj < N:     # 다음 인덱스의 위치가 범위안에 있다면
            dfs(ni, nj, path + arr[ni][nj]) # dfs 함수를 다음 위치로 돌리기

T = int(input())
N = 4

for tc in range(1, T+1):
    arr = [list(map(str, input().split())) for _ in range(4)]

    num_set = set()     # 만들어지는 숫자 조합을 담을 set

    for i in range(N):
        for j in range(N):
            dfs(i, j, arr[i][j])

    print(f'#{tc} {len(num_set)}')