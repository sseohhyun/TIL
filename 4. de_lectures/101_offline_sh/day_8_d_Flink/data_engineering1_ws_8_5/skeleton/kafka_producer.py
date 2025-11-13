from kafka import KafkaProducer
import json
import time
import random
from datetime import datetime

# Kafka 프로듀서 설정
producer = KafkaProducer(
    bootstrap_servers=['localhost:9092'],
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)

# 샘플 데이터 속성
stock_codes = ["005930", "035720", "035420", "051910", "000660"]  # 삼성전자, 카카오, 네이버, LG화학, SK하이닉스
stock_names = ["삼성전자", "카카오", "네이버", "LG화학", "SK하이닉스"]
trade_types = ["매수", "매도"]
base_prices = {
    "005930": 70000,  # 삼성전자
    "035720": 50000,  # 카카오
    "035420": 400000, # 네이버
    "051910": 400000, # LG화학
    "000660": 150000  # SK하이닉스
}

# 데이터 생성 및 전송
for _ in range(1000):  # 1000개의 거래 이벤트 생성
    stock_idx = random.randint(0, len(stock_codes)-1)
    stock_code = stock_codes[stock_idx]
    stock_name = stock_names[stock_idx]
    base_price = base_prices[stock_code]
    
    # 가격 변동 (기준가의 ±5% 범위 내에서 랜덤)
    price_variation = random.uniform(-0.05, 0.05)
    price = int(base_price * (1 + price_variation))
    
    # 거래량 (100주 단위로 1~1000주)
    volume = random.randint(1, 10) * 100
    
    event = {
        "stock_code": stock_code,
        "stock_name": stock_name,
        "trade_type": random.choice(trade_types),
        "price": price,
        "volume": volume,
        "trade_time": datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")[:-3]
    }
    
    producer.send('stock_trades', event)
    print(f"Sent: {event}")
    time.sleep(0.1)  # 0.1초 간격으로 이벤트 전송

producer.flush()
print("Data generation complete!")
