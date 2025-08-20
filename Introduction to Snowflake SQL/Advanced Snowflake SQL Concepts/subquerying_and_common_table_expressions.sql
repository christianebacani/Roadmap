/*
    Lesson: Subquerying and Common Table Expressions
*/


// Use database
USE DATABASE
    hospital_db;

------------------------------------------------------------------------ Data Creation ---------------------------------------------------------------------

// Hospitals table
CREATE OR REPLACE TABLE
    hospitals (
    hospital_id NUMBER(38, 0) PRIMARY KEY,
    hospital VARCHAR(255),
    address VARCHAR(255)
    );

// Departments table
CREATE OR REPLACE TABLE
    departments (
    department_id NUMBER(38, 0) PRIMARY KEY,
    department VARCHAR(255)
    );

// Genders table
CREATE OR REPLACE TABLE
    genders (
    gender_id CHAR(1) PRIMARY KEY,
    gender VARCHAR(255)
    );

// Doctors table
CREATE OR REPLACE TABLE
    doctors (
    doctor_id NUMBER(38, 0) PRIMARY KEY,
    hospital_id NUMBER(38, 0),
    department_id NUMBER(38, 0),
    gender_id CHAR(1),
    doctor VARCHAR(255),
    FOREIGN KEY(hospital_id) REFERENCES hospitals(hospital_id),
    FOREIGN KEY(department_id) REFERENCES departments(department_id),
    FOREIGN KEY(gender_id) REFERENCES genders(gender_id)
    );

// Nurses table
CREATE OR REPLACE TABLE
    nurses (
    nurse_id NUMBER(38, 0) PRIMARY KEY,
    hospital_id NUMBER(38, 0),
    department_id NUMBER(38, 0),
    gender_id CHAR(1),
    nurse VARCHAR(255),
    FOREIGN KEY(hospital_id) REFERENCES hospitals(hospital_id),
    FOREIGN KEY(department_id) REFERENCES departments(department_id),
    FOREIGN KEY(gender_id) REFERENCES genders(gender_id)
    );

// Patients table
CREATE OR REPLACE TABLE
    patients (
    patient_id NUMBER(38, 0) PRIMARY KEY,
    gender_id CHAR(1),
    patient VARCHAR(255),
    FOREIGN KEY(gender_id) REFERENCES genders(gender_id)
    );

// Patient Checkups Table
CREATE OR REPLACE TABLE
    patient_checkups (
    patient_id NUMBER(38, 0) PRIMARY KEY,
    patient VARCHAR(255),
    doctor_in_charge VARCHAR(255),
    reason_for_checkup TEXT,
    doctors_prescription TEXT
    );

// Patient Admissions Table
CREATE OR REPLACE TABLE
    patient_admissions (
    patient_id NUMBER(38, 0) PRIMARY KEY,
    patient VARCHAR(255),
    doctor_in_charge VARCHAR(255),
    reason_for_admission TEXT,
    admission_date_start DATE,
    admission_date_end DATE
    );

------------------------------------------------------------------------ Data Insertion ---------------------------------------------------------------------

INSERT INTO
    hospitals (
    hospital_id,
    hospital,
    address
    )
    VALUES
    (1, 'Bataan General Hospital', 'Brgy. Tenejero Balanga City, Bataan Philippines'),
    (2, 'Tarlac Provincial Hospital', 'Hospital Drive, Brgy. San Vicente, Tarlac City, 2300 Tarlac, Philippines');
    
INSERT INTO
    departments (
    department_id,
    department
    )
    VALUES
    (1, 'Emergency Department (Casualty)'),
    (2, 'Intensive Care Unit (ICU)'),
    (3, 'Surgery Department'),
    (4, 'Cardiology'),
    (5, 'Neurology'),
    (6, 'Pediatrics'),
    (7, 'Gynecology'),
    (8, 'Oncology'),
    (9, 'Psychiatry'),
    (10, 'Radiology'),
    (11, 'Anesthesiology'),
    (12, 'Gastroenterology'),
    (13, 'Ophthalmology'),
    (14, 'Urology');

INSERT INTO
    genders (
    gender_id,
    gender
    )
    VALUES
    ('M', 'Male'),
    ('F', 'Female');

INSERT INTO
    doctors (
    doctor_id,
    hospital_id,
    department_id,
    gender_id,
    doctor
    )
    VALUES
    (1, 1, 10, 'M', 'Christiane Rhely Joselle A. Bacani'),
    (2, 2, 9, 'F', 'Rica Mae G. Flores'),
    (3, 2, 1, 'F', 'Chrae Flores-Bacani');

INSERT INTO
    nurses (
    nurse_id,
    hospital_id,
    department_id,
    gender_id,
    nurse
    )
    VALUES
    (1, 2, 6, 'M', 'Gavjvorzki Flores-Bacani');

INSERT INTO
    patients (
    patient_id,
    gender_id,
    patient
    )
    VALUES
    (1, 'M', 'Nathnath Maslam'),
    (2, 'F', 'Rica Maeeee');

INSERT INTO
    patient_checkups (
    patient_id,
    patient,
    doctor_in_charge,
    reason_for_checkup,
    doctors_prescription
    )
    VALUES
    (1, 'Nathnath Maslam', 'Christiane Rhely Joselle A. Bacani', 'Masakit ang puwet', 'Inom biogesic');

INSERT INTO
    patient_admissions (
    patient_id,
    patient,
    doctor_in_charge,
    reason_for_admission,
    admission_date_start,
    admission_date_end
    )
    VALUES
    (1, 'Nathnath Maslam', 'Christiane Rhely Joselle A. Bacani', 'Sobrang sakit ng puwet', '2025-08-05', NULL);

// Uncorrelated subquery in Snowflake
SELECT
    hospital,
    (SELECT COUNT(*) FROM doctors WHERE hospital_id = 2 AND gender_id = 'M') AS total_male_doctor,
    (SELECT COUNT(*) FROM doctors WHERE hospital_id = 2 AND gender_id = 'F') AS total_female_doctor
FROM
    hospitals
WHERE
    hospital_id = 2;

// Correlated subqueries in Snowflake
SELECT
    hospital,
    (SELECT COUNT(doctors.*) FROM doctors WHERE doctors.hospital_id = hospitals.hospital_id AND doctors.gender_id = 'M') AS number_of_male_doctors,
    (SELECT COUNT(doctors.*) FROM doctors WHERE doctors.hospital_id = hospitals.hospital_id AND doctors.gender_id = 'F') AS number_of_female_doctors,
    (SELECT COUNT(nurses.*) FROM nurses WHERE nurses.hospital_id = hospitals.hospital_id AND nurses.gender_id = 'M') AS number_of_male_nurses,
    (SELECT COUNT(nurses.*) FROM nurses WHERE nurses.hospital_id = hospitals.hospital_id AND nurses.gender_id = 'F') AS number_of_female_nurses
FROM
    hospitals;

// Common Table Expressions in Snowflake
WITH
    cte1 AS (
        SELECT
            gender,
            (SELECT COUNT(*) FROM doctors WHERE doctors.gender_id = genders.gender_id) AS number_of_doctors,
            (SELECT COUNT(*) FROM nurses WHERE nurses.gender_id = genders.gender_id) AS number_of_nurses
        FROM
            genders
    ),
    cte2 AS (
        SELECT
            doctor
        FROM
            doctors
    ),
    cte3 AS (
        SELECT
            nurse
        FROM
            nurses
    ),
    cte4 AS (
        SELECT
            gender,
            (SELECT COUNT(*) FROM patients WHERE patients.gender_id = genders.gender_id) AS total_number_of_patients
        FROM
            genders
    )

SELECT *
FROM
    cte4;