CREATE DATABASE onlinebkstore_db;
USE onlinebkstore_db;
CREATE TABLE authors (
    author_id INT PRIMARY KEY,
    author_name VARCHAR(100),
    email VARCHAR(100) UNIQUE
);
CREATE TABLE books (
    book_id INT PRIMARY KEY,
    book_title VARCHAR(150),
    author_id INT,

    FOREIGN KEY (author_id) REFERENCES authors(author_id)
);
INSERT INTO authors VALUES (1, 'Chetan Bhagat', 'chetan@gmail.com'),(2, 'Arundhati Roy', 'arundhati@gmail.com');
INSERT INTO books VALUES (101, 'Five Point Someone', 1),(102, 'The God of Small Things', 2);
