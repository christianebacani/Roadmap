-- Database Name
USE practicedb;
-- I am a Data Engineer!

-- Referential Integriy/Foreign Key Constraint

-- Drop Table
DROP TABLE IF EXISTS cloud_services;
DROP TABLE IF EXISTS companies;
DROP TABLE IF EXISTS categories;

-- Create Table
CREATE TABLE categories(category TEXT);


CREATE TABLE companies(company_id INT PRIMARY KEY,
						category_code CHAR(7),
                        name TEXT);

CREATE TABLE cloud_services(cloud_id INT PRIMARY KEY,
							company_id INT REFERENCES companies(company_id), -- Create FK Constraint
                            name TEXT,
                            year_founded YEAR);  
    
-- Insert Data
INSERT INTO categories(category) 
VALUES ('Multinational Technological Company');

-- Alter
ALTER TABLE categories
ADD COLUMN category_code CHAR(7);

UPDATE categories
SET category_code = CONCAT(SUBSTR(category, 1, 3), ' - C');

ALTER TABLE categories
ADD CONSTRAINT cat_code_pk
PRIMARY KEY(category_code); 


-- Add FK Constraint
ALTER TABLE companies
ADD CONSTRAINT cat_code_fk
FOREIGN KEY(category_code) REFERENCES categories(category_code);

-- Insert Data
INSERT INTO companies(company_id, category_code, name) 
VALUES (1, 'Mul - C', 'Amazon Web Services'),
(2, 'Mul - C', 'Microsoft'),
(3, 'Mul - C', 'Google');

INSERT INTO cloud_services(cloud_id, company_id, name, year_founded) 
VALUES (1, 1, 'Amazon Web Services', '2006'), 
(2, 2, 'Microsoft Azure', '2010'), 
(3, 3, 'Google Cloud Platform', '2008'); 

-- Query Data
SELECT *
FROM cloud_services;

















    


    











    
    
    
    
    
    
    






