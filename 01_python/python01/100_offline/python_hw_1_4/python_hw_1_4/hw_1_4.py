'''
학생 점수 정보
   "Alice" = 85,
   "Bob" = 78,
   "Charlie" = 92,
   "David" = 88,
   "Eve" = 95
'''

'''
1) 모든 학생의 평균 점수를 계산하여 출력하시오.
2) 80점 이상을 받은 학생들의 이름을 리스트 컴프리헨션을 사용하여 추출하시오.
3) 학생들의 점수를 높은 순서대로 정렬하여 출력하시오.
4) 점수가 가장 높은 학생과 가장 낮은 학생의 점수 차이를 계산하여 출력하시오.
5) 각 학생의 점수가 평균 점수보다 높은지 낮은지를 판단하여, 낮은 학생의 이름과 성적을 함께 출력하시오
'''

# 아래에 코드를 작성하시오.

### 1번 ###
dct = {"Alice" : 85,
   "Bob" : 78,
   "Charlie" : 92,
   "David" : 88,
   "Eve" : 95}

print("1. 학생들의 이름과 점수를 딕셔너리에 저장")
print("students type:", end= " ")
print(type(dct))
print(f"학생들의 이름과 점수 : {dct}")

### 2번 ###
sm = 0
for lst in dct.keys():
    sm += int(dct[lst])
avg = sm / len(dct.values())
print("2. 모든 학생의 평균 점수 : %.2f"%avg)

### 3번 ###
lst_80_up = []
for lst in dct.keys(): 
    if int(dct[lst]) >= 80:
      lst_80_up.append(lst)
print(f'3. 기준 점수(80점) 이상을 받은 학생 수 : {lst_80_up}')

### 4번 ###
print("4. 점수 순으로 정렬 :")
dct_sort = sorted(dct.items(), key=lambda item : item[1], reverse=True)
for stu, sco in dct_sort :
   print(f'{stu} : {sco}')

### 5번 ###
scorea_max = max(dct.values())
scorea_min = min(dct.values())
print(f'5. 점수가 가장 높은 학생과 가장 낮은 학생의 점수 차이 : {scorea_max - scorea_min}')

### 6번 ###
print(f'6. 각 학생의 점수가 평균보다 높은지 낮은지 판단 : ')
for lst in dct.keys():
   if int(dct[lst]) >= avg:
      print(f'{lst} 학생의 점수({int(dct[lst])})는 평균 이상입니다.')
   else :
      print(f'{lst} 학생의 점수({int(dct[lst])})는 평균 이하입니다.')
