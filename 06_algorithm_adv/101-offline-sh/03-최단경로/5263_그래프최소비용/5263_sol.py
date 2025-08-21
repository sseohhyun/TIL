import sys
sys.stdin = open("sample_input_5263.txt")

def floyd_warshall(graph):
    for k_node in range(N):
        for start in range(N):
            for end in range(N):
                Dik = graph[start][k_node]
                Dkj = graph[k_node][end]
                Dij = graph[start][end]

                if Dik + Dkj < Dij:
                    graph[start][end] = Dik + Dkj
    return graph

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    adj_matrix = [list(map(int, input().split())) for _ in range(N)]

    # adj_matrix에서 i, j 값이 다른 경우 0일 때에 대해서 무한대로 바꾸기
    for i in range(N):
        for j in range(N):
            if i != j and adj_matrix[i][j] == 0:
                adj_matrix[i][j] = float('inf')

    result = floyd_warshall(adj_matrix)
    ans = max(map(max, result))
    print(f'#{tc} {ans}')
