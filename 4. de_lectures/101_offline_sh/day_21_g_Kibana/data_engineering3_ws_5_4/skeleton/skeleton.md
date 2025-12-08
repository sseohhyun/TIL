# Kibana Dashboard 생성 및 관리 (Air Quality 데이터 기준)

## 1. 개요
Kibana의 Dashboard를 활용하여 대기 질 데이터를 시각화하고 분석하는 방법을 학습한다.  
이 실습을 통해 `air_quality` 인덱스를 기반으로 대시보드를 생성하고 유용한 시각화 패널을 구성하는 방법을 익힐 수 있다.

---

## 2. 실습 내용

### 2.1 새로운 Dashboard 생성
- **Air Quality Dashboard**를 생성한다.

---

### 2.2 시각화 추가 후 Save

- **Line Chart**  
  - X축: `@timestamp` (날짜 기준)  
  - Y축: `avg(Data_Value)`  
  - 설명: 전체 지역의 평균 오염도 시계열 추이
 
---

### 2.3 대시보드 필터 적용

- **날짜 필터링**  
  - 최근 5년 데이터만 표시 (예: `"2010-01-01" 부터 2020-05-15`)


---