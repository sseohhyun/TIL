'''
2
12 10
1B3B3B81F75E
16 2
F53586D76286B2D8
'''

def makeset(char_list):
    global  chek_num_set

    for i in range(0, N, char_len):
        chek_num_set.add(char_list[i:i+char_len])

T = int(input())
for tc in range(1, T+1):
    N, K = list(map(int, input().split()))
    lst = input()   # 문자열 그대로 입력 받음

    char_len = N//4
    chek_num_set = set()

    # 기존 문자열에서 슬라이싱 후 set에 추가
    makeset(lst)

    for _ in range(char_len):
        lst = lst[-1] + lst[:-1]
        makeset(lst)

    # print("회전까지 하고 나서 모든 문자열 모음", chek_num_set)

    # 16진수를 10진수로 바꾸기
    change_16_num_set = []
    for num in chek_num_set:
        change_16_num_set.append(int(num, 16))
    # print("10진수로 바꾸고 나서 값 모음", change_16_num_set)

    # 정렬
    sort_set = sorted(change_16_num_set, reverse=True)
    # print("이건 10진수로 바꾼거 정렬한거 :", sort_set)
    print(f'#{tc} {sort_set[K-1]}')