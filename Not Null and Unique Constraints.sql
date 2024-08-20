-- Database Name
USE practicedb;

-- Not Null, Unique Constraints

-- Drop Data
DROP TABLE IF EXISTS student_assistants;
DROP TABLE IF EXISTS students;
DROP TABLE IF EXISTS college_departments;


-- Create Data
CREATE TABLE college_departments(department_id INT PRIMARY KEY,
								department VARCHAR(25) NOT NULL);

CREATE TABLE students(student_id INT PRIMARY KEY,
						department_id INT,
						name TEXT,
                        gwa DECIMAL(4, 2),
                        FOREIGN KEY (department_id) REFERENCES college_departments(department_id));


CREATE TABLE student_assistants(student_id INT PRIMARY KEY,
								name TEXT,
                                registrar_num SMALLINT);
                                
-- Add Unique Constraints
ALTER TABLE college_departments
ADD CONSTRAINT unique_department UNIQUE(department);

-- Add Not Null Constraints
ALTER TABLE students
MODIFY COLUMN name TEXT NOT NULL;

ALTER TABLE student_assistants
MODIFY COLUMN name TEXT NOT NULL;

ALTER TABLE student_assistants
MODIFY COLUMN registrar_num SMALLINT NOT NULL;





                            
                            
 

    
    
    







