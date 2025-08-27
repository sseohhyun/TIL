"""
경로 압축(Path Compression) + 랭크 기반 Union(Union by Rank)
두 최적화 기법을 모두 적용하여 거의 상수 시간 O(α(N))에 가까운 효율을 달성
실제 알고리즘 문제에서 사용하는 최종 버전
"""

# 전역 변수로 선언하여 find_set과 union 함수에서 접근 가능하도록 함
# 전역 변수가 아닌 클래스 내부에 정의하는 것이 더 좋은 설계입니다.
parent = []
rank = []


def make_set(n):
    """부모와 랭크 리스트 초기화"""
    global parent, rank
    # 인덱스 0은 사용하지 않고 1부터 n까지 사용하기 위해 n+1 크기로 생성
    parent = [i for i in range(n + 1)]
    # 랭크(트리의 높이) 초기값은 모두 0
    rank = [0] * (n + 1)
    # 별도 반환 없이 전역 변수를 바로 사용


def find_set(x):
    """경로 압축이 적용된 find_set"""
    # 현재 노드 x가 대표자(자신이 부모)가 아니면
    if x != parent[x]:
        # 재귀적으로 대표자를 찾아 올라가면서
        # 그 과정에 만나는 모든 노드의 부모를 최종 대표자로 직접 연결
        parent[x] = find_set(parent[x])
    return parent[x]


def union(x, y):
    """랭크 기반으로 최적화된 union"""
    root_x = find_set(x)
    root_y = find_set(y)

    # 두 원소의 대표자가 서로 다르면 합치기
    if root_x != root_y:
        # 1. 랭크가 더 높은 트리에 낮은 트리를 합침
        if rank[root_x] > rank[root_y]:
            parent[root_y] = root_x
        elif rank[root_x] < rank[root_y]:
            parent[root_x] = root_y
        # 2. 랭크가 같으면 아무 트리에나 합치고, 합쳐진 새 트리의 랭크를 1 증가
        else:
            parent[root_y] = root_x
            rank[root_x] += 1


# 주어진 대로 테스트 실행
make_set(6)
edges = [(1, 2), (2, 3), (4, 5), (5, 6), (3, 4)]

for i, (u, v) in enumerate(edges):
    union(u, v)

print(f"최종 parent: {parent}")
print(f"최종 rank: {rank}")