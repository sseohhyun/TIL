"""
기본적인 서로소 집합 자료구조
- 각 집합은 트리 형태로 표현
- parent[i] = j는 'i의 부모는 j'를 의미
- 자기 자신이 부모인 경우 그 원소가 집합의 대표자
"""

def make_set(n):
    '''
        n : 집합을 만들 원소의 개수
    '''
    # 원소 개수 n을 입력받으면, 자기 자신을 대표자(부모)로 하는 배열 반환
    return [i for i in range(n+1)]


def find_set(x):
    '''
        원소 x가 속한 집합의 대표자가 누구인지 반환
    '''
    # 원소 x가 속한 집합의 대표자가 자기 자신이면
    if x == parent[x]:   # 원소 x가 속한 집합의 대표자
        return parent[x]
    # 아니야!
    # x의 대표자로 지정된 원소의 대표자가 누군지 찾음
    return find_set(parent[x])


def union(x, y):
    '''
        x, x : 합쳐질 두 집합의 원소
        유니온 과정에 삽입 대상 원소는 그 원소의 집합의 대표자가 아닐 수 있음
    '''
    root_x = find_set(x)
    root_y = find_set(y)

    # 두 집합을 합침
    # 두 원소가 속한 집합의 대표자가 서로 다르다면
    if root_x != root_y:
    # 어떤한 기준을 토대로, 집합 x가 속한 집합의 대표자를 y로 바꾸거나
    # 원소 y가 속한 집합의 대표자를 x로 바꾸거나
        parent[root_y] = root_x

    # 두 원소가 속한 집합의 대표자가 서로 같다면
    # 두 원소의 대표자가 같으면 이미 원래 두 원소는 같은 집합 소속임

# 각 원소들이 가지고 있는 값이 중요하다면,
# 각 원소들이 가진 값들을 부모 정보를 기입할 배열과 동일한 크기로 미리 작성
#      0    1    2    3    4    5    6
tree = [0, 'a', 'b', 'c', 'd', 'e', 'f']
# 6개의 원소로 테스트
parent = make_set(6)
print(f"초기 상태: {parent}")

# 긴 트리를 만들어 비효율성 확인
union(5, 6)
print(f"5와 6 합치기 연산 후 상태: {parent}")
union(4, 5)
print(f"4와 5 합치기 연산 후 상태: {parent}")
union(3, 4)
print(f"3와 4 합치기 연산 후 상태: {parent}")
union(2, 3)
print(f"2와 3 합치기 연산 후 상태: {parent}")
union(1, 2)
print(f"1와 2 합치기 연산 후 상태: {parent}")