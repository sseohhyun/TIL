users = [
    {"username": "alice", "age": 25, "is_active": True},
    {"username": "bob", "age": 17, "is_active": False},
    {"username": "charlie", "age": 30, "is_active": True},
    {"username": "david", "age": 22, "is_active": False},
    {"username": "eve", "age": 29, "is_active": True}
]

# 아래에 코드를 작성하시오.

# 나이가 18세 이상인 사용자를 필터링하는 함수를 작성하시오.
# 활성화된(is_active가 True인) 사용자를 필터링하는 함수를 작성하시오.
# 나이가 18세 이상이고 활성화된 사용자를 필터링하는 함수를 작성하시오.
# 위의 함수를 별도의 모듈로 작성하고, 이를 메인 파일에서 불러와 사용하시오.

import user_filter

print(f' Adults: {user_filter.adults_filter(users)}')
print(f' Active Users: {user_filter.active_filter(users)}')
print(f' Adults Active Users: {user_filter.adults_active_filter(users)}')