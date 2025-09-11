-- 모든 사용자의 이름과 이메일을 조회하는 SQL 쿼리를 작성하시오.
SELECT name, email 
FROM users;

-- '홍길동' 사용자가 작성한 모든 게시물의 제목과 내용을 조회하는 SQL 쿼리를 작성하시오.
SELECT title, content
FROM posts
WHERE user_id = 1;

-- '첫 번째 게시물'에 달린 모든 댓글의 내용을 조회하는 SQL 쿼리를 작성하시오.
SELECT content
FROM comment
WHERE post_id = (
  SELECT post_id 
  FROM posts 
  WHERE title = "첫 번째 게시글");

-- 새로운 사용자를 사용자 테이블에 삽입하는 SQL 쿼리를 작성하시오.
INSERT INTO users(name, email) 
VALUES ('김서현', 'seohyun@example.com');

-- '이순신' 사용자의 이메일을 'new_lee@example.com'으로 수정하는 SQL 쿼리를 작성하시오.
UPDATE users
SET email = "new_lee@example.com"
WHERE name = "이순신";