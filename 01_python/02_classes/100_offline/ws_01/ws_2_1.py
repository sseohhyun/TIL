class MovieTheater:
    def __init__(self, name, total_seats):
        self.name = name
        self.total_seats = total_seats
        self.reserved_seats = 0

    def __str__(self):
        return self.name

# 인스턴스 생성
theater1 = MovieTheater("메가박스", 100)
theater2 = MovieTheater("CGV", 80)

# 인스턴스 정보 출력 
print(theater1)
print(theater2)