'''
User 클래스를 정의한다.
User 클래스는 사용자의 이름과 이메일을 인자로 받는 생성자 메서드를 정의한다.
각 인스턴스는 고유한 이름과 이메일을 담을 수 있는 name과 email 변수를 가지고, 인자로 넘겨받은 값을 할당 받는다.
User 클래스는 사용자의 정보를 출력하는 show_info 인스턴스 메서드를 정의한다.
AdminUser 클래스를 정의하고, User 클래스를 상속받는다.
AdminUser 클래스는 추가적으로 관리자의 권한을 나타내는 permissions 변수를 가지며, 생성자 메서드에서 이를 초기화한다.
AdminUser 클래스는 show_info 메서드를 오버라이딩하여, 사용자 정보와 함께 권한 정보를 출력한다.
2개 이상의 User 인스턴스와 1개 이상의 AdminUser 인스턴스를 생성하고, 각 인스턴스의 show_info 메서드를 호출하여 정보를 출력한다.
'''

# 아래에 코드를 작성하시오.
class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email

    def show_info(self):
        return f'Name : {self.name}, Email : {self.email}'

class AdminUser(User):
    def __init__(self, name, email, permissions):
        self.permissions = permissions
        super().__init__(name, email)

    def show_info(self):
        return f'Name : {self.name}, Email : {self.email}, Permissions : {self.permissions}'    
    
user1 = User("Alice", "alice@example.com")
user2 = User("Bob", "bob@example.com")
user3 = AdminUser("Charlie", "charlie@example.com", "Full Access")

print(user1.show_info())
print(user2.show_info())
print(user3.show_info())
