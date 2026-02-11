CREATE DATABASE companydata_db;
USE companydata_db;

CREATE TABLE Employee (
    id INT PRIMARY KEY,
    name VARCHAR(50),
    department VARCHAR(50),
    `leave` INT);

INSERT INTO Employee VALUES
(1,'Raju','Sales',1),
(2,'Sangeetha','Sales',3),
(3,'Vinay','Operations',8),
(4,'Abey','Packing',2),
(5,'Thomas','Packing',1),
(6,'Muneer','Operations',7),
(7,'Aparna','Sales',3),
(8,'Abid','Operations',9),
(9,'Fathima','Sales',11),
(10,'Varghese','Operations',14);

CREATE TABLE Exam (
    id INT PRIMARY KEY,
    employee_id INT,
    exam_status VARCHAR(10) );

INSERT INTO Exam VALUES
(1,2,'Pass'),
(2,5,'Fail'),
(3,1,'Fail'),
(4,8,'Pass'),
(5,3,'Pass'),
(6,1,'Pass'),
(7,6,'Fail'),
(8,9,'Pass'),
(9,10,'Pass');
SELECT *FROM Employee WHERE department = 'Sales' AND `leave` > 5;


SELECT COUNT(*) AS total_employees FROM Employee WHERE department = 'Operations';

SELECT department, COUNT(*) AS employee_count  FROM Employee GROUP BY department;


SELECT department,SUM(`leave`)AS leaves FROM Employee GROUP BY department HAVING SUM(`leave`) > 10;


SELECT employee.name FROM Employee JOIN Exam ON employee.id = exam.employee_id WHERE exam.exam_status = 'Pass';
 
SELECT e.name
FROM Employee e
LEFT JOIN Exam ex
ON e.id = ex.employee_id
WHERE ex.employee_id IS NULL;