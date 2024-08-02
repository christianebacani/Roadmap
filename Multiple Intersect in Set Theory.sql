-- Use any database 
USE countries;
-- Intersect in Set Theory in MySQL 
-- Combines the records from different tables and query the records that have similar records from one table to others

-- Drop unnecessary tables
DROP TABLE IF EXISTS college_students;
DROP TABLE IF EXISTS workers;
DROP TABLE IF EXISTS scholars;

-- Create
CREATE TABLE college_students(student_id INT PRIMARY KEY,
						student_name VARCHAR(50));

CREATE TABLE workers(worker_id INT PRIMARY KEY,
					worker_name VARCHAR(50));

CREATE TABLE scholars(student_id INT PRIMARY KEY,
						student_name VARCHAR(50));

-- Insert
INSERT INTO college_students(student_id, student_name) 
VALUES (1, 'Christiane Bacani'), (2, 'Rica Flores'), (3, 'Nathaniel Flores');

INSERT INTO workers(worker_id, worker_name) 
VALUES (1, 'Christiane Bacani'), (2, 'Rica Flores');

INSERT INTO scholars(student_id, student_name) 
VALUES (1, 'Christiane Bacani'), (2, 'Rica Flores'), (3, 'Nathaniel Flores');

-- Alternative we can used join with AND clause (Depends on the nature of the data, but here I used left join since the number of records is not equal) for further filtering
SELECT
	*
FROM college_students AS c
LEFT JOIN scholars AS s
	ON s.student_id = c.student_id
    AND s.student_name = c.student_name
LEFT JOIN workers AS w
	ON w.worker_id = s.student_id
    AND w.worker_name = s.student_name;


-- Using INTERSECT for better readability
SELECT
	student_name AS student_scholar_worker
FROM college_students
INTERSECT 
SELECT
	student_name
FROM scholars
UNION 
SELECT
	worker_name
FROM workers
ORDER BY student_scholar_worker

    
    
    
    
    
    
    


































    

    

    











    

 








    















