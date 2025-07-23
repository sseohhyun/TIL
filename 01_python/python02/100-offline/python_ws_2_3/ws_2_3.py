'''
MovieTheater 클래스를 상속받는 VIPMovieTheater 클래스를 정의한다.
VIPMovieTheater 클래스는 VIP 좌석 수를 저장하는 vip_seats 인스턴스 변수를 가진다.
생성자에서 처리되어야 한다.
VIPMovieTheater 클래스는 VIP 좌석을 예약하는 reserve_vip_seat 메서드를 가진다.
reserve_vip_seat 메서드는 예약 가능한 VIP 좌석이 있는 경우, vip_seats를 1 감소시키고 예약 성공 메시지를 반환한다.
예약 가능한 VIP 좌석이 없는 경우, 예약 실패 메시지를 반환한다.
VIPMovieTheater 클래스는 reserve_seat 메서드를 오버라이딩하여, VIP 좌석이 먼저 예약되도록 한다.
VIP 좌석이 예약 가능한 경우, reserve_vip_seat 메서드를 호출하여 VIP 좌석을 예약한다.
VIP 좌석이 예약 불가능한 경우, 부모 클래스의 reserve_seat 메서드를 호출하여 일반 좌석을 예약한다.
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


class VIPMovieTheater(MovieTheater):
    def __init__(self, name, total_seats, vip_seats):
        super().__init__(name, total_seats)
        self.vip_seats = vip_seats # vip 좌석수
    
    def reserve_vip_seat(self):
        if self.vip_seats > 0 :
            self.vip_seats -= 1
            self.reserved_seats += 1
            return "VIP 좌석 예약이 완료되었습니다."
        else :
            return "예약 가능한 VIP 좌석이 없습니다."
        
    def reserve_seat(self): 
        if self.vip_seats > 0 :
            return self.reserve_vip_seat()
        else :
            return super().reserve_seat() 


movie1 = VIPMovieTheater("메가박스",100,3)

print(movie1.reserve_vip_seat())
print(movie1.reserve_vip_seat())
print(movie1.reserve_vip_seat())
print(movie1.reserve_seat())
print(movie1.reserve_vip_seat())