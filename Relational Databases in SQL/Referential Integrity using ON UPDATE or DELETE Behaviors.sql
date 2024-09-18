-- Database Name/Any Database
USE practicedb;

-- Hello! My name is Christiane A. Bacani a Data/DevOps Engineer

-- Referential Integrity Constraint with different ON DELETE/UPDATE Behaviors


-- Drop Table
DROP TABLE IF EXISTS orders;
DROP TABLE IF EXISTS products;
DROP TABLE IF EXISTS customers;
DROP TABLE IF EXISTS employees;
DROP TABLE IF EXISTS platforms;
DROP TABLE IF EXISTS companies;
DROP TABLE IF EXISTS business_categories;   

-- Create Table
CREATE TABLE business_categories(category_id INT PRIMARY KEY,
									category TEXT);
-- Insert Data
INSERT INTO business_categories(category_id, category) 
VALUES (1, 'E-Ecommerce');

-- Create Entity with ON DELETE/UPDATE Behavior
CREATE TABLE companies(company_id INT PRIMARY KEY,
						company TEXT,
                        category_id INT,
                        FOREIGN KEY(category_id) REFERENCES business_categories(category_id)
                        ON DELETE SET NULL
                        ON UPDATE SET NULL);
-- Insert Data
INSERT INTO companies(company_id, company, category_id) 
VALUES (1, 'BCX Company', 1),
(2, 'Shop-E Inc.', 1);

-- Create Entity with ON DELETE/UPDATE Behavior
CREATE TABLE platforms(platform_id INT PRIMARY KEY,
						platform_type VARCHAR(25),
                        platform TEXT,
                        company_id INT,
                        FOREIGN KEY(company_id) REFERENCES companies(company_id) 
                        ON UPDATE CASCADE
                        ON DELETE RESTRICT);
-- Insert Data
INSERT INTO platforms(platform_id, platform_type, platform, company_id) 
VALUES (1, 'Website', 'www.bcxcompany.com', 1);
 
 -- Create Entity with ON DELETE/UPDATE Behavior
CREATE TABLE employees(employee_id INT PRIMARY KEY,
						platform_id INT,
                        employee TEXT,
						monthly_salary DECIMAL(11, 2),
                        FOREIGN KEY(platform_id) REFERENCES platforms(platform_id)
                        ON UPDATE CASCADE
                        ON DELETE SET NULL); 
-- Insert Data
INSERT INTO employees(employee_id, platform_id, employee, monthly_salary) 
VALUES (1, 1, 'Doe, John', 80000);

-- Create Data
CREATE TABLE customers(customer_id INT PRIMARY KEY,
						customer TEXT);
-- Insert Data
INSERT INTO customers(customer_id, customer) 
VALUES (1, 'McKinsey Jane');

-- Create Entity with ON DELETE/UPDATE Behavior
CREATE TABLE products(product_id INT PRIMARY KEY,
						platform_id INT,
						product TEXT,
                        amount DECIMAL(11, 2),
                        product_type TEXT, 
                        FOREIGN KEY(platform_id) REFERENCES platforms(platform_id)
                        ON DELETE RESTRICT
                        ON UPDATE CASCADE);
-- Insert Data
INSERT INTO products(product_id, platform_id, product, amount, product_type) 
VALUES (1, 1, 'Nike Shoes', 2500, 'Miscellaneous');

-- Create Entity with ON DELETE/UPDATE Behavior
CREATE TABLE orders(order_id SERIAL PRIMARY KEY,
					order_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                    product_quantity BIGINT,
                    total_amount DECIMAL(11, 2),
                    customer_id INT,
                    FOREIGN KEY(customer_id) REFERENCES customers(customer_id) 
                    ON UPDATE CASCADE
                    ON DELETE CASCADE,
                    product_id INT,
                    FOREIGN KEY(product_id) REFERENCES products(product_id) 
                    ON DELETE SET NULL
                    ON UPDATE CASCADE); 

-- Insert Data
INSERT INTO orders(order_date, product_quantity, total_amount, customer_id, product_id) 
VALUES (CURDATE(), 2, 5000, 1, 1);


-- Query
SELECT *
FROM orders;





















    
    
    

    
    






