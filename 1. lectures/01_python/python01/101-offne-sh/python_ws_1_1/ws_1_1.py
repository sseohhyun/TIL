# username 변수에 'user123' 문자열을 할당한다.
# age 변수에 20 정수를 할당한다.
# is_active 변수에 True 불린 값을 할당한다.
# 각 변수에 담긴 값을 출력한다.
# f-string을 활용하여 'Username: user123, Age: 20, Active: True' 문자열을 출력한다.
# 단, username, age, is_active 변수를 사용하여야 한다.
# age 변수를 5만큼 증가시킨 후, 새로운 값을 출력한다.

# 아래에 코드를 작성하시오.

username = "user123"
age = int(20)
is_active = True
print(f'{username}\n{age}\n{is_active}')
print(f"Username: {username}, Age: {age}, Active: {is_active}")
age_plus_5 = age + 5
print(age_plus_5)