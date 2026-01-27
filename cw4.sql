INSERT INTO `books`(`id`, `title`, `author`, `price`, `stock`) VALUES ('1','learn sql','john smith','400','10'),('2','mastering python','jane doe','600','5'),(3, 'HTML & CSS Basics', 'Alan Webb', 300, 8);
UPDATE `books` SET price='50',stock='12'WHERE title=' learn sql';
UPDATE books SET stock='2'WHERE price > 500;
SELECT * FROM `books` WHERE id='3';
