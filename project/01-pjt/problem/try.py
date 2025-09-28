from pprint import pprint
import csv

movie_rating_dist = {}

with open('C:\\Users\\SSAFY\\Desktop\\01-pjt\\DB\\movie_reviews.csv', 'r', encoding='utf-8') as vote:
    reader = csv.DictReader(vote)

    for row in reader:
        movie_id = row['movie_id']
        rating = row['rating']

        if rating:
            rating = float(rating)

            # 영화 ID에 대한 딕셔너리 없으면 초기화
            if movie_id not in movie_rating_dist:
                movie_rating_dist[movie_id] = {}

            # 해당 평점 카운트
            if rating in movie_rating_dist[movie_id]:
                movie_rating_dist[movie_id][rating] += 1
            else:
                movie_rating_dist[movie_id][rating] = 1


# 출력 확인
for movie_id, dist in movie_rating_dist.items():
    print(f"{movie_id}: {dist}")