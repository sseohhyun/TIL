import sys
sys.stdin = open("sample_input_5432.txt", "r")

T = int(input())
for t_c in range(1, T+1):
    str = input()
    str_laser = str.replace("()", "l") # '()'를 l(laser)로 변경

    stack = []              # "("의 인덱스를 쌓을 리스트
    brackets_open = "("
    brackets_close = ")"
    final_cut_count = 0     # 최종 쇠막대기 개수

    def check_leser_count(start, end):      # 괄호 안에 laser의 개수를 세는 함수
        laser_count = 0
        for index in range(start, end+1):   # 괄호 안에만 반복문으로 돌면서 확인
            if str_laser[index] == "l":     # 괄호 안에 만약 "l"이 있으면 1을 카운트
                laser_count += 1
        cut_count = laser_count + 1         # 막대기 개수는 레이저 개수보다 한개 더 많으므로 cut_count 변수 생성
        return cut_count

    for i in range(len(str_laser)):
        if str_laser[i] == brackets_open:       # "("에 해당하는 인덱스를 스택에 쌓음
            stack.append(i)

        elif str_laser[i] == brackets_close:    # ")"를 만나면,
            start_index = stack.pop()           # 스택에서 맨 위의 인덱스를 빼서 괄호 시작 인덱스(start_index)에 할당
            end_index = i                       # ")"에 해당하는 현재 인덱스를 괄호 끝 인덱스(end_index)에 할당
            final_cut_count += check_leser_count(start_index, end_index)    # 구한 인덱스를 바탕으로 레이저의 개수를 세는 함수를 돌림

    print(f'#{t_c} {final_cut_count}')




