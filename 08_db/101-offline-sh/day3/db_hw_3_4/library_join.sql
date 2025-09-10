USE library_db;

-- INNER JOIN을 수행하는 데 필요한 인덱스를 생성하여 검색 속도를 최적화하시오.
  -- authors 테이블의 name 컬럼에 대한 인덱스
CREATE INDEX idx_authors_name
ON authors(name);
  -- genres 테이블의 genre_name 컬럼에 대한 인덱스
CREATE INDEX idx_genres_genre_name
ON genres(genre_name);

-- INNER JOIN을 사용하여 책의 제목, 저자 이름, 장르 이름을 모두 포함하는 조회문을 작성하시오.
SELECT 
  b.title AS BookTitle, 
  a.name AS AuthorName,
  g.genre_name AS GenreName
FROM books b
INNER JOIN authors a
  ON b.author_id = a.id 
INNER JOIN genres g
  ON b.genre_id = g.id;
ORDER BY b.id;

  -- 작가 이름이 'J.K. Rowling' 이고, 장르가 'Fantasy'인 데이터의 책의 제목, 저자 이름, 장르 이름을 출력.
SELECT 
  b.title AS BookTitle, 
  a.name AS AuthorName,
  g.genre_name AS GenreName
FROM books b
INNER JOIN authors a
  ON b.author_id = a.id 
INNER JOIN genres g
  ON b.genre_id = g.id
WHERE g.genre_name = "Fantasy" AND a.name = "J.K. Rowling"
ORDER BY b.id;