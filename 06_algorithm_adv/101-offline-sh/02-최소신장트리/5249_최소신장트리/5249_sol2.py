import sys
sys.stdin = open("sample_input_5249.txt")

class Disjointset:
    # 초기 설정
    def __init__(self, v):
        self.p = [0] * (len(v) + 1)
        self.rank = [0] * (len(v) + 1)
    def make_set(self, x):
        self.p[x] = x
        self.rank[x] = 0

    # 계산 함수
    def find_set(self, x):
        if x != self.p[x]:
            self.p[x] = self.find_set(self.p[x])
        return self.p[x]

    def union(self, x, y):
        px = self.find_set(x)
        py = self.find_set(y)

        if px != py:
            if self.rank[px] < self.rank[py]:
                self.p[px] = py
            elif self.rank[px] > self.rank[py]:
                self.p[py] = px
            else:
                self.p[py] = px
                self.rank[px] += 1
def mst_kruskal(vertices, edges):
    mst = []
    edges.sort(key = lambda x: x[2])
    ds = Disjointset(vertices)
    for i in range(len(vertices) + 1):
        ds.make_set(i)
    for edge in edges:
        s, e, w = edge
        if ds.find_set(s) != ds.find_set(e):
            ds.union(s, e)
            mst.append(w)
    return mst

T = int(input())
for tc in range(1, T+1):
    V, E = map(int, input().split())
    vertices = [i for i in range(V+1)]
    edges = [list(map(int, input().split())) for _ in range(E)]

    result = mst_kruskal(vertices, edges)
    print(f'#{tc} {sum(result)}')