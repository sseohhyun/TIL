from itertools import permutations

def is_triplet(card):
    return card[0] == card[1] == card[2]

def is_run(card):
    return card[0] + 2 == card[1] + 1 == card[2]

import sys
sys.stdin = open("input_16546.txt", "r")

T = int(input())
for tc in range(1, T+1):
    lst = sorted(list(map(int, input())))

    for num_set in permutations(lst):
        if (is_triplet(num_set[:3]) or is_run(num_set[:3])) and (is_triplet(num_set[3:]) or is_run(num_set[3:])):
            result = "true"
            break
    else:
        result = "false"

    print(f'{tc} {result}')


