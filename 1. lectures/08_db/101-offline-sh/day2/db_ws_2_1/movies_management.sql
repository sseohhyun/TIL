-- Active: 1752638285122@@localhost@3306@movies
CREATE DATABASE movies;

USE movies;

CREATE TABLE movie_list(
  id INT PRIMARY KEY AUTO_INCREMENT,
  title VARCHAR(255),
  genre VARCHAR(100),
  release_year YEAR
);

INSERT INTO movie_list(title, genre, release_year)
VALUES
('Inception', 'Sci-Fi', 2010),
('The Dark Knight', 'Action', 2008),
('Interstellar', 'Sci-Fi', 2014),
('Unknown', 'Drama', Null),
('The Shawshank Redemption', 'Drama', 1994),
('Fight Club', 'Drama', 1999),
('Mad Max: Fury Road', 'Action', 2015),
('Star Wars: The Force Awakens', 'Sci-Fi', 2015);
