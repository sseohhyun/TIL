# problem_d.py

import requests
import csv

API_KEY = 'f8f401656006be0954fdb3470ef7914e'
CREDITS_BASE_URL = "https://api.themoviedb.org/3/movie/{}/credits"

# movie.csv 파일에서 movie_id 목록 불러오기
with open('movie.csv', 'r', encoding='utf-8') as f:
    reader = csv.DictReader(f)
    movie_ids = [row['id'] for row in reader]

# 출연진 정보를 저장할 리스트
cast_list = []

for movie_id in movie_ids:
    url = CREDITS_BASE_URL.format(movie_id)
    params = {
        'api_key': API_KEY,
        'language': 'ko-KR'
    }

    response = requests.get(url, params=params)
    if response.status_code == 200:
        data = response.json()
        casts = data.get('cast', [])

        for cast in casts:
            if cast['order'] <= 10:
                character_clean = cast['character'].replace('\n', ' ').replace('\r', ' ') if cast.get('character') else ''
                
                cast_info = {
                    'cast_id': cast['cast_id'],
                    'movie_id': movie_id,
                    'name': cast['name'],
                    'character': character_clean,
                    'order': cast['order']
                }
                cast_list.append(cast_info)
    else:
        print(f"❌ 출연진 정보 요청 실패 (movie_id: {movie_id}) - status: {response.status_code}")

# CSV로 저장
fieldnames = ['cast_id', 'movie_id', 'name', 'character', 'order']

with open('movie_cast.csv', 'w', newline='', encoding='utf-8') as f:
    writer = csv.DictWriter(f, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(cast_list)