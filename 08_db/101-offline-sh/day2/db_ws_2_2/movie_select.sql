USE movies;

-- 개봉 연도가 2010년 이후인 영화 목록을 조회하시오.
SELECT *
FROM movie_list
WHERE release_year > 2010;

-- 장르가 'Action' 또는 'Sci-Fi'인 영화 목록을 조회하시오.
SELECT *
FROM movie_list
WHERE genre in ('Action', 'Sci-Fi');

-- 영화 제목에 'The'가 포함된 영화를 조회하시오.
SELECT *
FROM movie_list
WHERE title LIKE "%The%";

-- 개봉 연도가 2008년부터 2014년 사이인 영화 목록을 조회하시오.
SELECT *
FROM movie_list
WHERE release_year BETWEEN 2008 AND 2014;

-- 영화 목록에서 개봉 연도가 NULL인 영화를 조회하시오.
SELECT *
FROM movie_list
WHERE release_year IS NULL;