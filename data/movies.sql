CREATE DATABASE movierecommendation;

USE movierecommendation;

CREATE TABLE movies (
    movie_id INT PRIMARY KEY,
    title VARCHAR(255),
    genres VARCHAR(255)
);

CREATE TABLE ratings (
    user_id INT,
    movie_id INT,
    rating FLOAT,
    timestamp BIGINT,
    PRIMARY KEY (user_id, movie_id)
);
SHOW DATABASES;
USE movierecommendation;
SHOW TABLES;

LOAD DATA INFILE 'C:/ProgramData/MySQL/MySQL Server 8.0/Uploads/movies.csv'
INTO TABLE movies
FIELDS TERMINATED BY ',' ENCLOSED BY '"'
LINES TERMINATED BY '\n'
IGNORE 1 ROWS
(movie_id, title, genres);

LOAD DATA INFILE 'C:/ProgramData/MySQL/MySQL Server 8.0/Uploads/ratings.csv'
INTO TABLE ratings
FIELDS TERMINATED BY ',' ENCLOSED BY '"'
LINES TERMINATED BY '\n'
IGNORE 1 ROWS
(user_id, movie_id, rating, timestamp);

SELECT * FROM movies LIMIT 5;
SELECT * FROM ratings LIMIT 5;

SHOW DATABASES;
USE movierecommendation;
SHOW TABLES;