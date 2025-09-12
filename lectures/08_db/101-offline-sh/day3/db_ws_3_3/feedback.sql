USE online_course_platform_db;

-- 'john_doe' 학생이 작성한 가장 오래된 피드백의 내용을 검색하는 SQL 쿼리를 작성하시오.
SELECT f.comment
FROM feedback f
INNER JOIN students s
 ON f.student_id = s.id
WHERE s.username = "john_doe"
ORDER BY f.created_at ASC
LIMIT 1;

DROP VIEW views

-- 특정 학생이 작성한 모든 피드백과 해당 코스의 제목을 포함하는 뷰를 생성하는 SQL 문장을 작성하시오.
CREATE VIEW Views AS
SELECT s.username, c.title, f.comment, f.created_at
FROM feedback f
INNER JOIN students s
 ON s.id = f.student_id
INNER JOIN courses c
 ON c.id = f.course_id
ORDER BY s.id ASC;

-- 결과화면 3은 생성한 View로 전체 조회시 확인 가능한 정보이다.
SELECT * FROM Views;

-- 생성한 뷰를 사용하여 'john_doe' 학생이 작성한 모든 피드백과 해당 코스의 제목을 조회하는 SQL 쿼리를 작성하시오.
SELECT * 
FROM Views
WHERE username = "john_doe";