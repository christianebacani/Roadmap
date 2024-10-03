-- Database Name/Any Database
USE practicedb;


-- A simple schema to write some SQL Scripts to enfore 1NF, 2NF, and 3NF


-- Drop tables
DROP TABLE IF EXISTS storage_users; -- Added a table for 1NF
DROP TABLE IF EXISTS user_types; -- Added a new table user_types for 2NF and 3NF
DROP TABLE IF EXISTS user_jobs; -- Added a new table user_jobs for 2NF and 3NF
DROP TABLE IF EXISTS user_departments; -- Added a new table user_departments for 2NF and 3NFa
DROP TABLE IF EXISTS user_companies; -- Added a new table user_companies for 2NF and 3NF
DROP TABLE IF EXISTS storages; -- Added a new table storages for 2NF and 3NF
DROP TABLE IF EXISTS storage_types; -- Added a new table storage_types for 2NF and 3NF


-- Enforcing 1NF
-- Create table storage_users
CREATE TABLE storage_users (user_id INT PRIMARY KEY,
							username TEXT,
                            user_type VARCHAR(30),
                            job VARCHAR(30),
                            department VARCHAR(30),
                            company VARCHAR(50),
                            storage TEXT,
                            storage_type TEXT);

-- Insert records from storage_users table
INSERT INTO storage_users (user_id, username, user_type, job, department, company, storage, storage_type)
VALUES (1, 'Jerry Toms', 'Internal User', 'Data Analyst', 'Data Department', 'XYZ Corporation', 'Data Warehouse', 'Cloud Server'),
		(2, 'Richard Feyn', 'Internal User', 'Data Scientist', 'Data Department', 'XYZ Corporation', 'Data Lakes', 'Cloud Server'),
        (3, 'Alex Gutierrez', 'External User', NULL, NULL, NULL, 'Databases', 'Cloud Server'),
        (4, 'Carl Miller', 'Internal User', 'Machine Learning Engineer', 'IT Department', 'XYZ Corporation', 'Data Lakehouses', 'Cloud Server'); 


-- Enforce 2NF


-- Create user_types table
CREATE TABLE user_types (user_type_id INT PRIMARY KEY,
						user_type TEXT); 

-- Insert records from storage_users
INSERT INTO user_types (user_type_id, user_type)
VALUES (1, 'Internal Users'), (2, 'External Users');


-- Remove column that violates the standard for 2NF
ALTER TABLE storage_users 
DROP COLUMN user_type,
ADD COLUMN user_type_id INT; -- Add column to enforce relationship with the user_types table 


-- Update records from storage_users for referential integrity
UPDATE storage_users
SET user_type_id = 1
WHERE job IS NOT NULL;


UPDATE storage_users
SET user_type_id = 2
WHERE job IS NULL;


-- Add constraint for the storage_users table
ALTER TABLE storage_users
ADD CONSTRAINT user_type_fk
FOREIGN KEY (user_type_id) REFERENCES user_types (user_type_id); 


-- Create user_jobs table
CREATE TABLE user_jobs (job_id INT PRIMARY KEY,
						job TEXT); 

-- Insert records from storage_users table
INSERT INTO user_jobs (job_id, job)
VALUES (1, 'Data Analyst'), (2, 'Data Scientist'), (3, 'Machine Learning Engineer'); 


-- Remove column that violates the standard for 2NF and 3NF
ALTER TABLE storage_users
DROP COLUMN job,
ADD COLUMN job_id INT; -- Add column to enforce relationship with the user_jobs table 


-- Update records from storage_users for referential integrity
UPDATE storage_users
SET job_id = 1
WHERE user_id = 1;

UPDATE storage_users
SET job_id = 2
WHERE user_id = 2;


UPDATE storage_users
SET job_id = 3
WHERE user_id = 4;


-- Add constraint for the storage_users table
ALTER TABLE storage_users
ADD CONSTRAINT job_fk
FOREIGN KEY (job_id) REFERENCES user_jobs (job_id);


-- Querying the data
SELECT *
FROM storage_users;


-- Create user_departments table
CREATE TABLE user_departments (department_id INT PRIMARY KEY,
								department TEXT);

-- Insert records for user_departments table
INSERT INTO user_departments (department_id, department)
VALUES (1, 'Data Department'), (2, 'IT Department');


-- Remove column that violates the standards for 2NF
ALTER TABLE storage_users
DROP COLUMN department;

-- Add column to enforce referential integrity with user_departments table
ALTER TABLE user_jobs
ADD COLUMN department_id INT;

-- Update records from user_jobs to enforce referential integrity with user_departments table
UPDATE user_jobs
SET department_id = 1
WHERE job_id <= 2;

UPDATE user_jobs
SET department_id = 2
WHERE job_id = 3;


-- Add constraint for the user_departments table
ALTER TABLE user_jobs
ADD CONSTRAINT department_fk
FOREIGN KEY (department_id) REFERENCES user_departments (department_id);


-- Create user_companies table
CREATE TABLE user_companies (company_id INT PRIMARY KEY,
							company TEXT);
                            
-- Insert records for user_companies table
INSERT INTO user_companies (company_id, company) 
VALUES (1, 'XYZ Corporation'); 


-- Alter table storage_users that violates the standard for 2NF and 3NF
ALTER TABLE storage_users
DROP COLUMN company;


-- Alter table user_jobs to enforce referential integrity with user_companies
ALTER TABLE user_jobs
ADD COLUMN company_id INT;

-- Update records to enforce referential integrity with user_companies
UPDATE user_jobs
SET company_id = 1; 

-- Add constraint to enforce referential integrity with user_companies
ALTER TABLE user_jobs
ADD CONSTRAINT company_fK
FOREIGN KEY (company_id) REFERENCES user_companies (company_id);


-- Create storages table
CREATE TABLE storages (storage_id INT PRIMARY KEY,
						storage TEXT);

-- Insert records for storages table
INSERT INTO storages (storage_id, storage)
VALUES (1, 'Data Warehouse'), (2, 'Data Lakes'), (3, 'Databases'), (4, 'Data Lakehouses');


-- Alter storage_users table that violates the standard for 2NF and 3NF
ALTER TABLE storage_users
DROP COLUMN storage,
ADD COLUMN storage_id INT;


-- Update records for storage_users table to enforce referential integrity to storages table
UPDATE storage_users
INNER JOIN storages
	ON storages.storage_id = storage_users.user_id
SET storage_users.storage_id = storages.storage_id;


-- Add constraint to enforce referential integrity for storages table
ALTER TABLE storage_users
ADD CONSTRAINT storage_id
FOREIGN KEY (storage_id) REFERENCES storages (storage_id);


-- Create storage_types table
CREATE TABLE storage_types (storage_type_id INT PRIMARY KEY,
							storage_type TEXT);

-- Insert records for storage_types table
INSERT INTO storage_types (storage_type_id, storage_type) 
VALUES (1, 'Cloud Server');


-- Alter table that violates the standard for 2NF and 3NF
ALTER TABLE storage_users
DROP COLUMN storage_type;


-- Alter storages table to enforce referential integrity with storage_types table
ALTER TABLE storages
ADD COLUMN storage_type_id INT;


-- Update storages table to enforce referential integrity with storage_types table
UPDATE storages
SET storage_type_id = 1;


-- Add constraint to enforce referential integrity with storage_types table
ALTER TABLE storages
ADD CONSTRAINT storage_fk
FOREIGN KEY (storage_type_id) REFERENCES storage_types (storage_type_id); 


-- Querying Data
SELECT *
FROM user_companies;

















































































































































