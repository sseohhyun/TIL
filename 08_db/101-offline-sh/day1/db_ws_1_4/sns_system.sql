CREATE DATABASE sns_system_db;

USE sns_system_db;

CREATE TABLE users(
  user_id INT PRIMARY KEY AUTO_INCREMENT,
  name VARCHAR(255),
  email VARCHAR(255)
);

CREATE TABLE posts(
  post_id INT PRIMARY KEY,
  user_id INT,
  title VARCHAR(255),
  content TEXT,
  FOREIGN KEY (user_id) REFERENCES users(user_id)
);

CREATE TABLE comment(
  comment_id INT PRIMARY KEY,
  post_id INT,
  content TEXT,
  FOREIGN KEY (post_id) REFERENCES posts(post_id)
);