# TMDB API 키 설정
import requests
from pprint import pprint
import csv


API_KEY = 'f8f401656006be0954fdb3470ef7914e'
DETAIL_BASE_URL = "https://api.themoviedb.org/3/movie/{}"

# 파일을 읽어서 movie_id 넣기
with open('movie.csv', 'r', encoding='utf-8') as csvfile:
    reader = csv.DictReader(csvfile)
    movie_ids = [row['id'] for row in reader]

# 각 영화의 상세 정보 가져오기

completed_detail = [] # 최종 결과물을 담을 리스트
for movie_id in movie_ids:
    url = DETAIL_BASE_URL.format(movie_id)
    params = {
        'api_key': API_KEY,
        'language': 'ko-KR',
    }
    response = requests.get(url, params=params).json()

    fields = ['id','budget','revenue','runtime','genres']

    temp_item = {}
    for key in fields:
        if key == 'genres':
            a = []
            for dct in response[key]:
                a.append(dct['name'])
            temp_item[key] = a

        else :
            temp_item[key] = response[key]

    completed_detail.append(temp_item)
print(completed_detail)





# 데이터 수집 및 CSV 파일로 저장
with open("movie_details.csv", "w", newline="", encoding="utf-8") as file:
    writer = csv.DictWriter(file, fields)
    writer.writeheader()
    writer.writerows(completed_detail)

