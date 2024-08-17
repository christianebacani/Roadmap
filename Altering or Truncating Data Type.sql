-- Database Name
USE practicedb;

-- Domain Attribute Constraints / Altering or Truncating Data Type
-- Domain : Set of Properties that allow a specific permissible values

-- Drop Tables
DROP TABLE IF EXISTS customers;
DROP TABLE IF EXISTS malls;
DROP TABLE IF EXISTS corporations;

-- Create Tables
CREATE TABLE corporations(corporation_id INT PRIMARY KEY,
							corporation_name VARCHAR(150) NOT NULL);

CREATE TABLE malls(id INT PRIMARY KEY,
					corporation_id INT,
					mall_name VARCHAR(150) DEFAULT 'N/A',
                    location TEXT,
                    FOREIGN KEY (corporation_id) REFERENCES corporations(corporation_id)
                    ON UPDATE CASCADE
                    ON DELETE CASCADE); 
                    

CREATE TABLE customers(customer_id INT PRIMARY KEY,
						id INT,
						customer_name VARCHAR(150) DEFAULT 'N/A',
                        total_spent NUMERIC(11, 2),
                        gender CHAR(1), CHECK(gender = 'M' OR gender = 'F'),
                        FOREIGN KEY (id) REFERENCES malls(id)
                        ON DELETE CASCADE);

-- Changing Data Type
ALTER TABLE corporations
MODIFY COLUMN corporation_name TEXT;

-- Truncating Data Type
ALTER TABLE customers
MODIFY COLUMN total_spent INT;


-- Insert Tables
INSERT INTO corporations(corporation_id, corporation_name) 
VALUES (1, 'SM Prime Holdings, INC.');

INSERT INTO malls(id, corporation_id, mall_name, location) 
VALUES (1, 1, 'SM Tarlac', 'Tarlac City, Tarlac'), (2, 1, 'SM Bataan', 'Balanga City, Bataan');

INSERT INTO customers(customer_id, id, customer_name, total_spent, gender) 
VALUES (1, 1, 'Rica Mae', 314, 'F'), (2, 2, 'Christiane', 64, 'M');

-- Query
SELECT *
FROM customers
INNER JOIN malls
	USING(id) 
INNER JOIN corporations
	ON corporations.corporation_id = malls.corporation_id;
    


    







