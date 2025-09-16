# 자동으로 .git 폴더 삭제 해주는 코드.
# 현재 폴더를 기준으로 모든 폴더를 조사하여서,
# .git 폴더를 삭제 한다.
    # 단, 최상위 폴더 (코드가 실행된 위치의 .git은 제외하고)
# os 파이썬 표준 라이브러리 -> 운영 체제와 상호 작용 가능
import os
import shutil

# 현재 폴더 경로를 변수에 저장
current_folder = os.getcwd()

# 현재 폴더 및 모든 하위 폴더를 반복
for foldername, subfolders, filenames in os.walk(current_folder):
    # .git 폴더가 현재 폴더의 하위 폴더 목록에 있으면
    if '.git' in subfolders:
        # 최상위 폴더는 제외
        if foldername == current_folder:
            continue

        # 삭제할 .git 폴더의 전체 경로를 변수에 저장
        git_folder_path = os.path.join(foldername, '.git')

        try:
            # shutil.rmtree를 사용하여 운영 체제에 관계없이 폴더 삭제
            shutil.rmtree(git_folder_path)
            print(f'{git_folder_path} 폴더가 삭제되었습니다.')
        except OSError as e:
            print(f"오류: {e.strerror}. 폴더를 삭제할 수 없습니다: {git_folder_path}")

        # .git 폴더를 삭제했으므로, os.walk가 해당 하위 디렉토리를 탐색하지 않도록
        # subfolders 리스트에서 .git을 제거합니다.
        subfolders.remove('.git')
