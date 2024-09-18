-- Database Name
USE practicedb;

-- SuperKey, Candidate Key

-- Drop
DROP TABLE IF EXISTS students_id;
DROP TABLE IF EXISTS genders;
DROP TABLE IF EXISTS departments;

-- Create
CREATE TABLE departments(department_id INT PRIMARY KEY,
							department VARCHAR(30));

CREATE TABLE genders(gender_id INT PRIMARY KEY,
						gender CHAR(1) CHECK(LENGTH(gender) = 1));

CREATE TABLE students_id(id CHAR(8) CHECK (LENGTH(id) = 8),
							department_id INT,
                            gender_id INT,
							student_name VARCHAR(100) NOT NULL,
                            processed_date DATE NOT NULL,
                            FOREIGN KEY(department_id) REFERENCES departments(department_id)
                            ON DELETE CASCADE,
                            FOREIGN KEY(gender_id) REFERENCES genders(gender_id)
                            ON UPDATE CASCADE); 
-- Modify
ALTER TABLE departments
MODIFY COLUMN department VARCHAR(30) NOT NULL;

-- Insert
INSERT INTO departments(department_id, department) 
VALUES (1, 'CCS');

INSERT INTO genders(gender_id, gender) 
VALUES (1, 'M');

INSERT INTO students_id(id, department_id, gender_id, student_name, processed_date) 
VALUES ('22-00981', 1, 1, 'Bacani, Christiane Rhely Joselle A.', CURDATE()),
('22-00982', 1, 1, 'Bacani, CRJ D.', CURDATE());

-- Query the Candidate Key
SELECT
	COUNT(DISTINCT id) AS num_rows
FROM students_id;
