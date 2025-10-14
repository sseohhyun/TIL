USE online_course_platform_db;

-- INNER JOIN을 사용하여 'john_doe' 학생이 작성한 코스 피드백과 해당 코스의 제목을 검색하는 SQL 쿼리를 작성하시오.
SELECT s.username, c.title, f.COMMENT
FROM feedback f
INNER JOIN students s
  ON s.id = f.student_id
INNER JOIN courses c
  ON c.id = f.course_id
WHERE s.username = "john_doe";

-- LEFT JOIN을 사용하여 'jane_smith' 학생이 작성한 코스 피드백과 해당 코스의 제목을 검색하는 SQL 쿼리를 작성하시오.
SELECT s.username, c.title, f.COMMENT
FROM feedback f
LEFT JOIN students s
  ON s.id = f.student_id
LEFT JOIN courses c
  ON c.id = f.course_id
WHERE s.username = "jane_smith";

-- 'mary_jones' 학생이 작성한 가장 최근 피드백의 내용을 검색하는 SQL 쿼리를 작성하시오.
SELECT f.comment
FROM feedback f
INNER JOIN students s
 ON s.id = f.student_id
WHERE s.username = "mary_jones";
