class MovieTheater:
    total_movies = 0

    def __init__(self, name, total_seats):
        self.name = name
        self.total_seats = total_seats
        self.reserved_seats = 0

    def reserve_seat(self):
        if self.reserved_seats < self.total_seats:
            self.reserved_seats += 1
            return "좌석 예약이 성공적으로 완료되었습니다."
        else:
            return "더 이상 예약 가능한 좌석이 없습니다."

    @classmethod
    def add_movie(cls):
        cls.total_movies += 1
        return "영화가 성공적으로 추가되었습니다."

    @staticmethod
    def description():
        print("이 클래스는 영화관의 정보를 관리하고 좌석 예약 및 영화 추가 기능을 제공합니다.")
        print("영화관의 이름, 총 좌석 수, 예약된 좌석 수, 총 영화 수를 관리합니다.")

theater1 = MovieTheater("메가박스", 100)
theater2 = MovieTheater("CGV", 150)

print(theater1.reserve_seat())
print(theater1.reserve_seat())
print(theater2.reserve_seat())

print(MovieTheater.add_movie())
print(MovieTheater.add_movie())

print(f"{theater1.name} 영화관의 총 좌석 수: {theater1.total_seats}")
print(f"{theater1.name} 영화관의 예약된 좌석 수: {theater1.reserved_seats}")
print(f"{theater2.name} 영화관의 총 좌석 수: {theater2.total_seats}")
print(f"{theater2.name} 영화관의 예약된 좌석 수: {theater2.reserved_seats}")
print(f"총 영화 수: {MovieTheater.total_movies}")

MovieTheater.description()