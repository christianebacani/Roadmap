-- Use any database
USE countries;

-- Set Theory using Except
DROP TABLE IF EXISTS supplies;
DROP TABLE IF EXISTS global_suppliers;

-- Create
CREATE TABLE supplies(supply_id INT PRIMARY KEY,
						supply_name VARCHAR(50),
                        supplier_name VARCHAR(50));

CREATE TABLE global_suppliers(supplier_id INT PRIMARY KEY,
						supplier_name VARCHAR(50));

-- Insert
INSERT INTO supplies(supply_id, supply_name, supplier_name) 
VALUES (1, 'Laptop', 'Huawei Corporation'), (2, 'Smartphone', 'Google Corporation'), (3, 'Foods', 'Mcdonalds');


INSERT INTO global_suppliers(supplier_id, supplier_name) 
VALUES (1, 'Google Corporation'), (2, 'Nvidia Corporation'), (3, 'Intel Corporation');


-- Query using EXCEPT
SELECT
	supplier_name AS supplier
FROM supplies
EXCEPT
SELECT
	supplier_name
FROM global_suppliers;






                        



                    
                      


    








    
































    


















    
    
    
    
    
    
    


































    

    

    











    

 








    















