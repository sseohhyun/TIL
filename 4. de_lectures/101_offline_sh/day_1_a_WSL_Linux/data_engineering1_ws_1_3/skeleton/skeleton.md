# 텍스트 파일 분석 및 필터링 실습
# 목표: grep, head, sort, uniq 명령어를 활용하여 로그에서 특정 키워드를 추출하고 정리하는 방법을 익힌다.

# [Step 1] 샘플 로그 파일 생성
# 실습을 위해 system.log라는 파일이 필요하므로, 다음 명령어로 임의 로그 데이터를 생성합니다.
# 각 줄은 로그 한 줄이며, 다양한 메시지 유형이 혼합되어 있습니다.
# EOF는 양 EOF 사이의 내용을 텍스트 입력으로 이용한다 라는 의미.
cat  <<EOF > system.log
[INFO] System boot complete
[ERROR] Failed to mount disk
[WARNING] CPU temperature high
[ERROR] Disk read error
[INFO] User login
[ERROR] Disk write error
[INFO] Shutdown initiated
[Disk] Disk scan complete
EOF

# [Step 2] "ERROR" 키워드를 포함하는 로그만 추출하여 저장
# grep 명령어를 이용해 "ERROR"가 포함된 줄만 찾아 error_logs.txt에 저장합니다.
grep "ERROR" system.log > error_logs.txt

# [Step 3] "Disk" 키워드를 포함하는 로그만 추출하여 저장
# 대소문자를 구분하지 않기 위해 "Disk"로 검색합니다.
grep "Disk" system.log > disk_logs.txt

# [Step 4] 추출된 로그의 앞 5줄만 미리 확인
# head 명령어를 사용하면 전체 파일을 보지 않고 앞부분만 간략히 확인할 수 있습니다.
head -n 5 error_logs.txt
head -n 5 disk_logs.txt

# [Step 5] 중복 제거 및 정렬
# 추출된 로그들 중 중복된 라인이 있을 수 있으므로, sort로 정렬한 뒤 uniq로 중복을 제거합니다.
# 결과는 *_sorted.txt 파일로 저장됩니다.
sort error_logs.txt | uniq > error_sorted.txt
sort disk_logs.txt | uniq > disk_sorted.txt

# [Step 6] 최종 결과 확인
# cat 명령어를 사용해 정리된 로그 파일을 확인합니다.
cat error_sorted.txt
cat disk_sorted.txt
