-- Database Name/Any Database
USE metadata;
-- I will become a Data/DevOps Engineer

-- Drop Table
DROP TABLE IF EXISTS constraints_metadata;
DROP TABLE IF EXISTS columns_metadata;
DROP TABLE IF EXISTS tables_metadata;

-- Create
CREATE TABLE tables_metadata(table_name VARCHAR(50) PRIMARY KEY,
							description TEXT);

-- Insert
INSERT INTO tables_metadata(table_name, description) 
VALUES ('business_categories', 'Business Category of a business'), 
('companies', 'Company name and it`s business categories'),
('platforms', 'List of company`s platform'),
('employees', 'Employee`s data, monthly salary, and the platform they worked with'), 
('customers', 'Customers name'),
('products', 'The company`s product they sell to the specific platforms and the data about that product'),
('orders', 'Customer`s order data about it`s corresponding products/s');

-- Create
CREATE TABLE columns_metadata(column_name VARCHAR(50),
								data_type VARCHAR(50),
								description TEXT,
								table_name VARCHAR(50),
                                PRIMARY KEY(column_name, table_name),
                                FOREIGN KEY(table_name) REFERENCES tables_metadata(table_name)); 
-- Insert
INSERT INTO columns_metadata(column_name, data_type , description , table_name) 
VALUES ('category_id', 'INT', 'Primary key of business categories table', 'business_categories'), 
('category', 'TEXT', 'Category name of a business', 'business_categories'), 
('company_id', 'INT', 'Primary key of company / Unique Identification of companies in `companies` table', 'companies'), 
('company', 'TEXT', 'Name of the company', 'companies'), 
('category_id', 'INT', 'Foreign key linking to the business category into the business_categories table', 'companies'),
('platform_id', 'INT', 'Primary key of company platform`s table / Unique Identification of companies `platform` table', 'platforms'),
('platform_type', 'TEXT', 'Platform type of company, they used this platform to sell products', 'platforms'),
('platform', 'TEXT', 'Specific name of the platform', 'platforms'),
('company_id', 'INT', 'Foreign key linking to the company name into the companies table', 'platforms'),
('employee_id', 'INT', 'Primary key of employee`sd table / Unique Identification of employees', 'employees'), 
('platform_id', 'INT', 'Foreign key linking to the platform name into the platforms table', 'employees'),
('employee', 'TEXT', 'Employee name of the specific platform they worked at', 'employees'),
('monthly_salary', 'DECIMAL(11,2)', 'Monthly salary of the employees', 'employees'),
('customer_id', 'INT', 'Primary key of the customers table / Unique Identification of customers', 'customers'),
('customer', 'TEXT', 'Customer name', 'customers'),
('product_id', 'INT', 'Primary key of products table / Unique Identification of platform`s product', 'products'),
('platform_id', 'INT', 'Foreign key linking to the product name into the products table', 'products'),
('product', 'TEXT', 'Product name', 'products'), 
('amount', 'DECIMAL(11, 2)', 'Amount of product', 'products'), 
('product_type', 'TEXT', 'Types of product', 'products'),
('order_id', 'SERIAL', 'Artificial key of the order`s table / Unique Identification of the order`s table', 'orders'),
('order_date', 'TIMESTAMP', 'Timestamp including the specific year, month, day, and time that the customer ordered a product', 'orders'),
('product_quantity', 'BIG INT', 'Quantity of the product that the user ordered', 'orders'), 
('total_amount', 'DECIMAL (11, 2)', 'Total amount of customer`s order of the product', 'orders'),
('customer_id', 'INT', 'Foreign key linking to the customer name into the customers table', 'orders'),
('product_id', 'INT', 'Foreign key linking to the products name into the products table', 'orders');

CREATE TABLE constraints_metadata(constraint_name VARCHAR(40),
									constraint_type VARCHAR(40),
                                    column_name VARCHAR(40),
                                    table_name VARCHAR(40),
                                    PRIMARY KEY(constraint_name, table_name));

INSERT INTO constraints_metadata(constraint_name, constraint_type, column_name, table_name) 
VALUES ('fk_companies_business_categories', 'FOREIGN KEY' , 'category_id', 'companies'),
('fk_platforms_companies', 'FOREIGN KEY', 'company_id', 'platforms'),
('fk_employees_platforms', 'FOREIGN KEY', 'platform_id', 'employees_id'),
('fk_products_platforms', 'FOREIGN KEY', 'platform_id', 'products'),
('fk_orders_customers', 'FOREIGN KEY', 'customer_id', 'orders'),
('fk_orders_products', 'FOREIGN KEY', 'product_id', 'orders');

SELECT *
FROM columns_metadata;















