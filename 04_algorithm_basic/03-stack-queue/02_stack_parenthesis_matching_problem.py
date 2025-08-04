def check_match(expression):
    # 여는 괄호들을 일단 담아둘 스택
    stack = []
    # 괄호의 짝을 매칭시킬수 있어야 할 것 같은데...
    matching_dict = {
        ')': '(',
        '}': '{',
        ']': '['
    }
    for char in expression:
        # 여는 괄호니?
        if char in matching_dict.values():  # ['(', '{', '[']
            # 네. stack에 넣어 주세요.
            stack.append(char)
        # 닫는 괄호니?
        elif char in matching_dict.keys():
            # 닫는 괄호면 무엇을 해야하나?
            # 스택에서 나와 매칭되는 짝을 찾을 수 있다면, 그 괄호를 제거
            # 단, 스택이 비어있지 않다면!
                # 스택이 비었거나, 마지막 요소의 값이 내가 찾는 여는괄호가 아니면
            if not stack or stack[-1] != matching_dict[char]:
                return False    # 실패
            # 위에서 성공해서 이곳으로 왔다면?
            stack.pop()
    # 모든 문자를 다 순회하고, 이곳에 도달했다면....
    return not stack
# 예시
examples = ["(a(b)", "a(b)c)", "a{b(c[d]e}f)"]
for ex in examples:
    if check_match(ex): 
        print(f"{ex} 는 올바른 괄호") 
    else:
        print(f"{ex} 는 올바르지 않은 괄호")  
