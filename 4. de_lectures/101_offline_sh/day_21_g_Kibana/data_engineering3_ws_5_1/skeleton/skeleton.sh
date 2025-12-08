# Docker-compose를 통해 elasticsearch와 연동되는 kibana를 띄우고 kibana가 올바르게 접속되는지 확인합니다.

docker-compose up -d


# kibana:
#     image: docker.elastic.co/kibana/kibana:8.17.1
#     container_name: kibana
#     depends_on:
#       es01:
#         condition: service_healthy
#     environment:
#       - SERVER_NAME=kibana
#       - ELASTICSEARCH_HOSTS=http://es01:9200
#       - XPACK_ALERTING_ENABLED=false
#       - XPACK_ACTIONS_ENABLED=false
#       - XPACK_RULE_REGISTRY_WRITE_ENABLED=false
#       - TELEMETRY_ENABLED=false
#       - XPACK_SECURITY_SOLUTION_ENABLED=false
#       - XPACK_INFRA_ENABLED=false
#       - XPACK_LOGS_ENABLED=false
#       - XPACK_ALERTING_ENABLED=false
#       - XPACK_APM_ENABLED=false
#       - XPACK_FLEET_ENABLED=false
#       - XPACK_SECURITY_SOLUTION_ENABLED=false
#       - XPACK_OBSERVABILITY_ENABLED=false
#       - XPACK_REPORTING_ENABLED=false
#       - XPACK_ML_ENABLED=false
#       - TELEMETRY_ENABLED=false
#       - MONITORING_ENABLED=false
#     ports:
#       - 5601:5601
#     networks:
#       - elastic
