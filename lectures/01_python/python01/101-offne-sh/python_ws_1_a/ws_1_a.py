# name 변수에 'Alice' 문자열을 할당한다.
# age 변수에 25 정수를 할당한다.
# height 변수에 5.6 부동 소수점을 할당한다.
# is_student 변수에 True 불린 값을 할당한다.
# 각 변수에 담긴 값을 출력한다.
# f-string을 활용하여 'Alice는 25살이고, 키는 5.6이며 학생 여부는 True입니다.' 문자열을 출력한다.
# 단, name, age, height, is_student 변수를 사용하여야 한다.

# 아래에 코드를 작성하시오.

name = "Alice"
age = int(25)
height = float(5.6)
is_student = True

print(f'{name}\n{age}\n{height}\n{is_student}')
print(f'{name}는 {age}살이고, 키는 {height}이며 학생 여부는 {is_student}입니다.')