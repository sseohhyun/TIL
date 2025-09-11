CREATE DATABASE restaurant_db;

USE restaurant_db;

CREATE Table restaurants(
  id INT PRIMARY KEY AUTO_INCREMENT,
  name VARCHAR(255),
  location VARCHAR(255),
  cuisine_type VARCHAR(100)
);

CREATE Table menus(
  id INT PRIMARY KEY AUTO_INCREMENT,
  restaurant_id INT,
  item_name VARCHAR(255),
  price DECIMAL(10, 2),
  FOREIGN KEY (restaurant_id) REFERENCES restaurants(id)
);

INSERT INTO restaurants(name, location, cuisine_type)
VALUES
('Sushi Place', 'Tokyo', 'Japanese'),
('Pasta Paradise', 'Rome', 'Italian'),
('Curry Corner', 'Mumbai', 'Indian');

INSERT INTO menus(restaurant_id, item_name, price)
VALUES
(1, 'Salmon Nigiri', 5.50),
(1, 'Tuna Sashimi', 6.00),
(2, 'Spaghetti Carbonara', 7.50),
(2, 'Margherita Pizza', 8.00),
(3, 'Chicken Curry', 6.50),
(3, 'Vegetable Biryani', 5.00);