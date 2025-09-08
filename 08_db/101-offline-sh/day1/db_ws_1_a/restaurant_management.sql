CREATE DATABASE restaurant_db
  DEFAULT CHARACTER SET = 'utf8mb4';

USE restaurant_db;

CREATE TABLE restaurants(
  id INT PRIMARY KEY AUTO_INCREMENT,
  name VARCHAR(255),
  location VARCHAR(255),
  cuisine_type VARCHAR(100)
);

CREATE TABLE menus(
  id INT PRIMARY KEY AUTO_INCREMENT,
  restaurant_id INT,
  item_name VARCHAR(255),
  price DECIMAL(10, 2),
  FOREIGN KEY (restaurant_id) REFERENCES restaurants(id)
);