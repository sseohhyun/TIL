"""
자리 배정 알고리즘 모듈
"""
import random

def assign_seats(students):
    """학생 명단을 무작위로 섞어 자리를 배정합니다."""
    seats = students[:]
    random.shuffle(seats)
    return seats
