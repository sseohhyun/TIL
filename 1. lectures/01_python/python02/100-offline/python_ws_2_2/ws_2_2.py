'''
문제
영화관 시스템을 모델링하는 클래스를 정의하시오. 요구 사항에 맞춰 클래스를 작성하고, 
인스턴스를 생성하여 영화관 시스템을 시뮬레이션하시오.

요구사항
3432번 문제에서 작성한 코드에서 이어서 작성한다.
MovieTheater 클래스는 좌석을 예약하는 reserve_seat 메서드를 가진다.
reserve_seat 메서드는 예약 가능한 좌석이 있는 경우, reserved_seats를 1 증가시키고 예약 성공 메시지를 반환한다.
예약 가능한 좌석이 없는 경우, 예약 실패 메시지를 반환한다.
MovieTheater 클래스는 현재 예약 상태를 출력하는 current_status 메서드를 가진다.
current_status 메서드는 총 좌석 수와 예약된 좌석 수를 출력한다.

'''

# 아래에 코드를 작성하시오.
class MovieTheater:
    def __init__(self, name, total_seats):
        self.name = name
        self.total_seats = total_seats # 총 좌석수
        self.reserved_seats = 0 # 예약된 좌석수
    def __str__(self):
        return self.name
    
    def reserve_seat(self): 
        if self.total_seats > self.reserved_seats :
            self.reserved_seats += 1
            return "좌석 예약이 완료되었습니다."
        else :
            return "좌석 예약이 실패되었습니다."
    
    def current_status(self):
        return f'총 좌석 수 : {self.total_seats}\n예약된 좌석 수 : {self.reserved_seats}'

movie1 = MovieTheater("메가박스",100)

print(movie1.reserve_seat())
print(movie1.reserve_seat())
print(movie1.reserve_seat())
print(movie1.current_status())
