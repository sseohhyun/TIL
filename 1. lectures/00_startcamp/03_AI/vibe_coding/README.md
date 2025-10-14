# 학생 자리 무작위 배정 프로젝트

## 프로젝트 개요
학생들의 자리를 무작위로 배정하고, 배정 결과를 시각적으로 확인 및 관리할 수 있는 파이썬(PyQt5) 기반 응용 프로그램입니다.

## 주요 기능
- 학생 명단은 코드에 고정되어 관리됩니다.
- 무작위 자리 배정(이전 자리와 중복 방지)
- 자리 배정 결과를 파일(prev_seating.json)에 저장 및 불러오기
- GUI에서 자리 배정 결과를 교실 형태로 시각화
- 자리 배정 확정 전까지 여러 번 무작위 배정 가능
- 확정 후, "변경 모드"에서 학생 쌍을 선택해 자리 교환 가능
  - 여러 쌍을 연속적으로 교환할 수 있으며, 각 쌍은 다른 색상으로 하이라이트됨
  - 확정 버튼을 눌러야만 변경 결과가 저장됨

## 실행 방법
1. Python 3.8 이상 환경에서 `pip install pyqt5`로 라이브러리 설치
2. `main_gui.py` 실행

## 사용법 요약
1. 프로그램 실행 후 "자리 무작위 배정" 버튼 클릭 → 학생 자리 자동 배정
2. "확정" 버튼 클릭 시 결과가 저장됨
3. 확정 후 "변경 모드" 진입 → 학생 쌍을 클릭해 자리 교환, 여러 쌍 선택 가능(각 쌍마다 색상 다름)
4. 다시 "확정" 버튼 클릭 시 변경 결과 저장

## 파일 구조
- main_gui.py : GUI 실행 파일
- seat_assigner/students_list.py : 학생 명단
- seat_assigner/assigner.py : 자리 배정 알고리즘
- seat_assigner/history.py : 자리 배정 결과 저장/불러오기
- prev_seating.json : 최근 확정된 자리 배정 결과

## 기타
- 모든 코드는 PEP8 스타일을 준수하며, 예외 처리 및 사용자 친화적 메시지를 제공합니다.
- 학생 명단은 `students_list.py`에서 직접 수정 가능합니다.

# 학생 자리 무작위 배정 프로젝트

## 프로젝트 개요
학생들의 자리를 무작위로 배정하는 파이썬 기반 응용 프로그램입니다. 현재 학생 명단은 코드에 고정되어 있으며, PyQt5 기반 GUI를 통해 자리 배정 결과를 바로 확인할 수 있습니다.

## 실행 방법
1. Python 3.8 이상 환경에서 `pip install pyqt5`로 라이브러리 설치
2. `main_gui.py` 실행

## 주요 파일
- `main_gui.py`: PyQt5 기반 GUI 실행 파일
- `seat_assigner/students_list.py`: 고정 학생 명단
- `seat_assigner/assigner.py`: 자리 무작위 배정 알고리즘
- `seat_assigner/visualizer.py`: CLI용 결과 출력(선택적)

## 폴더 구조
```
vibe_coding/
├── main_gui.py
├── seat_assigner/
│   ├── students_list.py
│   ├── assigner.py
│   ├── visualizer.py
│   └── __init__.py
├── README.md
```

## 참고
- 학생 명단은 `students_list.py`에서 직접 수정 가능
- GUI에서 바로 자리 배정 결과 확인
