import sys
sys.stdin = open("input_1263.txt")

'''
2
3 0 1 0 1 0 1 0 1 0
4 0 0 1 0 0 0 1 0 1 1 0 1 0 0 1 0
'''
def floyd_warshall(graph):
    for k_node in range(N):
        for start in range(N):
            for end in range(N):
                dij = graph[start][end]
                dik = graph[start][k_node]
                dkj = graph[k_node][end]

                if dik + dkj < dij:
                    graph[start][end] = dik + dkj
    return graph

T = int(input())
for tc in range(1, T+1):
    N, *lst = list(map(int, input().split()))
    adj_matrix = []
    for i in range(0, len(lst), N):
        adj_matrix.append(lst[i:i+N])
    INF = float('inf')

    for i in range(N):
        for j in range(N):
            if i != j and adj_matrix[i][j] == 0:
                adj_matrix[i][j] = INF

    result = floyd_warshall(adj_matrix)
    ans = min(map(sum, result))

    print(f'#{tc} {ans}')