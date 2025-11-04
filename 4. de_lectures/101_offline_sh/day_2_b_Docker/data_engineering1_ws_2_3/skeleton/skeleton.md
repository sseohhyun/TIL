# Docker 컨테이너를 직접 실행하고, 내부에서 파일 생성하거나 명령

# Step 1: 컨테이너 실행
# (컨테이너 이름은 'devtest', 이미지 이름은 'python-lab'로 지정하세요.)
docker run -it --name devtest python-lab

# Step 2: 컨테이너 내부에서 작업

## 2-1: 현재 디렉토리 위치 확인
pwd

## 2-2: 테스트 파일 생성
echo "Docker container 내부 테스트 파일입니다." > docker_note.txt

## 2-3: 생성한 파일 내용 확인
cat docker_note.txt

## 2-4: Python 실행 후 출력
python
>>> print(3 * 7)
>>> exit()

# Step 3: 컨테이너 종료
# (exit 또는 Ctrl+D를 사용하세요.)
exit

# Step 4: 컨테이너 목록 확인
docker ps -a

# Step 5: 컨테이너 재접속 (선택 사항)
docker start -ai devtest