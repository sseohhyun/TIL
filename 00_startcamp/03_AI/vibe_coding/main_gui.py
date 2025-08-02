"""
PyQt5 기반 학생 자리 무작위 배정 프로그램 GUI
"""
import sys
from PyQt5.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QGridLayout, QPushButton, QLabel, QMessageBox
)
from seat_assigner.assigner import assign_seats
from seat_assigner.history import load_prev_seating, save_seating
from PyQt5.QtCore import Qt

class SeatAssignerApp(QWidget):

    def __init__(self):
        super().__init__()
        self.setWindowTitle('학생 자리 무작위 배정')
        self.setGeometry(100, 100, 400, 500)
        from seat_assigner.students_list import STUDENTS
        self.students = STUDENTS[:]
        self.seats = []
        self.prev_seating = load_prev_seating()
        self.is_edit_mode = False
        self.selected_pairs = []  # [(idx1, idx2), ...]
        self.current_pair = []    # [idx1, idx2]
        self.init_ui()

    def init_ui(self):
        main_layout = QVBoxLayout()
        self.label = QLabel(f'학생 명단 ({len(self.students)}명)')
        self.label.setFixedHeight(22)
        self.label.setMaximumWidth(180)
        main_layout.addWidget(self.label)

        self.assign_btn = QPushButton('자리 무작위 배정')
        self.assign_btn.clicked.connect(self.assign_seats)
        main_layout.addWidget(self.assign_btn)

        self.confirm_btn = QPushButton('확정')
        self.confirm_btn.clicked.connect(self.confirm_seats)
        self.confirm_btn.setEnabled(False)
        main_layout.addWidget(self.confirm_btn)

        self.edit_btn = QPushButton('변경 모드')
        self.edit_btn.clicked.connect(self.toggle_edit_mode)
        main_layout.addWidget(self.edit_btn)


        # 교실 좌석 배치: 5행, 가운데 통로
        self.grid = QGridLayout()

        # 상단 라벨: 7열에 맞춰 배치
        self.grid.addWidget(QLabel('문'), 0, 0)
        self.grid.addWidget(QLabel(''), 0, 1)
        self.grid.addWidget(QLabel('스크린'), 0, 2)
        self.grid.addWidget(QLabel(''), 0, 3)
        self.grid.addWidget(QLabel('스크린'), 0, 4)
        self.grid.addWidget(QLabel(''), 0, 5)
        self.grid.addWidget(QLabel('강사'), 0, 6)

        # 좌석 위치 정의
        self.seat_labels = []
        seat_positions = []
        # 1~4행: 3자리-통로-3자리
        for row in range(1, 5):
            for col in range(0, 3):
                seat_positions.append((row, col))
            for col in range(4, 7):
                seat_positions.append((row, col))
        # 5행: 2자리-통로-2자리
        for col in range(0, 2):
            seat_positions.append((5, col))
        for col in range(4, 6):
            seat_positions.append((5, col))

        self.max_seats = len(seat_positions)
        for idx, pos in enumerate(seat_positions):
            label = QLabel()
            label.setStyleSheet('border: 1px solid gray; min-width: 70px; min-height: 20px; background-color: #ffffff;')
            label.setAlignment(Qt.AlignCenter)
            label.mousePressEvent = lambda event, i=idx: self.handle_seat_click(i)
            self.grid.addWidget(label, pos[0], pos[1])
            self.seat_labels.append(label)

        main_layout.addLayout(self.grid)
        self.setLayout(main_layout)

        self.update_seats(self.students)

    # 학생 명단은 고정이므로 파일 불러오기 기능 제거

    def assign_seats(self):
        # 이전 자리와 겹치지 않게 shuffle
        import random
        max_attempts = 1000
        for _ in range(max_attempts):
            seats = self.students[:]
            random.shuffle(seats)
            if self.prev_seating:
                if all(seats[i] != self.prev_seating[i] for i in range(min(len(seats), len(self.prev_seating)))):
                    break
            else:
                break
        else:
            QMessageBox.warning(self, '경고', '이전 자리와 겹치지 않는 배정이 불가능합니다.')
        self.seats = seats
        self.update_seats(self.seats)
        self.label.setText('자리 배정 결과')
        self.confirm_btn.setEnabled(True)
        self.edit_btn.setEnabled(True)
        self.is_edit_mode = False
        self.selected_indices = []

    def toggle_edit_mode(self):
        if not self.seats or not self.prev_seating or (not self.is_edit_mode and self.seats != self.prev_seating):
            QMessageBox.warning(self, '경고', '자리를 먼저 확정해 주세요.')
            return
        self.is_edit_mode = not self.is_edit_mode
        self.selected_pairs = []
        self.current_pair = []
        self.update_seats(self.seats)
        if self.is_edit_mode:
            self.edit_btn.setText('변경 모드 종료')
            self.confirm_btn.setEnabled(True)
        else:
            self.edit_btn.setText('변경 모드')
            self.confirm_btn.setEnabled(True)

    def handle_seat_click(self, idx):
        if not self.is_edit_mode:
            return
        if idx >= len(self.seats):
            return
        # 이미 선택된 쌍에 포함된 좌석은 선택 불가
        for pair in self.selected_pairs:
            if idx in pair:
                return
        # 현재 쌍에서 선택 해제
        if idx in self.current_pair:
            self.current_pair.remove(idx)
            self.update_seats(self.seats)
            return
        # 현재 쌍에 추가
        if len(self.current_pair) < 2:
            self.current_pair.append(idx)
            self.update_seats(self.seats)
        # 두 명 선택 시 교환 후 쌍 저장, 다음 쌍 선택 가능
        if len(self.current_pair) == 2:
            i1, i2 = self.current_pair
            self.seats[i1], self.seats[i2] = self.seats[i2], self.seats[i1]
            self.selected_pairs.append((i1, i2))
            self.current_pair = []
            self.update_seats(self.seats)

    def confirm_seats(self):
        save_seating(self.seats)
        self.prev_seating = self.seats[:]
        self.confirm_btn.setEnabled(False)
        self.is_edit_mode = False
        self.selected_pairs = []
        self.current_pair = []
        self.edit_btn.setText('변경 모드')
        self.edit_btn.setEnabled(True)
        self.update_seats(self.seats)
        QMessageBox.information(self, '확정', '자리 배정이 확정되어 저장되었습니다.')

    def update_seats(self, students):
        highlight_colors = [
            ('#ff6600', '#ffe4b3'),
            ('#007acc', '#cce6ff'),
            ('#009966', '#ccffe6'),
            ('#9933cc', '#e6ccff'),
            ('#cc0000', '#ffcccc'),
        ]
        for i, label in enumerate(self.seat_labels):
            if i < len(students):
                label.setText(f'{students[i]}')
                style = 'border: 1px solid gray; min-width: 70px; min-height: 20px; background-color: #ffffff;'
                # 이미 교환된 쌍 하이라이트
                if self.is_edit_mode:
                    for idx, pair in enumerate(self.selected_pairs):
                        if i in pair:
                            border, bg = highlight_colors[idx % len(highlight_colors)]
                            style = f'border: 2px solid {border}; min-width: 70px; min-height: 20px; background-color: {bg};'
                    # 현재 선택 중인 쌍 하이라이트(가장 우선)
                    if i in self.current_pair:
                        border, bg = highlight_colors[len(self.selected_pairs) % len(highlight_colors)]
                        style = f'border: 2px solid {border}; min-width: 70px; min-height: 20px; background-color: {bg};'
                label.setStyleSheet(style)
            else:
                label.setText('')
                label.setStyleSheet('border: 1px solid gray; min-width: 70px; min-height: 20px; background-color: #ffffff;')

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = SeatAssignerApp()
    window.show()
    sys.exit(app.exec_())
