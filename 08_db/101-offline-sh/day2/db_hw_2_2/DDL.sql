-- 데이터베이스 생성
CREATE DATABASE libraries;

-- 데이터베이스 사용
USE libraries;

-- books 테이블 생성
CREATE TABLE books (
    id INT AUTO_INCREMENT PRIMARY KEY,
    title VARCHAR(255) NOT NULL,
    publisher VARCHAR(255) NOT NULL,
    author VARCHAR(255) NOT NULL,
    published_date DATE NOT NULL,
    isbn VARCHAR(13) NOT NULL UNIQUE,
    price DECIMAL(5,2) NOT NULL,
    genre VARCHAR(50) NOT NULL
);

INSERT INTO books(title, publisher, author, published_date, isbn, price, genre)
VALUES
('The Great Gatsby', 'Scribner', 'F. Scott Fitzgerald', '1925-04-10', '9780743273565', 10.99, 'Classic'),
('1984', 'Secker & Warburg', 'George Orwell', '1949-06-08', '9780451524935', 8.99, 'Dystopian');

SELECT * FROM books;