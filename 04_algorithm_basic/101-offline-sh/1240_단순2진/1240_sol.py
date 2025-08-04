import sys
sys.stdin = open("input_1240.txt", "r")

T = int(input())

for t_c in range(1, T+1):
    n, m = map(int, input().split())
    arr = [input().strip() for _ in range(n)]

    code = {
        "0001101": "0",
        "0011001": "1",
        "0010011": "2",
        "0111101": "3",
        "0100011": "4",
        "0110001": "5",
        "0101111": "6",
        "0111011": "7",
        "0110111": "8",
        "0001011": "9"
    }

    found = False # 2중 루프 탈출용

    for i in range(n):
        for j in range(m-1,-1,-1):
            if arr[i][j] == "1":
                code_str = arr[i][j-55:j+1]
                code_str = "".join(code_str)
                found = True
                break
        if found:
            break

    decode = []
    for idx in range(0,56,7):
        code_num = int(code[code_str[idx:idx+7]])
        decode.append(code_num)

    odd = sum(decode[i] for i in range(0,len(decode),2))
    even = sum(decode[i] for i in range(1,len(decode),2))

    if (odd*3 + even)%10 == 0:
        result = sum(decode)
    else:
        result = 0

    print(f'#{t_c} {result}')