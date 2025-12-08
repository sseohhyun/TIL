# Kibana를 통한 Data Views 연결

## 1. 개요  
Kibana에서 Elasticsearch 데이터를 사용하기 위해 **Data Views**를 설정하는 방법을 학습한다.  
이 실습을 통해 Kibana에서 `air_quality` 인덱스를 기반으로 데이터를 연결하고 Discover에서 검색할 수 있다.

---

## 2. 실습 내용

### 2.1 기존 Data Views 확인
- Kibana 좌측 메뉴에서 `Stack Management → Data Views` 메뉴로 이동한다.
- 기존에 `air_quality` 관련 뷰가 있는지 확인한다.

---

### 2.2 새로운 Data View 생성

1. **“Create data view”** 버튼 클릭  
2. 아래와 같이 입력:

| 항목 | 값 |
|------|----|
| **Name** | `air_quality` |
| **Index pattern** | `air_quality` |
| **Timestamp field** | `@timestamp`|

3. 하단 또는 상단의 **Create data view** 버튼 클릭

---

## 3. 데이터 확인

- Discover 메뉴로 이동
- 상단의 Data View 선택에서 `air_quality`를 선택
- 다음 필드들이 존재하는지 확인:
  - `@timestamp` (또는 `Start_Date`)
  - `Geo_Place_Name`, `Geo_Type_Name`
  - `Name` (오염물질명), `Data_Value` (수치)

---
