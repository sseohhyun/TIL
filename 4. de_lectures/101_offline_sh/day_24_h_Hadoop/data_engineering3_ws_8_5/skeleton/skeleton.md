# Kibana를 활용한 금융 데이터 시각화 실습

## 실습 내용
CSV 형식의 금융 데이터를 Elasticsearch에 업로드하면, Kibana에서 이를 시계열 또는 집계 시각화로 표현할 수 있다. 거래량을 라인그래프로 시각화해보는 기본 예제를 실습한다.

## 수행 순서
- Elasticsearch에 `transactions.csv` 데이터를 업로드한다.
- Kibana에서 Index Pattern을 생성하고 Discover 탭에서 데이터 확인
- Lens를 활용해 거래량 시각화 수행

## 요구 사항

1. Kibana에 접속하여 이전에 구성한 finance index를 통해 `finance-kibana` Index Pattern을 생성하세요.

2. 시각화 탭에서 모든 거래 `amount`를 시간순으로 Line Chart로 시각화하세요.
