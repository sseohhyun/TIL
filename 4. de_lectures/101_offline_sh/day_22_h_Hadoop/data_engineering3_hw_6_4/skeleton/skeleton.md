# 설정 파일 적용 확인 및 환경 점검 실습

## 1. core-site.xml, hdfs-site.xml 에 설정한 값 확인
```bash
# core-site.xml에서 설정한 fs.defaultFS 값 확인
hdfs getconf -confKey fs.defaultFS

# hdfs-site.xml에서 설정한 NameNode 저장 경로 확인
hdfs getconf -confKey dfs.namenode.name.dir

# hdfs-site.xml에서 설정한 DataNode 저장 경로 확인
hdfs getconf -confKey dfs.datanode.data.dir
```

## 2. 환경 변수 확인
```bash
# HADOOP_HOME 환경 변수 확인
echo $HADOOP_HOME

# PATH 환경 변수 중 hadoop 관련 경로 확인
echo $PATH | grep hadoop
```

## 3. Hadoop 구성 점검 (hdfs 명령어 정상 동작 여부)
```bash
# HDFS 루트 디렉토리 리스트 확인
hdfs dfs -ls /
```
