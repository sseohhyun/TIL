def dfs(num_list, depth):
    global max_num

    # 종료 조건
    if depth == N:
        num_str = ''.join(num_list)
        max_num = max(max_num, int(num_str))
        return

    # 방문 체크
    key = (''.join(num_list), depth)
    if key in visited:
        return
    visited.add(key)

    # 모든 가능한 교환 시도
    for i in range(len(num_list)):
        for j in range(i+1, len(num_list)):
            num_list[i], num_list[j] = num_list[j], num_list[i]  # swap
            dfs(num_list, depth+1)
            num_list[i], num_list[j] = num_list[j], num_list[i]  # 원복


T = int(input())
for tc in range(1, T+1):
    num, N = input().split()
    N = int(N)
    num_list = list(num)

    max_num = 0
    visited = set()
    dfs(num_list, 0)

    print(f"#{tc} {max_num}")
