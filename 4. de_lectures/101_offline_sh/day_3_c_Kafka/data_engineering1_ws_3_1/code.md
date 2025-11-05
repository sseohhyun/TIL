1) Zookeeper 실행
```bash
cd /home/ssafy/kafka
./bin/zookeeper-server-start.sh config/zookeeper.properties
```

2) kafka 브로커 실행
```bash
cd /home/ssafy/kafka
./bin/kafka-server-start.sh config/server.properties
```

3) 현재 생성된 토픽 목록을 조회
```bash
bin/kafka-topics.sh --list --bootstrap-server localhost:9092 
```