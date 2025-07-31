# 주어진 input_list에서 모든 부분 집합을 생성하는 함수
def create_subset(depth, included):
    if depth == len(input_list): # 재귀 호출 깊이가 input_list의 길이와 같아지면
        cnt_subset = [input_list[i] for i in range(len(input_list)) if included[i]] # 포함된 요소들로 부분 집합 생성
        subsets.append(cnt_subset) # 생성된 부분 집합을 subsets 리스트에 추가
        return
    
    # 현재 요소를 포함하지 않는 경우
    included[depth] = False
    create_subset(depth + 1, included) # 다음 깊이로 재귀 호출

    # 현재 요소를 포함하는 경우
    included[depth] = True
    create_subset(depth + 1, included) # 다음 깊이로 재귀 호출


input_list = [1, 2, 3] # 부분 집합을 생성할 입력 리스트
subsets = [] # 모든 부분 집합을 저장할 리스트
init_included = [False] * len(input_list) # 각 요소의 포함 여부를 저장할 리스트 초기화
create_subset(0, init_included) 
print(subsets) 