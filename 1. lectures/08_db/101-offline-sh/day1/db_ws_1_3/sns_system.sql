CREATE DATABASE sns_system_db;

USE sns_system_db;

CREATE TABLE users(
  user_id INT PRIMARY KEY,
  name VARCHAR(255),
  email VARCHAR(255)
)

CREATE TABLE posts(
  post_id INT PRIMARY KEY,
  title VARCHAR(255),
  content TEXT,
  created_at DATETIME,
  user_id INT,
  FOREIGN KEY (user_id) REFERENCES users(user_id)
)

CREATE TABLE comment(
  comment_id INT PRIMARY KEY,
  content TEXT,
  created_at DATETIME,
  user_id INT,
  post_id INT,
  FOREIGN KEY (user_id) REFERENCES users(user_id),
  FOREIGN KEY (post_id) REFERENCES posts(post_id)
)