USE sns_system_db

INSERT INTO users (name, email) VALUES
('홍길동', 'hong@example.com'),
('이순신', 'lee@example.com');

INSERT INTO posts (post_id, user_id, title, content) VALUES
('101', '1', '첫 번째 게시글', '안녕하세요'),
('102', '1', '두 번째 게시글', '반갑습니다'),
('103', '2', '세 번째 게시글', '좋은 하루');

INSERT INTO comment (comment_id, post_id, content) VALUES
('1001', '101', '첫 댓글'),
('1002', '102', '두 번째 댓글'),
('1003', '103', '세 번째 댓글');