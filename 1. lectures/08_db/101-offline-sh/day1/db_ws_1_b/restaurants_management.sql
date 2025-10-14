-- Active: 1752638285122@@localhost@3306@restaurant_db
USE restaurant_db;

ALTER TABLE restaurants
ADD COLUMN phone_number VARCHAR(20);

ALTER TABLE menus
ADD COLUMN description TEXT;

ALTER TABLE restaurants
RENAME COLUMN name TO restaurant_name;

ALTER TABLE menus
MODIFY COLUMN price DECIMAL(12, 2) NOT NULL;