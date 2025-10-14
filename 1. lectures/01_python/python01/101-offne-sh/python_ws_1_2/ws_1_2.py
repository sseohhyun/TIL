# friends 리스트에 'Alice', 'Bob', 'Charlie' 문자열을 할당한다.
# user_info 딕셔너리에 'username' 키에 'user123' 값을, 'age' 키에 20 값을, 'is_active' 키에 True 값을 할당한다.
# friends 리스트와 user_info 딕셔너리에 담긴 값을 각각 출력한다.
# friends 리스트에 'David'를 추가한 후, 리스트의 모든 값을 출력한다.
# user_info 딕셔너리에 'email' 키에 'user123@example.com' 값을 추가한 후, 딕셔너리의 모든 값을 출력한다.

# 아래에 코드를 작성하시오.

friends = ['Alice', 'Bob', 'Charlie']
user_info = {'username':'user123', 
             'age' : 20, 
             'is_active':True}
print(friends)
print(user_info)

friends.append('David')
print(friends)

user_info['email'] = 'user123@example.com'
print(user_info)