'''
    LEGB rule에 대한 설명
        - 파이썬에서 내가 찾고자 하는 대상을 탐색하는 순서
        - local
        - enclosing
        - global
        - built-in
    LEGB를 사용하다보면 쉽게 헷갈릴 수 있는 이야기들...
'''

statement = "안녕하세요"

def some():
    # local 영역에서 statement 변수를 찾으려고 시도합니다.
    # 만약 local 영역에 없다면, enclosing 영역(여기서는 global)에서 찾습니다.
    return statement

print(some())

def some2():
    return max

print(some2())
print(max(1, 2, 3)) # 파이썬 기본 내장함수 max는 넘겨받은 값들 중 가장 큰 값을 반환

# def some3():
#     # NameError: name 'nothing' is not defined
#     return nothing

# print(some3())

def some4():
    # 함수 내부 local 영역에서 statement 변수에 값을 직접 할당 한것
    statenment = "안녕히가세요"
    return statenment

print(some4())
print(statement)  # 여전히 global 영역의 statement 변수는 "안녕하세요"입니다.

global_statement = "전역변수"

def some5():
    # global 키워드를 사용하여 전역변수에 접근합니다.
    # 자, 나는 이곳에서 전역변수 global_statement를 사용하겠다고 선언합니다.
    global global_statement     
    '''
        단, 항상 주의 하여야 한다.
        특정 함수에서 global 키워드를 사용하여 전역 변수를 바꾼다는 행위는
        다른 함수나, 나른 수식에서 해당하는 전역변수를 사용할때
        예기치 못한 상황을 발생 시킬 수 있다!
    '''

    global_statement = "전역변수 변경"
    return global_statement
print(some5())
print(global_statement)  # 이제 global_statement는 "전역변수 변경"입니다.

def some6(word):
    print(word, '| 함수 내부에서 출력')
    word = "여기서 이렇게 값을 변경"
    return word

print(some6(global_statement))  
# 이 함수 some6을 통해서 넘겨줬던 인자가 some6에 의해 변경된 뒤에
# 그 변경된 값을 다시 global_statement에 할당한다면...
global_statement = some6(global_statement)
print(global_statement)  # 이제 global_statement는 "여기서 이렇게 값을 변경"입니다.

arr = [1, 2, 3]
def some7():
    # 리스트는 mutable(변경 가능한) 객체입니다.
    # ? local에서 글로벌에 있는 값 변경 안된더니 이건 뭐임?
        # append 메서드의 역할을 생각해보자.
    '''
        1. arr라는 이름의 변수를 로컬 영역에서 찾는다.
        2. 없어서 글로벌에 있는 arr을 찾는다.
        3. 글로벌에 있는 arr을 찾아서 그 객체가 가진 메서드를 호출한다.
        4. append 메서드는 리스트에 값을 추가하는 메서드이므로, 
    '''
    arr.append(4) 
    return arr
print(some7())  
print(arr) 

def some8():
    arr[0] = 100
some8()
print(arr)  # ?