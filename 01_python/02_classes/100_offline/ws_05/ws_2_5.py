'''
'Theater' 부모 클래스를 정의한다.
'Theater' 클래스는 영화관의 이름을 저장하는 'name' 인스턴스 변수를 가진다.
'Theater' 클래스는 영화관의 총 좌석 수를 저장하는 'total_seats' 인스턴스 변수를 가진다.
'Theater' 클래스는 현재 예약된 좌석 수를 저장하는 'reserved_seats' 인스턴스 변수를 가진다.
'Theater' 클래스는 좌석을 예약하는 'reserve_seat' 인스턴스 메서드를 가진다.
'reserve_seat' 메서드는 예약 가능한 좌석이 있는 경우, 'reserved_seats'를 1 증가시키고 예약 성공 메시지를 반환한다.
예약 가능한 좌석이 없는 경우, 예약 실패 메시지를 반환한다.

MovieTheater 자식 클래스를 정의하고, Theater 클래스를 상속받는다.
MovieTheater 클래스는 영화관의 총 영화 수를 저장하는 total_movies 클래스 변수를 가진다.
MovieTheater 클래스는 영화관의 총 영화 수를 증가시키는 add_movie 클래스 메서드를 가진다.
add_movie 메서드는 total_movies를 1 증가시키고, 영화 추가 성공 메시지를 반환한다.
MovieTheater 클래스는 영화관의 정보를 출력하는 description 정적 메서드를 가진다.
'''

class Theater:
    def __init__(self, name):
        self.name = name

class MovieTheater(Theater):
    total_movies = 0

    @classmethod
    def add_movie(cls):
        cls.total_movies += 1
        return "영화 추가 성공"
        # 만약에
        # print("영화 추가 성공")
        # python은 함수가 return 값이 없으면?
        # 알아서 None을 return 하게 만들어 준다.

    # MovieTheater 클래스는 영화관의 정보를 출력하는 description 정적 메서드를 가진다.
    # 정적 메서드는 self와 cls를 필수적으로 매개변수로 넘겨줄필요가 없다.
    # 정적 메서드에 기대하는바가, self와 cls의 속성을 조작하는 것이 아니기 때문이다.
    @staticmethod
    def description(obj):
        # description 메서드는 영화관의 이름, 총 좌석 수, 예약된 좌석 수, 총 영화 수를 출력한다.
        print(obj.name)

    
mt = MovieTheater('메가박스')
# result = MovieTheater.add_movie()
print(MovieTheater.total_movies)
# print(result)
MovieTheater.description(mt)

import os
class FuncUtil:
    @staticmethod
    def desctipion():
        print(os.getcwd())
    # 이곳에는 특별한 인스턴스가 생성되는게 아니라
    # 각종 기능들을 모아놓은 class
    # A라는 기능을 위해 만들어 놓은 class예요
    # 근데 그러면? instance가 만들어질 필요가 없으니
    # 저는 self가 필요 없는데
    # 매번 메서드를 정의할때마다 불필요한 self로 메모리를 낭비하고 싶지 않아요.
    # 그럼 어떻게해야하죠?
    # -> staticmethod
    @staticmethod
    def add(x, y):
        return x + y
    
    @staticmethod
    def sub(x, y):
        return x - y