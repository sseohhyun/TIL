'''
MovieTheater 클래스를 정의한다.
생성자 메서드는 영화관의 이름(name)과 영화관의 총 좌석 수(total_seats)를 인자로 받는다.
각 인스턴스는 고유한 영화관의 이름(name)과 영화관의 총 좌석 수(total_seats) 변수를 가지고, 인자로 넘겨받은 값을 할당받는다.
예약된 좌석 수를 저장하는 reserved_seats 인스턴스 변수는 0을 할당한다.
MovieTheater 클래스의 인스턴스를 생성하여, 영화관 정보를 확인한다. 참조: __str__
인스턴스를 print하면 인스턴스의 name이 출력 되어야 한다.
'''
# 아래에 코드를 작성하시오.

class MovieTheater:
    def __init__(self, name, total_seats):
        self.name = name
        self.total_seats = total_seats
        self.reserved_seats = 0
    def __str__(self):
        return self.name

movie1 = MovieTheater("메가박스",0)
movie2 = MovieTheater("CGV",0)

print(movie1)
print(movie2)