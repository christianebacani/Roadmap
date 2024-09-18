-- Database Name/Any Database
USE practicedb;
-- Publisher : Bacani, Christiane A.


-- Drop Table if necessary
DROP TABLE IF EXISTS enrollments;
DROP TABLE IF EXISTS online_students;
DROP TABLE IF EXISTS online_courses;
DROP TABLE IF EXISTS associations;



-- Create Data
CREATE TABLE associations(association_id INT PRIMARY KEY,
							association TEXT);

CREATE TABLE online_courses(course_id INT PRIMARY KEY,
							association_id INT REFERENCES associations(association_id),
							course TEXT);
 
CREATE TABLE online_students(student_id INT PRIMARY KEY,
								username VARCHAR(100) UNIQUE,
                                gender CHAR(1),
                                user_country TEXT);
                                

-- Create a N:M Relationships between Online Students and Online Courses Entities
CREATE TABLE enrollments(course_id INT REFERENCES online_courses(course_id),
							course TEXT,
							student_id INT REFERENCES online_students(online_students),
                            username VARCHAR(100) UNIQUE);



-- Insert Data
INSERT INTO associations(association_id, association) 
VALUES (1, 'Harvard University'), (2, 'Yale University'), (3, 'DataCamp');



INSERT INTO online_courses(course_id, association_id, course)
VALUES (1, 1, 'CS50X : Introduction to Computer Science'), (2, 3, 'Understanding Data Engineering'); 



INSERT INTO online_students(student_id, username, gender, user_country) 
VALUES (1, 'christianebacani04', 'M', 'Philippines');


INSERT INTO enrollments(course_id, course, student_id, username) 
VALUES (1, 'CS50X : Introduction to Computer Science', 1, 'christianebacani04');




-- Add Surrogate Key
ALTER TABLE enrollments
ADD COLUMN enrollment_code CHAR(7); 

UPDATE enrollments
SET enrollment_code = CONCAT(SUBSTR(course, 1, 3), '_', SUBSTR(username, 1, 3));

ALTER TABLE enrollments
ADD CONSTRAINT enrollment_code_pk
PRIMARY KEY(enrollment_code); 



-- Query Data
SELECT *
FROM enrollments;















    


    











    
    
    
    
    
    
    






