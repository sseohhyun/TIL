def inorder(idx):
    if idx <= N:
        inorder(idx * 2)
        inorder_idx.append(tree[idx])
        inorder(idx * 2 + 1)

import sys
sys.stdin = open("sample_input_5176.txt")

T = int(input())
for tc in range(1, T+1):
    N = int(input())

    tree = [i for i in range(N+1)]
    inorder_idx = []
    inorder(1)

    for i in range(len(inorder_idx)):
        tree[inorder_idx[i]] = i + 1

    print(f'#{tc} {tree[1]} {tree[N//2]}')
