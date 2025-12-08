# Kibana Dev Tools - Nested Query 실습

## 실습 목적
Kibana를 통해 Elasticsearch의 `nested` 타입 필드를 활용하여 문서 내 배열 형태의 객체 필드를 효율적으로 검색하는 방법을 실습합니다.

---

## 1. 기존 인덱스 삭제
```http
DELETE nested_test
```

---

## 2. 새로운 인덱스 생성 및 매핑 설정 (nested 필드 포함)
```json
PUT nested_test
{
  "mappings": {
    "properties": {
      "title": {
        "type": "text"
      },
      "reviews": {
        "type": "nested",
        "properties": {
          "author": { "type": "keyword" },
          "rating": { "type": "integer" },
          "comment": { "type": "text" }
        }
      }
    }
  }
}
```

---

## 3. Bulk를 활용한 샘플 데이터 삽입
```json
POST _bulk
{ "index": { "_index": "nested_test", "_id": "1" } }
{ "title": "Elasticsearch Advanced Guide", "reviews": [ { "author": "Alice", "rating": 5, "comment": "Excellent book!" }, { "author": "Bob", "rating": 3, "comment": "Decent but could be improved." } ] }
{ "index": { "_index": "nested_test", "_id": "2" } }
{ "title": "Mastering Elasticsearch", "reviews": [ { "author": "Charlie", "rating": 4, "comment": "Great for advanced users." }, { "author": "David", "rating": 2, "comment": "Too complex for beginners." } ] }
{ "index": { "_index": "nested_test", "_id": "3" } }
{ "title": "Introduction to Elasticsearch", "reviews": [ { "author": "Eve", "rating": 5, "comment": "A great starting point!" }, { "author": "Frank", "rating": 3, "comment": "Covers the basics well." } ] }
{ "index": { "_index": "nested_test", "_id": "4" } }
{ "title": "Elasticsearch Deep Dive", "reviews": [ { "author": "Grace", "rating": 4, "comment": "Very in-depth and useful." }, { "author": "Hank", "rating": 5, "comment": "Best resource for Elasticsearch!" } ] }
{ "index": { "_index": "nested_test", "_id": "5" } }
{ "title": "Practical Elasticsearch", "reviews": [ { "author": "Ivy", "rating": 3, "comment": "Good but lacks examples." }, { "author": "Jack", "rating": 4, "comment": "Practical and insightful." } ] }
```

---

## 4. Nested Query를 이용한 특정 조건 검색
> **Alice가 작성한 리뷰 중 평점이 5 이상인 문서 검색**
```json
GET nested_test/_search
{
  "query": {
    "nested": {
      "path": "reviews",
      "query": {
        "bool": {
          "must": [
            { "match": { "reviews.author": "Alice" } },
            { "range": { "reviews.rating": { "gte": 5 } } }
          ]
        }
      },
      "inner_hits": {}
    }
  }
}
```

---

## 5. 특정 책의 리뷰 중 평점이 4 이상인 리뷰만 조회
```json
GET nested_test/_search
{
  "query": {
    "nested": {
      "path": "reviews",
      "query": {
        "bool": {
          "must": [
            { "range": { "reviews.rating": { "gte": 4 } } }
          ]
        }
      },
      "inner_hits": {}
    }
  }
}
```

---

## 6. 인덱스 매핑 정보 확인
```http
GET nested_test/_mapping?pretty
```

---

## 7. 전체 데이터 조회 (확인용)
```http
GET nested_test/_search?size=10
```
