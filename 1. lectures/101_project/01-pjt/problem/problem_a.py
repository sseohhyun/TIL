import requests
from pprint import pprint

# TMDB API 키 설정
API_KEY = 'f8f401656006be0954fdb3470ef7914e'
BASE_URL = 'https://api.themoviedb.org/3/movie/popular'


# API 호출 함수
params = {
    'api_key': API_KEY,
    'language': 'ko-KR',
    # 'page': 1
}

response = requests.get(BASE_URL, params=params)


if response.status_code == 200:
    data = response.json()
    movies = data['results']  # ✅ 여기서 진짜 영화 리스트 추출

    completed_popularity_movie = []
    fields = ['id', 'title', 'release_date', 'popularity']

    for item in movies:
        temp_item = {key: item[key] for key in fields}
        completed_popularity_movie.append(temp_item)

    pprint(completed_popularity_movie)

else:
    print('API 호출 실패:', response.status_code)
    


# 응답 확인 및 출력

# 영화 데이터 처리 함수

# 데이터 수집 및 CSV 파일로 저장

import csv

# 저장할 파일 이름
filename = 'movies.csv'

# CSV 파일로 저장
with open(filename, 'w', newline='', encoding='utf-8') as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames=['id', 'title', 'release_date', 'popularity'])
    writer.writeheader()  # 헤더 작성
    writer.writerows(completed_popularity_movie)  # 영화 데이터 쓰기

print(f'✅ CSV 저장 완료: {filename}')
    

