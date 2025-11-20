from kafka import KafkaProducer
import json
import time
import random
from datetime import datetime, timedelta

# Kafka Producer 생성
producer = KafkaProducer(
    bootstrap_servers=['localhost:9092'],
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)

# 샘플 페이지 및 유저 목록
pages = ["/home", "/product/123", "/product/456", "/cart", "/checkout"]
users = [f"user_{i}" for i in range(1, 6)]
events = ["click", "view", "purchase"]

base_time = datetime.now() - timedelta(minutes=5)

for i in range(100):
    event_time = base_time + timedelta(seconds=random.randint(0, 300))  # 5분 내 랜덤
    message = {
        "user_id": random.choice(users),
        "page": random.choice(pages),
        "event_type": random.choice(events),
        "timestamp": event_time.strftime("%Y-%m-%d %H:%M:%S")
    }
    
    producer.send("click-events", message)
    print(f"전송된 이벤트: {message}")
    time.sleep(0.3)

producer.flush()
