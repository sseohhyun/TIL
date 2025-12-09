# 로컬 WSL Hadoop 설치 및 환경 설정 실습

## 1. Hadoop 3.3.5 다운로드
```bash
wget https://dlcdn.apache.org/hadoop/common/hadoop-3.3.5/hadoop-3.3.5.tar.gz
```

## 압축 해제
```bash
tar -xvzf hadoop-3.3.5.tar.gz
```

## 2. 디렉토리 이동(기본 위치: /home/ssafy/hadoop)
```bash
sudo mv hadoop-3.3.5 /home/ssafy/hadoop
```

## 3. 환경 변수 설정 
```bash
# .bashrc 파일 수정
vi ~/.bashrc
```

### 아래 내용 추가 (입력 후 Ctrl + X → Y → Enter)
```bash
export HADOOP_HOME=/home/ssafy/hadoop
export HADOOP_CONF_DIR=$HADOOP_HOME/etc/hadoop
export PATH=$PATH:$HADOOP_HOME/bin:$HADOOP_HOME/sbin
```

### 적용
```bash
source ~/.bashrc
echo $HADOOP_HOME  # 출력 결과: /home/ssafy/hadoop
```

## 4. 설정 파일 구성

### (1) hadoop-env.sh
```bash
cd $HADOOP_HOME/etc/hadoop
vi hadoop-env.sh
```

#### JAVA_HOME 설정 추가
```bash
export JAVA_HOME=/usr/lib/jvm/java-11-openjdk-amd64
```

### (2) core-site.xml
```bash
vi core-site.xml
```

#### 내용 추가
```xml
<configuration>
  <property>
    <name>fs.defaultFS</name>
    <value>hdfs://localhost:9000</value>
  </property>
</configuration>
```

### (3) hdfs-site.xml
```bash
vi hdfs-site.xml
```

#### 내용 추가
```xml
<configuration>
  <property>
    <name>dfs.replication</name>
    <value>1</value>
  </property>
  <property>
    <name>dfs.namenode.name.dir</name>
    <value>file:///home/ssafy/hadoop/data/namenode</value>
  </property>
  <property>
    <name>dfs.datanode.name.dir</name>
    <value>file:///home/ssafy/hadoop/data/datanode</value>
  </property>
</configuration>
```

### (4) yarn-site.xml
```bash
vi yarn-site.xml
```

#### 내용 추가
```xml
<configuration>
  <property>
    <name>yarn.resourcemanager.aux-hostname</name>
    <value>localhost</value>
  </property>
  <property>
    <name>yarn.nodemanager.aux-services</name>
    <value>mapreduce_shuffle</value>
  </property>
</configuration>
```

### (5) mapred-site.xml
```bash
# 템플릿이 없을 경우 복사
cp mapred-site.xml.template mapred-site.xml

# 수정
vi mapred-site.xml
```

#### 내용 추가
```xml
<configuration>
  <property>
    <name>mapreduce.framework.name</name>
    <value>yarn</value>
  </property>
</configuration>
```

## 5. 데이터 디렉터리 생성
```bash
mkdir -p /home/ssafy/hadoop/data/namenode
mkdir -p /home/ssafy/hadoop/data/datanode
```

## 6. Hadoop 초기화 및 실행
```bash
hdfs namenode -format
start-dfs.sh
start-yarn.sh
```

## 웹 UI 확인
- NameNode UI: [http://localhost:9870](http://localhost:9870) (HDFS 상태 확인)
- ResourceManager UI: [http://localhost:8088](http://localhost:8088) (YARN 작업 모니터링)
