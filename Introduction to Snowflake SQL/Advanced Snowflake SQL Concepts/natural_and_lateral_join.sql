/*
    Lesson: Joining in Snowflake
*/


// Create School Classes Database
CREATE DATABASE IF NOT EXISTS
    school_classes_db;

// Use School Classes Database
USE DATABASE
    school_classes_db;

------------------------------------------------------- Table Creation -----------------------------------------------------

// Universities Table
CREATE OR REPLACE TABLE
    universities (
    university_id NUMBER(38, 0) PRIMARY KEY,
    university VARCHAR(255)
    );

// Campuses Table
CREATE OR REPLACE TABLE
    campuses (
    campus_id NUMBER(38, 0) PRIMARY KEY,
    university_id NUMBER(38, 0),
    campus VARCHAR(255),
    FOREIGN KEY(university_id) REFERENCES universities(university_id)
    );

// College Departments Table
CREATE OR REPLACE TABLE
    college_departments (
    college_department_id NUMBER(38, 0) PRIMARY KEY,
    campus_id NUMBER(38, 0),
    college_department VARCHAR(255)
    );

// Degrees Table
CREATE OR REPLACE TABLE
    degrees (
    degree_id NUMBER(38, 0) PRIMARY KEY,
    degree VARCHAR(255)
    );

// Programs Table
CREATE OR REPLACE TABLE
    programs (
    program_id NUMBER(38, 0) PRIMARY KEY,
    college_department_id NUMBER(38, 0),
    degree_id NUMBER(38, 0),
    program VARCHAR(255),
    FOREIGN KEY(college_department_id) REFERENCES college_departments(college_department_id),
    FOREIGN KEY(degree_id) REFERENCES degrees(degree_id)
    );

// Majors Table
CREATE OR REPLACE TABLE
    majors (
    major_id NUMBER(38, 0) PRIMARY KEY,
    program_id NUMBER(38, 0),
    major VARCHAR(255),
    FOREIGN KEY(program_id) REFERENCES programs(program_id)
    );

// College Years Table
CREATE OR REPLACE TABLE
    college_years (
    college_year_id NUMBER(38, 0) PRIMARY KEY,
    college_year NUMBER(38, 0)
    );

// Sections Table
CREATE OR REPLACE TABLE
    sections (
    section_id NUMBER(38, 0) PRIMARY KEY,
    section CHAR(1)
    );

// Genders Table
CREATE OR REPLACE TABLE
    genders (
    gender_id CHAR(1) PRIMARY KEY,
    gender VARCHAR(20)
    );

// College Deans Table
CREATE OR REPLACE TABLE
    college_deans (
    college_dean_id NUMBER(38, 0) PRIMARY KEY,
    college_department_id NUMBER(38, 0),
    gender_id CHAR(1),
    college_dean VARCHAR(255),
    FOREIGN KEY(college_department_id) REFERENCES college_departments(college_department_id),
    FOREIGN KEY(gender_id) REFERENCES genders(gender_id)
    );

// Courses Table
CREATE OR REPLACE TABLE
    courses (
    course_id NUMBER(38, 0) PRIMARY KEY,
    course VARCHAR(255),
    total_units FLOAT
    );

// Instructors Table
CREATE OR REPLACE TABLE
    instructors (
    instructor_id NUMBER(38, 0),
    course_id NUMBER(38, 0),
    gender_id CHAR(1),
    instructor VARCHAR(255),
    PRIMARY KEY(instructor_id, course_id),
    FOREIGN KEY(gender_id) REFERENCES genders(gender_id)
    );

// Students Table
CREATE OR REPLACE TABLE
    students (
    student_id CHAR(8) PRIMARY KEY,
    major_id NUMBER(38, 0),
    college_year_id NUMBER(38, 0),
    section_id NUMBER(38, 0),
    gender_id CHAR(1),
    first_name VARCHAR(255),
    middle_name VARCHAR(255),
    last_name VARCHAR(255),
    FOREIGN KEY(major_id) REFERENCES majors(major_id),
    FOREIGN KEY(college_year_id) REFERENCES college_years(college_year_id),
    FOREIGN KEY(section_id) REFERENCES sections(section_id),
    FOREIGN KEY(gender_id) REFERENCES genders(gender_id)
    );

------------------------------------------------------- Data Insertion -----------------------------------------------------

INSERT INTO
    universities (
    university_id,
    university
    )
    VALUES
    (1, 'Bataan Peninsula State University'),
    (2, 'Tarlac State University');

INSERT INTO
    campuses (
    campus_id,
    university_id,
    campus
    )
    VALUES
    (1, 1, 'Main Campus'),
    (2, 2, 'San Isidro');
    
INSERT INTO
    college_departments (
    college_department_id,
    campus_id,
    college_department
    )
    VALUES 
    (1, 1, 'College of Computer Studies'),
    (2, 2, 'College of Computer Studies');

INSERT INTO
    degrees (
    degree_id,
    degree
    )
    VALUES 
    (1, 'Bachelor of Science');

INSERT INTO
    programs (
    program_id,
    college_department_id,
    degree_id,
    program
    )
    VALUES
    (1, 1, 1, 'Computer Science'),
    (2, 1, 1, 'Information Technology');

INSERT INTO
    majors (
    major_id,
    program_id,
    major
    )
    VALUES
    (1, 1, 'Software Development'),
    (2, 2, 'Network Administration');

INSERT INTO
    college_years (
    college_year_id,
    college_year
    )
    VALUES
    (1, 1),
    (2, 2),
    (3, 3),
    (4, 4),
    (5, 5);

INSERT INTO
    sections (
    section_id,
    section
    )
    VALUES
    (1, 'A');

INSERT INTO
    genders (
    gender_id,
    gender
    )
    VALUES 
    ('M', 'Male'),
    ('F', 'Female');

INSERT INTO
    college_deans (
    college_dean_id,
    college_department_id,
    gender_id,
    college_dean
    )
    VALUES 
    (1, 1, 'F', 'Maria Lolita Masangcap'),
    (2, 2, 'M', 'Alvincent Danganan');

INSERT INTO
    courses (
    course_id,
    course,
    total_units
    )
    VALUES
    (1, 'Modeling & Simulations', 3.0),
    (2, 'System Integration & Architecture', 1.3);

INSERT INTO
    instructors (
    instructor_id,
    course_id,
    gender_id,
    instructor
    )
    VALUES
    (1, 1, 'F', 'Consuelo Cruz'),
    (2, 2, 'M', 'Dennis Padilla');

INSERT INTO
    students (
    student_id,
    major_id,
    college_year_id,
    section_id,
    gender_id,
    first_name,
    middle_name,
    last_name
    )
    VALUES
    ('22-00981', 1, 4, 1, 'M', 'Christiane Rhely Joselle', 'Aguibitin', 'Bacani'),
    ('22-00982', 2, 3, 1, 'F', 'Rica Mae', 'Gueco', 'Flores');

------------------------------------------------------- Data Selection -----------------------------------------------------

// Using 'NATURAL JOIN' to join two tables using the columns with the same name without specifying it using 'ON' clause
SELECT *
FROM
    campuses
NATURAL JOIN
    universities;


// Using 'LATERAL' for subqueries. It is similar to joins with subquery, the only difference is that it can access the left tables column and also the execution order
SELECT
    p.program,
    lat_male.number_of_male_students,
    lat_female.number_of_female_students
FROM
    programs AS p,
LATERAL (
SELECT
    COUNT(s.gender_id) AS number_of_male_students
FROM
    majors AS m
INNER JOIN
    students AS s
ON
    m.major_id = s.major_id
WHERE
    p.program_id = m.program_id AND
    s.gender_id = 'M'
) AS lat_male,
LATERAL (
SELECT
    COUNT(s.gender_id) AS number_of_female_students
FROM
    majors AS m
INNER JOIN
    students AS s
ON
    m.major_id = s.major_id
WHERE
    p.program_id = m.program_id AND
    s.gender_id = 'F'
) AS lat_female;