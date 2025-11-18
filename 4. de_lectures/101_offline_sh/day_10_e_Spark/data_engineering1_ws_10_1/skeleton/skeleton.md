# Apache Spark 3.5.4 환경 설정 및 실행 명령어

# 1. Apache Spark 3.5.4 다운로드 및 설치
# 공식 사이트에서 다운로드할 파일의 URL을 확인 후 사용하세요.
wget https://archive.apache.org/dist/spark/spark-3.5.4/spark-3.5.4-bin-hadoop3.tgz

# 다운로드한 Spark 압축 해제
tar -xvzf spark-3.5.4-bin-hadoop3.tgz

# 디렉토리를 이동 (기본 위치: /usr/local/spark)
sudo mv spark-3.5.4-bin-hadoop3 /usr/local/spark

# 2. 환경 변수 설정
# .bashrc 파일을 수정하여 환경 변수를 설정하세요.
vi ~/.bashrc

# 아래 내용을 추가 (입력 후 Ctrl + X → Y → Enter)
export SPARK_HOME=/usr/local/spark
export PATH=$SPARK_HOME/bin:$SPARK_HOME/sbin:$PATH

# 환경 변수 적용
source ~/.bashrc

# 설정이 올바르게 되었는지 확인
echo $SPARK_HOME

# 네트워크 환경 설정
vi $SPARK_HOME/conf/spark-env.sh

SPARK_MASTER_HOST=0.0.0.0
SPARK_LOCAL_IP=0.0.0.0
추가를 통한 바인딩

# 3. PySpark 설치 실행 및 버전 확인
# PySpark 설치 (Spark 3.5.4와 일치하게)
pip install pyspark==3.5.4

# 실행
pyspark

# Spark 버전 확인
sc.version

