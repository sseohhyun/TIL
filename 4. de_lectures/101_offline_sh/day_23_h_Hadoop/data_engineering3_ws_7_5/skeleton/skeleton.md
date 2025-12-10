# YARN 스케줄러 변경 및 Pi 계산 프로그램 실행 비교 실습

## 1. FIFO 스케줄러 적용
```bash
sudo vi /etc/hadoop/conf/yarn-site.xml
```
```xml
<property>
  <name>yarn.resourcemanager.scheduler.class</name>
  <value>org.apache.hadoop.yarn.server.resourcemanager.scheduler.fifo.FifoScheduler</value>
</property>
```

## 2. ResourceManager 재시작
```bash
stop-yarn.sh
start-yarn.sh
```

## 3. Pi 프로그램 실행 및 시간 측정 (FIFO)
```bash
time hadoop jar /home/ssafy/hadoop/share/hadoop/mapreduce/hadoop-mapreduce-examples-3.3.5.jar pi 10 100
```


## 자원 사용 확인
```bash
yarn node -list
```

---

## 4. Capacity 스케줄러 적용 (로컬에서는 기본으로 있는 값 사용)
```bash
sudo vi /etc/hadoop/conf/yarn-site.xml
```
```xml
<property>
  <name>yarn.resourcemanager.scheduler.class</name>
  <value>org.apache.hadoop.yarn.server.resourcemanager.scheduler.capacity.CapacityScheduler</value>
</property>
```

## 5. ResourceManager 재시작
```bash
stop-yarn.sh
start-yarn.sh
```

## 6. Pi 프로그램 실행 및 시간 측정 (Capacity)
```bash
time hadoop jar /home/ssafy/hadoop/share/hadoop/mapreduce/hadoop-mapreduce-examples-3.3.5.jar pi 10 100
```

## 자원 사용 확인
```bash
yarn node -list
```

---

## 7. Fair 스케줄러 적용
```bash
sudo vi /etc/hadoop/conf/yarn-site.xml
```
```xml
<property>
  <name>yarn.resourcemanager.scheduler.class</name>
  <value>org.apache.hadoop.yarn.server.resourcemanager.scheduler.fair.FairScheduler</value>
</property>
```

## 8. ResourceManager 재시작
```bash
stop-yarn.sh
start-yarn.sh
```

## 9. Pi 프로그램 실행 및 시간 측정 (Fair)
```bash
time hadoop jar /home/ssafy/hadoop/share/hadoop/mapreduce/hadoop-mapreduce-examples-3.3.5.jar pi 10 100
```

## 자원 사용 확인
```bash
yarn node -list
```
