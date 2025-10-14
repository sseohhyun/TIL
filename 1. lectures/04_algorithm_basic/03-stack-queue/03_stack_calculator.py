def infix_to_postfix(expression):
    # 연산자의 우선순위를 정의
    op_dict = {'+': 1, '-': 1, '*': 2, '/': 2, '(': 0}
    stack = []  # 연산자를 저장할 스택
    postfix = []    # 후위 표기식을 저장할 리스트

    for char in expression: # 표현식 순회
        # 피연산자인 경우
        if char.isnumeric():    # 정수라면
            postfix.append(char)    # 후위표기식에 삽입
        elif char == '(':
            stack.append(char)
        elif char == ')':
            top_token = stack.pop() # 연산자들을 스택에서 빼는데..
            while top_token != '(': # 여는 소괄호를 만날떄까지
                postfix.append(top_token)
                top_token = stack.pop()
        else:   # 연산자인 경우
            # 스택에 있는 연산자들이 지금 검사하는 연산자보다
            # 우선순위가 높거나 낮을때 서로 다르게 처리해야한다.
            while stack and op_dict[stack[-1]] >= op_dict[char]:
                postfix.append(stack.pop())
            stack.append(char)
    while stack:
        postfix.append(stack.pop())

    return ' '.join(postfix)

# 후위 표기식 계산 함수 
def run_calculator(expr):
    stack = []
    for token in expr.split():
        if token.isnumeric():  # 피연산자
            stack.append(int(token))
        else:  # 연산자
            b = stack.pop()
            a = stack.pop()
            if token == '+':
                stack.append(a + b)
            elif token == '-':
                stack.append(a - b)
            elif token == '*':
                stack.append(a * b)
            elif token == '/':
                stack.append(a // b)  # 정수 나눗셈
    return stack[0]  # 최종 결과

# 예시
infix_expression = "3+(2*5)-8/4"

# 중위 표기식을 후위 표기식으로 변환
postfix_expression = infix_to_postfix(infix_expression)
print(f"후위 표기식: {postfix_expression}")     # 결과 확인

# 후위 표기식을 계산
result = run_calculator(postfix_expression)
print(result)       # 결과 확인
