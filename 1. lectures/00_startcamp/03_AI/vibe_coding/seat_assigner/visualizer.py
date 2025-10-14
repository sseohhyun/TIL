"""
배정 결과 시각화 및 출력 모듈
"""
def print_seating(seats):
    print("\n[자리 배정 결과]")
    for idx, student in enumerate(seats, 1):
        print(f"{idx}번 자리: {student}")
