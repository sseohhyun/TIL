# Python이 설치된 경량 베이스 이미지 사용
FROM python:3.10-slim     
# 컨테이너 내부에서 작업할 디렉토리 지정             
WORKDIR /workspace    
# 로컬의 requirements.txt 파일을 컨테이너로 복사                 
COPY requirements.txt .   
# pip 업그레이드 및 패키지 설치            
RUN pip install --upgrade pip && \     
    pip install -r requirements.txt
# 실행할 app.py 파일 복사
COPY app.py .   
# 컨테이너 시작 시 실행할 명령 지정                       
CMD ["python", "app.py"]              