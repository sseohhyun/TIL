USE movies;

INSERT INTO movie_list(title, genre, release_year)
VALUES
('The Matrix', 'Sci-Fi', 1999),
('Gladiator', 'Action', 2000),
('Jurassic Park', 'Sci-Fi', 1993),
('The Fugitive', 'Action', 1993);

-- 'Drama' 장르의 영화 중 개봉 연도가 가장 빠른 영화의 제목을 조회하시오.
SELECT title
FROM movie_list
WHERE genre = "Drama"
ORDER BY release_year IS NULL, release_year ASC
LIMIT 1;

-- 2000년 이후에 개봉된 영화들 중 개봉 연도가 가장 늦은 'Action' 장르 영화의 제목과 개봉년도를 조회하시오.
SELECT title, release_year
FROM movie_list
WHERE release_year >= 2000 AND genre = "Action"
ORDER BY release_year DESC
LIMIT 1;

-- 'Drama' 장르의 영화와 개봉 연도가 같은 'Sci-Fi' 또는 'Action' 장르의 영화 목록을 조회하시오.
SELECT *
FROM movie_list
WHERE genre in ('Sci-Fi', 'Action') 
  AND release_year in (SELECT release_year FROM movie_list WHERE genre = "Drama");

-- 모든 'Action' 장르의 영화 개봉 연도의 평균보다 더 늦게 개봉한 'Sci-Fi' 장르의 영화 목록을 조회하시오.
SELECT *
FROM movie_list
WHERE genre = "Sci-Fi" AND release_year > (SELECT AVG(release_year) 
  FROM movie_list 
  WHERE genre = "Action");

-- 개봉 연도가 'Action' 장르 영화의 최소 개봉 연도와 같은 다른 장르의 영화를 조회하시오.
SELECT *
FROM movie_list
WHERE genre != "Action" 
  AND release_year = (SELECT release_year 
    FROM movie_list 
    WHERE genre = "Action" 
    ORDER BY release_year 
    LIMIT 1);

