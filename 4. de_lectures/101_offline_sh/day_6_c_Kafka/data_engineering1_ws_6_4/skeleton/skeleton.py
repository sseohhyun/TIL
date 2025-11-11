"""
Kafka 브로커의 주요 성능 데이터를 수집하고 분석하는 스크립트입니다.

기능:
1. Prometheus API를 호출하여 Kafka 브로커 메트릭 수집
2. 수집된 데이터를 기반으로 성능 평가
"""

import requests  

PROMETHEUS_URL = "http://localhost:9090/api/v1/query"  # Prometheus API 주소

# ==============================
# 메트릭 수집 함수
# ==============================
def get_broker_metrics():
    """
    Prometheus API를 호출하여 Kafka 브로커의 주요 메트릭(메시지 처리율, 누적 메시지 수)을 수집합니다.

    Returns:
        dict: {
            "message_rate": float,
            "message_count": float
        }
    """
    queries = {
        "message_rate": 'kafka_server_BrokerTopicMetrics_MeanRate{name="MessagesInPerSec"}',
        "message_count": 'kafka_server_BrokerTopicMetrics_Count{name="MessagesInPerSec"}'
    }

    metrics = {}
    for key, query in queries.items():
        try:
            response = requests.get(PROMETHEUS_URL, params={"query": query}, timeout=3)
            response.raise_for_status()
            data = response.json()

            if "data" in data and "result" in data["data"]:
                values = [float(metric["value"][1]) for metric in data["data"]["result"]]
                metrics[key] = sum(values)
            else:
                metrics[key] = 0.0

        except Exception as e:
            print(f"[WARN] Prometheus 쿼리 실패 ({key}): {e}")
            metrics[key] = None

    return metrics

# ==============================
# 성능 분석 함수
# ==============================
def analyze_broker_performance():
    """
    수집된 메트릭을 기반으로 Kafka 브로커의 성능을 평가합니다.
    """
    metrics = get_broker_metrics()
    rate = metrics.get("message_rate")
    total = metrics.get("message_count")

    if rate is None or total is None:
        print("메트릭 수집 실패 - Prometheus 연결 상태를 확인하세요.")
        return

    print("Kafka 브로커 성능 분석 결과:")
    if rate > 5000:
        print("메시지 처리 속도 매우 높음 → 클러스터 확장 고려")
    elif rate > 1000:
        print("메시지 처리 속도 양호함")
    else:
        print("메시지 처리 속도 낮음 → 트래픽 점검 필요")

    print(f"현재 처리 속도: {rate:.2f} msgs/sec")
    print(f"누적 처리량: {total:.0f} msgs")



if __name__ == "__main__":
    analyze_broker_performance()