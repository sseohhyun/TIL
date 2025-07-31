# 암호를 딕셔너리로 저장
# 뒤에서부터 1이 있는지 확인해서 56개 슬라이싱
# 암호코드 스캔 문제도 연계해서 한번 풀어보기 _ 어려워보여...



T = int(input())

for t_c in range(1, T+1):
    n, m = map(int, input().split())
    arr = [list(map(str, input())) for _ in range()]