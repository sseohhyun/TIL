# TMDB API 키 설정
import requests
import csv

from pprint import pprint

API_KEY = 'f8f401656006be0954fdb3470ef7914e'
REVIEW_BASE_URL = "https://api.themoviedb.org/3/movie/{}/reviews"

# 1. 영화 ID 목록 불러오기
with open('movie.csv', 'r', encoding='utf-8') as csvfile:
    reader = csv.DictReader(csvfile)
    movie_ids = [row['id'] for row in reader]

# 2. 리뷰 데이터를 저장할 리스트 선언
filtered_reviews = []

# 3. 영화별 리뷰 데이터 수집 (평점 5 이상만)
for movie_id in movie_ids:
    url = REVIEW_BASE_URL.format(movie_id)
    params = {
        'api_key': API_KEY,
        'language': 'en-US',
    }

    response = requests.get(url, params=params)

    
if response.status_code == 200:
    results = response.json().get('results', [])

    for review in results:
        rating = review['author_details'].get('rating')
    
        if rating is not None and rating >= 5:  # ⭐ 5점 이상 필터
            filtered_reviews.append({
                'review_id': review['id'],
                'movie_id': movie_id,
                'author': review['author'],
                'content': review['content'],
                'rating': rating
            })
else:
    print(f"❌ {movie_id} 리뷰 불러오기 실패:", response.status_code)

# 4. CSV 저장
fields = ['review_id', 'movie_id', 'author', 'content', 'rating']

with open("movie_reviews.csv", "w", newline="", encoding="utf-8") as file:
    writer = csv.DictWriter(file, fieldnames=fields)
    writer.writeheader()
    writer.writerows(filtered_reviews)

print("✅ 리뷰 데이터 저장 완료!")