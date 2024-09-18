-- Use any database 
USE countries;

-- Self Join in MySQL
-- Comparing the student from other departments
DROP TABLE IF EXISTS students;
-- Creating table
CREATE TABLE students(student_id INT PRIMARY KEY,
						student_name VARCHAR(50),
                        department VARCHAR(50),
                        grade INT);
-- Inserting table
INSERT INTO students(student_id, student_name, department, grade) 
VALUES (1, 'Christiane Bacani', 'CCS',  89), (2, 'Rica Flores', 'CCS', 95), (3, 'Crj Bacani', 'CEA', 85), (4, 'Rhely Mendoza', 'BSN', 90);

-- Querying
SELECT
	s1.student_name,
    s1.department,
    s1.grade,
    s2.student_name,
    s2.department,
    s2.grade
FROM students AS s1
INNER JOIN students AS s2
	ON s1.department <> s2.department
    AND s1.grade > 85 OR s2.grade > 85
ORDER BY s1.student_name, s2.grade DESC;

-- Using ON clause per pairing the students with not equal department and AND clause for better query of grade greater than 85




















    

    

    











    

 








    















