# 완전 이진 트리 기준 순회
# 완전 이진 트리일 때 N = 5 라면 5까지 돌면됨

# 전위 순회
def preorder_traversal(idx):
    # 어디까지 순회해야 함?
    # 순회 대사가 범위를 벗어나지 않았다면
    if idx <= N:
        # 전위 순회는 부모 노드를 먼저 조사함
        print(tree[idx], end=" ")
        # 이제 왼쪽 서브 트리에 대해서도 동일한 조건
        preorder_traversal(idx * 2) # A, B, D 돌고 8번 인덱스까지 늘어나나, if문 통과x
        # 이제 오른쪽 서브 트리에 대해서도 동일한 조건
        preorder_traversal(idx * 2 + 1)  # 9번 인덱스 if문 통과 x -> 5로 돌아감

# 중위 순회
def inorder_traversal(idx):
    '''
        중위 순회란, 부모 노드 찰계가 중간인 순회 방식
        즉, 왼쪽 서브 트리에 대한 처리가 우선되어야 함
        (8번까지 가서 확인함 -> 조건 만족x, 없음 출력x -> 돌아와서 D가 출력
         -> 9번 확인 -> 없음 -> ...)
    '''
    if idx <= N:
        # 이제 왼쪽 서브 트리에 대해서도 동일한 조건
        inorder_traversal(idx * 2)
        # 중위 순회는 왼쪽 서브트리 순회 후에 조사함
        print(tree[idx], end=" ")
        # 이제 오른쪽 서브 트리에 대해서도 동일한 조건
        inorder_traversal(idx * 2 + 1)

# 후위 순회
def postorder_traversal(idx):
    if idx <= N:
        # 이제 왼쪽 서브 트리에 대해서도 동일한 조건
        postorder_traversal(idx * 2)
        # 이제 오른쪽 서브 트리에 대해서도 동일한 조건
        postorder_traversal(idx * 2 + 1)
        # 중위 순회는 왼쪽 서브트리 순회 후에 조사함
        print(tree[idx], end=" ")

N = 5
tree = [0, 'A', 'B', 'C', 'D', 'E']


'''
    트리 구조
        'A'
      /   \
   'B'    'C'
  /   \
'D'    'E'
'''

print('전위 순회')
# 트리를 배열 형태로 만듦 -> 그 인덱스를 각 노드의 값이 삽입된 위치로 봄
# 루트 노드에 해당하는 1번 인덱스부터 조회를 시작함
preorder_traversal(1)  # 'A' 'B' 'D' 'E' 'C'
print()
print('중위 순회')
inorder_traversal(1)  # 'D' 'B' 'E' 'A' 'C'
print()
print('후위 순회')
postorder_traversal(1)  # 'D' 'E' 'B' 'C''A'