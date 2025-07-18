import os
import json

STUDY_DIR = "STUDY"
EXAM_STATUS_FILE = "exam_status.json"
BOOKMARKS_FILE = "bookmarks.json"

# STUDY 폴더 내 md 파일 목록 반환
def list_study_files():
    if not os.path.exists(STUDY_DIR):
        return []
    return [f for f in os.listdir(STUDY_DIR) if f.endswith('.md')]

# 시험 완료 표시
def mark_exam_completed(md_file):
    if os.path.exists(EXAM_STATUS_FILE):
        with open(EXAM_STATUS_FILE, "r", encoding="utf-8") as f:
            status = json.load(f)
    else:
        status = {}
    status[os.path.join(STUDY_DIR, md_file)] = "completed"
    with open(EXAM_STATUS_FILE, "w", encoding="utf-8") as f:
        json.dump(status, f, ensure_ascii=False, indent=2)

# 시험 완료 여부 확인
def is_exam_completed(md_file):
    if not os.path.exists(EXAM_STATUS_FILE):
        return False
    with open(EXAM_STATUS_FILE, "r", encoding="utf-8") as f:
        status = json.load(f)
    return status.get(os.path.join(STUDY_DIR, md_file)) == "completed"

# 문제 북마크 추가
def add_bookmark(question):
    if os.path.exists(BOOKMARKS_FILE):
        with open(BOOKMARKS_FILE, "r", encoding="utf-8") as f:
            bookmarks = json.load(f)
    else:
        bookmarks = {"bookmarked_questions": []}
    bookmarks["bookmarked_questions"].append(question)
    with open(BOOKMARKS_FILE, "w", encoding="utf-8") as f:
        json.dump(bookmarks, f, ensure_ascii=False, indent=2)

# 북마크된 문제 목록 반환
def get_bookmarked_questions():
    if not os.path.exists(BOOKMARKS_FILE):
        return []
    with open(BOOKMARKS_FILE, "r", encoding="utf-8") as f:
        bookmarks = json.load(f)
    return bookmarks.get("bookmarked_questions", [])

if __name__ == "__main__":
    import tkinter as tk
    from tkinter import messagebox, simpledialog

    def refresh_file_list():
        files = list_study_files()
        file_listbox.delete(0, tk.END)
        for f in files:
            status = "✅" if is_exam_completed(f) else "❌"
            file_listbox.insert(tk.END, f"{f} {status}")

    def mark_selected_completed():
        sel = file_listbox.curselection()
        if not sel:
            messagebox.showinfo("알림", "파일을 선택하세요.")
            return
        fname = file_listbox.get(sel[0]).split()[0]
        mark_exam_completed(fname)
        refresh_file_list()
        messagebox.showinfo("완료", f"{fname} 파일을 시험 완료로 표시했습니다.")

    def show_bookmarks():
        bookmarks = get_bookmarked_questions()
        if not bookmarks:
            messagebox.showinfo("북마크", "북마크된 문제가 없습니다.")
            return
        bm_text = "\n\n".join([f"[{b['type']}] {b['question_text']}\n({b['source_file']})" for b in bookmarks])
        top = tk.Toplevel(root)
        top.title("북마크된 문제")
        text = tk.Text(top, width=60, height=20)
        text.insert(tk.END, bm_text)
        text.config(state=tk.DISABLED)
        text.pack()

    root = tk.Tk()
    root.title("STUDY 시험 관리")

    tk.Label(root, text="STUDY 폴더의 md 파일 목록").pack()
    file_listbox = tk.Listbox(root, width=50)
    file_listbox.pack()

    btn_frame = tk.Frame(root)
    btn_frame.pack(pady=5)
    tk.Button(btn_frame, text="시험 완료로 표시", command=mark_selected_completed).pack(side=tk.LEFT, padx=5)
    tk.Button(btn_frame, text="북마크 문제 보기", command=show_bookmarks).pack(side=tk.LEFT, padx=5)

    refresh_file_list()
    root.mainloop()
