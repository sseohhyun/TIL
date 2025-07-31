"""
학생 명단 불러오기 및 저장 모듈
"""
import csv

def load_students(filepath):
    """CSV 파일에서 학생 명단을 불러옵니다."""
    students = []
    with open(filepath, encoding='utf-8') as f:
        reader = csv.reader(f)
        for row in reader:
            if row:
                students.append(row[0])
    return students
