# Elasticsearch가 실행된 상태에서 진행해야 합니다.

from elasticsearch import Elasticsearch
import subprocess
import time

# 재연결 함수 정의
def reconnect_to_alive_node(possible_hosts):
    for host in possible_hosts:
        try:
            es = Elasticsearch(host)
            if es.ping():
                print(f"{host} 연결 성공")
                return es
        except Exception:
            continue
    raise Exception("사용 가능한 Elasticsearch 노드가 없습니다.")

# 초기 연결
es = Elasticsearch("http://localhost:9200")

# 현재 노드 출력
print("현재 노드 상태:")
nodes_info = es.cat.nodes(format="json")
for node in nodes_info:
    print(f" - 이름: {node['name']}, 역할: {node['node.role']}, IP: {node['ip']}")

# 마스터 노드 확인
print("\n현재 마스터 노드:")
master = es.cat.master(format="json")[0]
master_node_name = master['node']
print(f" - 마스터 노드: {master_node_name}, IP: {master['ip']}")

# 마스터 노드에 해당하는 Docker 컨테이너 중지
# 기본 가정: node name == container name
print(f"\n마스터 노드 '{master_node_name}' 컨테이너 중지")
subprocess.run(["docker", "stop", master_node_name], check=True)

# 재연결
print("\n남은 노드로 재연결 시도 중...")
remaining_hosts = [
    "http://localhost:9200",
    "http://localhost:9201",
    "http://localhost:9202"
]
# 중지한 노드 제외
remaining_hosts = [host for host in remaining_hosts if not host.endswith(master['ip'].split('.')[-1])]
es = reconnect_to_alive_node(remaining_hosts)

# 대기 후 상태 재확인
time.sleep(5)
print("\n마스터 노드 중지 후 노드 상태:")
nodes_info = es.cat.nodes(format="json")
for node in nodes_info:
    print(f" - 이름: {node['name']}, 역할: {node['node.role']}, IP: {node['ip']}")

print("\n새 마스터 노드 확인:")
new_master = es.cat.master(format="json")[0]
print(f" - 새 마스터 노드: {new_master['node']}, IP: {new_master['ip']}")

# 마스터 노드 재시작
print(f"\n중지된 마스터 노드 '{master_node_name}' 재시작")
subprocess.run(["docker", "start", master_node_name], check=True)

# 재합류 대기
print(f"\n'{master_node_name}' 노드 재합류 대기 중...")
for i in range(30):
    nodes_info = es.cat.nodes(format="json")
    node_names = [node["name"] for node in nodes_info]
    if master_node_name in node_names:
        print(f"{master_node_name} 노드 클러스터에 재합류 완료")
        break
    time.sleep(1)
else:
    print(f"30초 내에 {master_node_name} 노드가 클러스터에 합류하지 못했습니다.")

# 최종 상태 출력
print("\n최종 클러스터 노드 상태:")
nodes_info = es.cat.nodes(format="json")
for node in nodes_info:
    print(f" - 이름: {node['name']}, 역할: {node['node.role']}, IP: {node['ip']}")

print("\n최종 마스터 노드:")
final_master = es.cat.master(format="json")[0]
print(f" - 마스터 노드: {final_master['node']}, IP: {final_master['ip']}")
