# Kafka 프로듀서를 사용하기 위한 라이브러리 import
from kafka import KafkaProducer
import json  # 메시지를 JSON 형식으로 직렬화하기 위해 사용
import time  # 시간 지연을 위해 사용
from datetime import datetime, timedelta  # 타임스탬프 생성용
import random  # 임의 시간 생성을 위해 사용

# ---------------------------------------------
# Kafka Producer 객체 생성
# Kafka 브로커 주소를 명시하고, 메시지를 전송할 때 사용할 직렬화 방식 설정
# value_serializer: Python 객체를 Kafka에 전송 가능한 bytes 형식으로 변환
# 여기서는 JSON 문자열로 변환한 뒤, UTF-8 인코딩하여 전송함
# ---------------------------------------------
producer = KafkaProducer(
    bootstrap_servers=['localhost:9092'],  # Kafka 브로커 주소 (로컬에 실행 중인 Kafka)
    value_serializer=lambda v: json.dumps(v).encode('utf-8')  # JSON → bytes 변환
)

# ---------------------------------------------
# 기준 시간 설정: 현재 시각에서 5분 전을 기준으로 잡음
# 이 값을 기준으로 과거 시점의 메시지 타임스탬프를 생성할 예정
# ---------------------------------------------
base_time = datetime.now() - timedelta(minutes=5)

# ---------------------------------------------
# 총 30개의 메시지를 생성하여 Kafka로 전송
# 각 메시지는 랜덤한 시간대 (0~4분 전 사이)에 발생한 것처럼 설정됨
# ---------------------------------------------
for i in range(30):
    # 메시지 타임스탬프를 위해 0~4분 사이의 임의의 분, 초를 생성
    offset_minutes = random.randint(0, 4)   # 0~4분 중 하나 선택
    offset_seconds = random.randint(0, 59)  # 0~59초 중 하나 선택

    # 기준 시간 + 임의 offset → 최종 메시지 시간
    msg_time = base_time + timedelta(minutes=offset_minutes, seconds=offset_seconds)

    # 메시지 구성: id, 텍스트 메시지, 타임스탬프 포함
    message = {
        'id': i,  # 메시지 식별자 (0부터 29까지 증가)
        'message': f'테스트 메시지 {i}',  # 메시지 내용
        'timestamp': msg_time.strftime('%Y-%m-%d %H:%M:%S')  # 타임스탬프 (문자열 포맷)
    }

    # Kafka로 메시지 전송 (토픽명: 'test-topic')
    producer.send('test-topic', message)

    # 전송된 메시지 콘솔 출력 (디버깅 또는 학습용)
    print(f'전송된 메시지: {message}')

    # 너무 빠르게 전송되지 않도록 0.5초 대기
    # 실제 스트리밍 환경처럼 데이터를 천천히 흘려보내는 효과
    time.sleep(0.5)

# ---------------------------------------------
# 모든 메시지가 브로커에 정상적으로 전달되도록 flush() 호출
# 내부 버퍼에 남아있는 메시지를 강제로 전송하고 마무리
# ---------------------------------------------
producer.flush()
