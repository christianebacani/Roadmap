-- Database Name/Any Database
USE practicedb;


-- Hello! My name is Christiane A. Bacani a Data & DevOps Engineer


-- Snowflake Schema (Extension of Star Schema)
-- Warehouse Modeling


-- Drop Table
DROP TABLE IF EXISTS billings;
DROP TABLE IF EXISTS dates;
DROP TABLE IF EXISTS months;
DROP TABLE IF EXISTS quarters;
DROP TABLE IF EXISTS years;
DROP TABLE IF EXISTS patients;
DROP TABLE IF EXISTS diagnosis;
DROP TABLE IF EXISTS patients;
DROP TABLE IF EXISTS occupation_categories;
DROP TABLE IF EXISTS patient_genders;
DROP TABLE IF EXISTS medicines;
DROP TABLE IF EXISTS medicine_categories;
DROP TABLE IF EXISTS employees;
DROP TABLE IF EXISTS contract_categories;
DROP TABLE IF EXISTS departments;
DROP TABLE IF EXISTS employee_genders;
DROP TABLE IF EXISTS hospitals;
DROP TABLE IF EXISTS hospital_categories;


-- Normalize the Dimension table of `hospitals` 
CREATE TABLE hospital_categories(category_id INT PRIMARY KEY);


-- Dimension Table
CREATE TABLE hospitals(hospital_id INT PRIMARY KEY,
						hospital_name TEXT,
                        hospital_type TEXT);
                        

-- Normalize the Dimension table of 'employees'
CREATE TABLE employee_genders(gender_id INT PRIMARY KEY,
							gender CHAR(1));


-- Normalize the Dimension table of `employees`
CREATE TABLE departments(department_id INT PRIMARY KEY,
						department TEXT);

                            
-- Normalize the Dimension table of `employees`
CREATE TABLE contract_categories(contract_category_id INT PRIMARY KEY,
									contract_type TEXT);

				
-- Dimension Table
CREATE TABLE employees(employee_id INT PRIMARY KEY,
						job VARCHAR(50),
                        department TEXT,
                        contract_type VARCHAR(50),
                        employee_name VARCHAR(50),
                        gender CHAR(1) NOT NULL,
                        start_date DATE,
                        end_date DATE); 
				
-- Normlize the Dimension table of `medicines` 
CREATE TABLE medicine_categories(medicine_category_id INT PRIMARY KEY,
								category TEXT);
                                    
-- Dimension Table
 CREATE TABLE medicines(medicine_id INT PRIMARY KEY,
						medicine TEXT);


-- Dimension Table
CREATE TABLE diagnosis(diagnosis_id INT PRIMARY KEY,
						disease TEXT,
                        disease_category TEXT); 
                        
-- Normalize the Dimension Table `patients`
CREATE TABLE patient_genders(gender_id INT PRIMARY KEY,
								gender TEXT);

-- Normalize the Dimension Table `patients`
CREATE TABLE occupation_categories(occupation_id INT PRIMARY KEY,
									category TEXT);
                                            
                                            
-- Dimension Table
CREATE TABLE patients(patient_id INT PRIMARY KEY,
						patient_name TEXT, 
                        patient_gender CHAR(1) NOT NULL,
                        patient_occupation TEXT,
                        patient_address TEXT); 


CREATE TABLE years(year_id INT PRIMARY KEY,
					year BIGINT);

-- Normalize the Dimension Table `dates`
CREATE TABLE quarters(quarter_id INT PRIMARY KEY,
						quarter INT);

-- Normalize the Dimension Table `dates`
 CREATE TABLE months(month_id INT PRIMARY KEY,
					month VARCHAR(40));
 
 
 -- Dimension Table
 CREATE TABLE dates(date_id INT PRIMARY KEY,
					time TIMESTAMP,
                    day INT,
                    month INT,
                    quarter INT, 
                    year BIGINT);

                        
-- Facts Table 
CREATE TABLE billings(record_id SERIAL PRIMARY KEY,
						date_id INT,
                        FOREIGN KEY (date_id) REFERENCES dates (date_id),
						patient_id INT,
						FOREIGN KEY (patient_id) REFERENCES patients(patient_id),
						diagnosis_id INT,
						FOREIGN KEY (diagnosis_id) REFERENCES diagnosis (diagnosis_id),
						medicine_id INT,
						FOREIGN KEY (medicine_id) REFERENCES medicines (medicine_id),
						employee_id INT,
						FOREIGN KEY (employee_id) REFERENCES employees (employee_id),
						hospital_id INT,
						FOREIGN KEY (hospital_id) REFERENCES hospitals (hospital_id),
						initial_bill NUMERIC,
						total_bill NUMERIC,
						total_days_administered BIGINT); 


-- Add a column
ALTER TABLE hospital_categories
ADD COLUMN category TEXT;


-- Add a column 
ALTER TABLE hospitals
ADD COLUMN category_id INT;


-- Create a FK
ALTER TABLE hospitals
ADD CONSTRAINT hospitals_hospital_categories_fk
FOREIGN KEY (category_id) REFERENCES hospital_categories (category_id);

		
-- Migrate the `hospital_type` from hospitals dimension table into `hospital_categories` dimension table
UPDATE hospital_categories
INNER JOIN hospitals
	USING(category_id) 
SET category = hospital_type;


-- Drop the column
ALTER TABLE hospitals
DROP COLUMN hospital_type;


-- Add FK for Dimension Table `departments` 
ALTER TABLE employees
ADD COLUMN department_id INT;


-- Add Constraint for Dimension Table `departments`
ALTER TABLE employees
ADD CONSTRAINT employees_department_id
FOREIGN KEY (department_id) REFERENCES departments (department_id);


-- Migrate `department` column into `departments` dimension table
UPDATE departments
INNER JOIN employees
	USING(department_id) 
SET departments.department = employees.department;


-- Drop table
ALTER TABLE employees
DROP COLUMN department;


-- Add FK for Dimension Table `contract_categories`
ALTER TABLE employees
ADD COLUMN contract_category_id INT;

-- Add Constraint for Dimension Table `contract_categories`
ALTER TABLE employees
ADD CONSTRAINT employees_contract_category_id_fk
FOREIGN KEY (contract_category_id) REFERENCES contract_categories (contract_category_id);


-- Migrate `contract_type` column into `contract_categories` dimension table
UPDATE contract_categories
INNER JOIN employees
	USING(contract_category_id) 
SET contract_categories.contract_type = employees.contract_type; 

-- Drop the column
ALTER TABLE employees
DROP COLUMN contract_type;


-- Add FK for Dimension Table `genders` 
ALTER TABLE employees
ADD COLUMN gender_id INT;


-- Add Constraint for Dimension Table `genders` 
ALTER TABLE employees
ADD CONSTRAINT employees_gender_id_fk
FOREIGN KEY (gender_id) REFERENCES employee_genders (gender_id); 


-- Migrate the `gender` column into `genders` dimension table 
UPDATE employee_genders
INNER JOIN employees
	USING(gender_id) 
SET employee_genders.gender = employees.gender;


-- Drop the column
ALTER TABLE employees
DROP COLUMN gender;


-- Add FK for Dimension Table `medicine_categories`
ALTER TABLE medicines
ADD COLUMN medicine_category_id INT;


-- Add Constraint for dimension table `medicine_categories` 
ALTER TABLE medicines
ADD CONSTRAINT medicine_medicine_category_fk
FOREIGN KEY (medicine_category_id) REFERENCES medicine_categories (medicine_category_id);


-- Rename the PK of the dimension table `occupatin_categories`
ALTER TABLE occupation_categories
RENAME COLUMN occupation_id TO category_id;

-- Add FK for Dimension table `patients`
ALTER TABLE patients
ADD COLUMN occupation_category_id INT;

-- Add Constraint for dimension table `occupation_categories`
ALTER TABLE patients
ADD CONSTRAINT patient_occupation_category_fk
FOREIGN KEY (occupation_category_id) REFERENCES occupation_categories (category_id);

-- Truncate the `gender` column
ALTER TABLE patient_genders
MODIFY COLUMN gender CHAR(1) NOT NULL;



ALTER TABLE patients
DROP COLUMN patient_gender;


-- Drop column
ALTER TABLE patients
DROP COLUMN patient_occupation;


-- Add FK for dimension table `months`
ALTER TABLE dates
ADD COLUMN month_id INT;


-- Add Constraint for dimension table `months`
ALTER TABLE dates
ADD CONSTRAINT date_month_fk
FOREIGN KEY (month_id) REFERENCES months (month_id); 


-- Drop Column
ALTER TABLE dates
DROP COLUMN month;


-- Add FK for the dimension table `quarters`
ALTER TABLE months
ADD COLUMN quarter_id INT;


-- Add Constraint for the dimension table `quarters`
ALTER TABLE months
ADD CONSTRAINT month_quarter_fk
FOREIGN KEY (quarter_id) REFERENCES quarters (quarter_id);


-- Drop Column
ALTER TABLE dates
DROP COLUMN quarter;


-- Add FK for the dimension table `years`
ALTER TABLE quarters
ADD COLUMN year_id INT;


-- Add Constraint for the dimension table `years`
ALTER TABLE quarters
ADD CONSTRAINT quarter_year_fk
FOREIGN KEY (year_id) REFERENCES years (year_id);
 

-- Drop Column
ALTER TABLE dates
DROP COLUMN year;


-- Query the Facts table
SELECT *
FROM billings;










