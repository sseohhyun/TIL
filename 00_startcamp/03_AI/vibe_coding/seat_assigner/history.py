import json
import os

HISTORY_FILE = 'prev_seating.json'

# 저장: {"0": "학생명", "1": "학생명", ...} 형태

def save_seating(seats):
    data = {str(idx): name for idx, name in enumerate(seats)}
    with open(HISTORY_FILE, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)


def load_prev_seating():
    if not os.path.exists(HISTORY_FILE):
        return None
    with open(HISTORY_FILE, 'r', encoding='utf-8') as f:
        data = json.load(f)
    # 인덱스 순서대로 학생명 리스트 반환
    return [data[str(idx)] for idx in range(len(data))]
