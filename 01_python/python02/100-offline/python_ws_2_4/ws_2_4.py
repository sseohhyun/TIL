'''
3433번 문제에서 작성한 코드에서 이어서 작성한다.

MovieTheater 클래스는 모든 영화관이 공통으로 가지는 total_movies변수를 가진다.
total_movies 변수를 MovieTheater 클래스에 클래스 변수로 추가한다.
MovieTheater 클래스는 총 영화 수를 증가시키는 add_movie 클래스 메서드를 가진다
add_movie 메서드는 total_movies를 1 증가시키고, 영화 추가 성공 메시지를 반환한다.
MovieTheater 클래스는 영화관의 정보를 출력하는 description 정적 메서드를 가진다.
description 메서드는 아래 문장을 출력한다.
'"이 클래스는 영화관의 정보를 관리하고 좌석 예약 및 영화 추가 기능을 제공합니다."
"영화관의 이름, 총 좌석 수, 예약된 좌석 수, 총 영화 수를 관리합니다."

'''

# 아래에 코드를 작성하시오.
class MovieTheater:
    total_movies = 0
    
    def __init__(self, name, total_seats):
        self.name = name
        self.total_seats = total_seats # 총 좌석수
        self.reserved_seats = 0 # 예약된 좌석수
    def __str__(self):
        return self.name
    
    def reserve_seat(self): 
        if self.total_seats > self.reserved_seats :
            self.reserved_seats += 1
            return "좌석 예약이 성공적으로 완료되었습니다."
        else :
            return "좌석 예약이 실패되었습니다."
    
    def current_status(self):
        return f'영화관의 총 좌석 수 : {self.total_seats}\n예약된 좌석 수 : {self.reserved_seats}'
    
    @classmethod
    def add_movie(cls):
        cls.total_movies += 1
        return "영화가 성공적으로 추가되었습니다."
    
    @staticmethod
    def description(string):
        return string

str_movie = '''이 클래스는 영화관의 정보를 관리하고 좌석 예약 및 영화 추가 기능을 제공합니다.
영화관의 이름, 총 좌석 수, 예약된 좌석 수, 총 영화 수를 관리합니다.'''


movie1 = MovieTheater("메가박스",100)

print(movie1.reserve_seat())
print(movie1.reserve_seat())
print(movie1.reserve_seat())
print(MovieTheater.classmethod())
print(MovieTheater.staticmethod())


print(movie1.current_status())
