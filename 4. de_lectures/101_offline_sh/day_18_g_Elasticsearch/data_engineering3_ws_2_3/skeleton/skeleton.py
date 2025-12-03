from elasticsearch import Elasticsearch
import time
import json

# 노드 조합 리스트: 실험에 사용할 노드 개수와 포함시킬 노드 이름
node_configurations = {
    1: ["es01"],
    2: ["es01", "es02"],
    3: ["es01", "es02", "es03"]
}

# Bulk JSON 경로
bulk_file_path = "../data/ecommerce.json"

# 클라이언트 연결
es = Elasticsearch("http://localhost:9200")

# 노드 개수별 실험
for node_count, node_names in node_configurations.items():
    print(f"\n 실험: 노드 수 = {node_count}개 → 사용 노드: {node_names}")

    # ----------------------------------------------
    # 1. 기존 인덱스 삭제
    # ----------------------------------------------
    if es.indices.exists(index="ecommerce"):
        es.indices.delete(index="ecommerce")  
        print("기존 인덱스 삭제 완료")

    # ----------------------------------------------
    # 2. 샤드 할당 노드 제한
    # ----------------------------------------------
    # TODO: transient 설정을 사용하여 샤드 할당 노드를 제한
    es.cluster.put_settings(body={
        "transient": {
            "cluster.routing.allocation.include._name": ",".join(node_names)
        }
    })
    print(f"샤드 할당 대상 노드 제한: {','.join(node_names)}")

    time.sleep(2)  # 설정 반영 대기

    # ----------------------------------------------
    # 3. 인덱스 생성 (샤드 3, 복제본 1)
    # ----------------------------------------------
    es.indices.create(index="ecommerce",
        body = {
            "settings": {
                "index": {
                    "number_of_shards": 3,
                    "number_of_replicas": 1
                }
            }
        })  
    print("인덱스 생성 완료")

    # ----------------------------------------------
    # 4. Bulk 데이터 삽입
    # ----------------------------------------------
    with open(bulk_file_path, "r", encoding="utf-8") as f:
        bulk_data = f.read()

    # TODO: Bulk API를 통해 데이터 삽입
    res = es.bulk(body = bulk_data)  
    if not res["errors"]:
        print("Bulk 데이터 삽입 완료")
    else:
        print("Bulk 삽입 중 오류 발생")

    time.sleep(2)  # 색인 완료 대기

    # ----------------------------------------------
    # 5. 캐시 제거 (공정한 속도 측정)
    # ----------------------------------------------
    es.indices.clear_cache(index="ecommerce", fielddata=True, query=True, request=True)
    time.sleep(1)

    # ----------------------------------------------
    # 6. 검색 쿼리 및 속도 측정
    # ----------------------------------------------
    query = {
        "query": {
            "match_all": {}
        }
    }

    start = time.time()
    # TODO: ecommerce 인덱스에 위의 쿼리로 검색 실행
    es.search(index="ecommerce", body=query)  
    end = time.time()

    elapsed_ms = int((end - start) * 1000)
    print(f"검색 시간 ({node_count} 노드): {elapsed_ms}ms")

# ----------------------------------------------
# 마지막 단계: 샤드 제한 초기화
# ----------------------------------------------
# TODO: 클러스터 샤드 제한 해제
es.cluster.put_settings(body={
    "transient": {
        "cluster.routing.allocation.include._name": "*"
    }
})
print("\n샤드 제한 초기화 완료")
