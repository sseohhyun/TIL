# Dockerfile을 작성하여 Python 환경이 포함된 Docker 이미지를 생성

# Step 1: 실습용 디렉토리 생성 및 이동
# - Dockerfile, requirements.txt, app.py 파일을 저장할 디렉토리를 새로 만듭니다.
# - 이 디렉토리 내에서 모든 작업을 수행합니다.
mkdir python-docker-env
cd python-docker-env

# Step 2: requirements.txt 파일 생성
# - Python 환경에서 사용할 패키지 목록을 정의합니다.
# - 이 파일은 Dockerfile에서 패키지 설치를 위해 참조됩니다.
# (필요한 Python 패키지를 여기에 작성하세요.)
echo -e "pandas\nnumpy" > requirements.txt

# Step 3: app.py 파일 생성
# - 도커 컨테이너 실행 시 동작할 Python 스크립트를 작성합니다.
# - 단순히 메시지를 출력하여 정상 동작을 확인할 수 있게 합니다.
# (컨테이너 실행 시 출력될 간단한 메시지 코드를 작성하세요.)
echo 'print("Hello from Docker Python environment")' > app.py

# Step 4: Dockerfile 작성
# - Python 3.10이 설치된 슬림 이미지를 기반으로 합니다.
# - 작업 디렉토리를 지정하고, 필요한 파일을 컨테이너에 복사합니다.
# - pip 업그레이드 및 패키지 설치를 진행하며, 최종적으로 app.py를 실행하도록 설정합니다.
# python-docker-env에 위치시켜주세요.

# Step 5: Docker 이미지 빌드
# - 현재 디렉토리에 있는 Dockerfile을 기반으로 이미지를 생성합니다.
# - 이미지 이름은 'python-lab'으로 지정합니다.
# (Dockerfile을 기반으로 이미지를 빌드합니다. 태그는 직접 지정하세요.)
docker build -t python-lab .

# Step 6: 컨테이너 실행
# - 생성한 이미지를 기반으로 컨테이너를 실행합니다.
# - 이름은 'pycheck'으로 지정하고, 터미널과 상호작용 가능한 모드로 실행합니다.
# (이미지를 기반으로 컨테이너를 실행하세요. 이름은 자유롭게 지정)
docker run -it --name pycheck python-lab