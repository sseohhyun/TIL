# Kibana KQL 실습 가이드

## 목적
Kibana Dev Tools와 Discover에서 Elasticsearch 인덱스 데이터를 조회하고, KQL(Kibana Query Language)을 활용한 다양한 검색 조건을 실습합니다.

---

## 1. Elasticsearch 인덱스 생성 및 데이터 삽입

### 기존 인덱스 삭제
```http
DELETE kibana_kql_test
```

### 인덱스 생성 및 매핑
```json
PUT kibana_kql_test
{
  "mappings": {
    "properties": {
      "user": { "type": "keyword" },
      "role": { "type": "keyword" },
      "message": { "type": "text" },
      "status": { "type": "keyword" },
      "age": { "type": "integer" },
      "created_at": { "type": "date" }
    }
  }
}
```

### 샘플 데이터 Bulk 삽입
```json
POST _bulk
{ "index": { "_index": "kibana_kql_test", "_id": "1" } }
{ "user": "Alice", "role": "admin", "message": "System updated successfully", "status": "success", "age": 32, "created_at": "2025-02-22T12:30:00" }
{ "index": { "_index": "kibana_kql_test", "_id": "2" } }
{ "user": "Bob", "role": "user", "message": "Login attempt failed", "status": "failure", "age": 28, "created_at": "2025-02-22T13:00:00" }
{ "index": { "_index": "kibana_kql_test", "_id": "3" } }
{ "user": "Charlie", "role": "admin", "message": "New user registered", "status": "success", "age": 45, "created_at": "2025-02-22T14:15:00" }
{ "index": { "_index": "kibana_kql_test", "_id": "4" } }
{ "user": "David", "role": "moderator", "message": "Post deleted by moderator", "status": "success", "age": 35, "created_at": "2025-02-22T15:45:00" }
{ "index": { "_index": "kibana_kql_test", "_id": "5" } }
{ "user": "Eve", "role": "user", "message": "Password reset requested", "status": "pending", "age": 29, "created_at": "2025-02-22T16:10:00" }
{ "index": { "_index": "kibana_kql_test", "_id": "6" } }
{ "user": "Frank", "role": "user", "message": "Account locked due to multiple failures", "status": "failure", "age": 40, "created_at": "2025-02-22T16:30:00" }
```

---

## 2. KQL 검색 실습

### 특정 사용자 검색
```kql
user: "Alice"
```

### 여러 필드 조건 검색 (AND)
```kql
user: "Alice" and role: "admin"
```

### 여러 값 검색 (OR)
```kql
role: ("admin" or "moderator")
```

### 부분 일치 검색
```kql
message: *success*
```

### 숫자 필터링
```kql
age > 30
```

### 숫자 범위 검색
```kql
age >= 30 and age <= 40
```
