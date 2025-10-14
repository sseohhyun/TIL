import csv
import requests

API_KEY = 'f8f401656006be0954fdb3470ef7914e'
RATING_BASE_URL = "https://api.themoviedb.org/3/movie/{}"

# ===== 1. 평점 분포 만들기 =====
movie_rating_dist = {}

with open('C:/Users/SSAFY/Desktop/01-pjt/problem/movie_reviews.csv', 'r', encoding='utf-8') as vote:
    reader = csv.DictReader(vote)

    for row in reader:
        movie_id = row['movie_id']
        rating = row['rating']
        if rating:
            rating = float(rating)

            if movie_id not in movie_rating_dist:
                movie_rating_dist[movie_id] = {}

            if rating in movie_rating_dist[movie_id]:
                movie_rating_dist[movie_id][rating] += 1
            else:
                movie_rating_dist[movie_id][rating] = 1

# ===== 2. 영화 ID 읽기 =====
with open('C:/Users/SSAFY/Desktop/01-pjt/problem/movie.csv', 'r', encoding='utf-8') as csvfile:
    reader = csv.DictReader(csvfile)
    movie_ids = [row['id'] for row in reader]

# ===== 3. TMDB API 호출 + 평점 분포 병합 =====
completed_detail = []
for movie_id in movie_ids:
    url = RATING_BASE_URL.format(movie_id)
    params = {
        'api_key': API_KEY,
        'language': 'ko-KR',
    }
    response = requests.get(url, params=params).json()

    fields = ['id', 'vote_average', 'vote_count']
    temp_item = {}

    for key in fields:
        temp_item[key] = response.get(key)

    # 평점 분포 문자열로 변환 ('8.0:3, 9.0:1' 형태)
    rating_dist = movie_rating_dist.get(movie_id, {})
    temp_item['rating_distribution'] = rating_dist

    completed_detail.append(temp_item)

# ===== 4. CSV로 저장 =====
output_fields = ['id', 'vote_average', 'vote_count', 'rating_distribution']
with open("movie_ratings.csv", "w", newline="", encoding="utf-8") as file:
    writer = csv.DictWriter(file, fieldnames=output_fields)
    writer.writeheader()
    writer.writerows(completed_detail)
