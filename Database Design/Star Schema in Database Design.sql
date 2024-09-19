-- Database Name/Any Database
USE practicedb;


-- Hello! My name is Christiane A. Bacani a Data/DevOps Engineer


-- Star Schema
-- Warehouse Modeling

-- Drop Table
DROP TABLE IF EXISTS billings;
DROP TABLE IF EXISTS dates;
DROP TABLE IF EXISTS patients;
DROP TABLE IF EXISTS diagnosis;
DROP TABLE IF EXISTS patients;
DROP TABLE IF EXISTS medicines;
DROP TABLE IF EXISTS employees;
DROP TABLE IF EXISTS hospitals;

-- Dimension Table
CREATE TABLE hospitals(hospital_id INT PRIMARY KEY,
			hospital_name TEXT,
                        hospital_type TEXT);
                        
                        
-- Dimension Table
CREATE TABLE employees(employee_id INT PRIMARY KEY,
			job_type VARCHAR(50),
                        contract_type TEXT,
                        employee_name VARCHAR(50),
                        gender CHAR(1) NOT NULL,
                        start_date DATE,
                        end_date DATE); 
                        
                        
-- Dimension Table
 CREATE TABLE medicines(medicine_id INT PRIMARY KEY,
			medicine TEXT);

-- Dimension Table
CREATE TABLE diagnosis(diagnosis_id INT PRIMARY KEY,
			disease TEXT,
                        disease_category TEXT); 
                        

-- Dimension Table
CREATE TABLE patients(patient_id INT PRIMARY KEY,
			patient_name TEXT, 
                        patient_gender CHAR(1) NOT NULL,
                        patient_occupation TEXT,
                        patient_address TEXT); 
 
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
                        



                            
                        
                        


