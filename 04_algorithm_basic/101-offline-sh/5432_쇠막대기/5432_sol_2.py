import sys
sys.stdin = open("sample_input_5432.txt", "r")

T = int(input())
for t_c in range(1, T+1):
    str = input()
    str_laser = str.replace("()", "l") # '()'를 l(laser)로 변경

    stack = []              # "("의 인덱스를 쌓을 리스트
    stick_count = 0         # 최종 쇠막대기 개수

    for i in range(len(str_laser)):
        if str_laser[i] == "(":       # "("를 만나면 stick_count를 1 증가시키고, stack에 쌓음
            stick_count += 1
            stack.append(i)

        elif str_laser[i] == "l":
            stick_count += len(stack)   # "l"을 만나면 "("가 쌓인 개수만큼 stick_count를 증가시킴

        else:    # "("를 만나면 ")"를 스택에서 빼냄
            start_index = stack.pop()

    print(f'#{t_c} {stick_count}')