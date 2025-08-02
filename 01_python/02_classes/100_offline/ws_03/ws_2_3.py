class MovieTheater:
    def __init__(self, name, total_seats):
        self.name = name
        self.total_seats = total_seats
        self.reserved_seats = 0

    def reserve_seat(self):
        if self.reserved_seats < self.total_seats:
            self.reserved_seats += 1
            return "좌석 예약이 완료되었습니다."
        else:
            return "예약 가능한 좌석이 없습니다."


class VIPMovieTheater(MovieTheater):
    def __init__(self, name, total_seats, vip_seats):
        super().__init__(name, total_seats)
        self.vip_seats = vip_seats

    def reserve_vip_seat(self):
        if self.vip_seats > 0:
            self.vip_seats -= 1
            return "VIP 좌석 예약이 완료되었습니다."
        else:
            return "예약 가능한 VIP 좌석이 없습니다."

    def reserve_seat(self):
        if self.vip_seats > 0:
            return self.reserve_vip_seat()
        else:
            return super().reserve_seat()


vip_movie_theater = VIPMovieTheater("VIP 영화관", 100, 3)
print(vip_movie_theater.reserve_seat())
print(vip_movie_theater.reserve_seat())
print(vip_movie_theater.reserve_seat())
print(vip_movie_theater.reserve_seat())
print(vip_movie_theater.reserve_vip_seat())

