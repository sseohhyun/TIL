# Kibana에서 Air Quality 데이터 검색 실습

## 1. 실습용 데이터 로드  
- CSV 파일 (`Air_Quality.csv`)을 Elasticsearch에 적재  
- 인덱스명: **`air_quality`**

## 2. Discover에서 데이터 탐색  
- **Discover 메뉴에서 `air_quality` 인덱스 선택**  
- 주요 필드 확인:
  - `Start_Date`: 측정일 (날짜 필드)
  - `Geo_Place_Name.keyword`: 지역 이름
  - `Geo_Type_Name.keyword`: 지역 유형 (`Borough`, `CD`, `UHF42`, 등)
  - `Name.keyword`: 오염물질 이름 (`Ozone (O3)`, `SO2`, 등)
  - `Data_Value`: 측정값 (수치)

## 3. KQL을 활용한 검색 및 필터링

### Borough 지역만 필터링
```kql
Geo_Type_Name:Borough
```