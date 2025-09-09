USE movies;

-- 가장 많은 영화를 보유한 장르를 조회하시오.
SELECT genre
FROM movie_list
GROUP BY genre
ORDER BY COUNT(*) DESC
LIMIT 1;

-- 장르별 영화의 개수와 평균 개봉 연도를 조회하시오.
SELECT genre, COUNT(*) AS movie_count, AVG(release_year) AS avg_release_year
FROM movie_list
GROUP BY genre;

-- 장르별로 가장 최근에 개봉한 영화의 제목과 개봉 연도를 조회하시오.
SELECT main.genre, main.title, main.release_year
FROM movie_list as main
WHERE main.release_year = (
  SELECT MAX(sub.release_year)
  FROM movie_list as sub
  WHERE sub.genre = main.genre
);

-- 개봉 연도가 'Action' 장르 영화의 최소 개봉 연도와 같은 다른 장르의 영화를 개봉 연도와 제목으로 정렬하여 조회하시오.
SELECT *
FROM movie_list
WHERE genre != "Action"
  AND release_year = (
    SELECT release_year
    FROM movie_list
    WHERE genre = "Action"
    ORDER BY release_year ASC
    LIMIT 1)
ORDER BY release_year ASC, title ASC;

-- 모든 'Drama' 장르의 영화와 같은 개봉 연도를 가진 'Sci-Fi' 또는 'Action' 장르의 영화를 개봉 연도 순으로 정렬하여 조회하시오.
SELECT *
FROM movie_list
WHERE genre != "Drama"
  AND release_year in (
    SELECT release_year
    FROM movie_list
    WHERE genre = "Drama")
ORDER BY release_year ASC;