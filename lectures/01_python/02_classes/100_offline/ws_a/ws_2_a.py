'''
2개 이상의 인스턴스를 생성하고, 각 인스턴스의 name과 email을 출력한다.
User 클래스의 user_count를 출력한다.
description 스태틱 메서드를 호출한다.
'''
# User 클래스를 정의한다.
class User:
    # User의 인스턴스 수를 기록할 수 있는 클래스 변수 user_count를 정의하고, 0을 할당한다.
    user_count = 0 
    # 생성자 메서드를 정의한다.
    # 생성자 메서드는 사용자의 이름과 이메일을 인자로 받는다.
    # 각 인스턴스는 고유한 이름과 이메일을 담을 수 있는 name과 email 변수를 가지고, 인자로 넘겨받은 값을 할당 받는다.
    def __init__(self, name, email):
        self.name = name
        self.email = email
        # 인스턴스가 생성될 때마다 user_count를 1 증가시킨다.
        User.user_count += 1

    # 'SNS 사용자'에 대한 설명을 출력하는 description 스태틱 메서드를 정의한다.
    @staticmethod       # 함수를 꾸며주는 함수 (데코레이터)를 사용하게 되면 스태틱 메서드가 된다.
    def description():  # 데코레이터 없이 함수를 정의하면 인스턴스 메서드가 된다.
        '''
            스태틱 메서드란, 클래스나 인스턴스의 속성과 무관한 동작을 진행할때 사용한다.
            단, 속해있는 그 클래스의 동작을 대변할 수 있어야 한다.
        '''
        print("SNS 사용자: 이름과 이메일을 가지고 있습니다.")
        