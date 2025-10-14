import sys
sys.stdin = open("input_1248.txt")

def find_parent(node):
    result = []
    while True:
        if node == 1:
            break
        parent_node = parent[node]
        result.append(parent_node)
        node = parent_node
    return result

def count_child(node):
    cnt = 1
    for child in child_dct[node]:
        cnt += count_child(child)
    return cnt

T = int(input())
for tc in range(1, T+1):
    V, E, node_a, node_b = map(int, input().split())
    edges = list(map(int, input().split()))

    parent = [None] * (V+1)
    child_dct = {i: [] for i in range(1, V+1)}

    for i in range(0, len(edges), 2):
        parent[edges[i+1]] = edges[i]
        child_dct[edges[i]].append(edges[i+1])

    node_a_parent = find_parent(node_a)
    node_b_parent = find_parent(node_b)
    common_parent = next(x for x in node_a_parent if x in node_b_parent)

    count_tree = count_child(common_parent)

    print(f"#{tc} {common_parent} {count_tree}")
