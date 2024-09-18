-- Use any database 
USE countries;

-- Using Union, Union All for Set Theory
-- Drops the table if it`s exists in database
DROP TABLE IF EXISTS google_developers;
DROP TABLE IF EXISTS microsoft_developers;

-- Create
CREATE TABLE google_developers(developer_id INT PRIMARY KEY,
								developer_name VARCHAR(50),
                                salary INT);

CREATE TABLE microsoft_developers(developer_id INT PRIMARY KEY,
									developer_name VARCHAR(50),
                                    salary INT);
-- Insert
INSERT INTO google_developers(developer_id, developer_name, salary) 
VALUES (1, 'Christiane Bacani', 250000), (2, 'Rica Mae Flores', 300000), (3, 'Nicko De Guzman', 120000);

INSERT INTO microsoft_developers(developer_id, developer_name, salary) 
VALUES (1, 'Nathaniel Dela Rosa', 90000), (2, 'Crj Perez', 11000);

-- Perform Union all(Joining two tables with duplicates)
SELECT
	developer_name AS google_dev,
    salary AS dev_salary
FROM google_developers
UNION ALL
SELECT
	developer_name AS microsoft_dev,
    salary AS dev_salary
FROM microsoft_developers
ORDER BY dev_salary;
























    

    

    











    

 








    















