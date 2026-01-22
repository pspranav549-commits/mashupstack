INSERT INTO `student`(`id`, `name`, `age`, `department`, `grade`) VALUES ('NO 1','PRANAV','22','ELECTRONICS','92')
INSERT INTO `student`(`name`, `age`, `department`, `grade`) VALUES ('PRANAV','22','ELECTRONICS','92'), ('AMAL','22','MECHANICAL','90'),('JEAN','22','COMPUTER SCIENCE','94'),('ANJANA','22','PHYSICS','90')
SELECT * FROM `student` WHERE age>20;
SELECT * FROM `student` WHERE department IN ('COMPUTER SCIENCE' ,'PHYSICS');
SELECT * FROM `student` WHERE grade = 90;
SELECT * FROM `student` WHERE grade BETWEEN 70 AND 90;