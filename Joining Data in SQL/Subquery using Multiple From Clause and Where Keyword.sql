-- Use any database
USE practicedb;

-- Multiple FROM Clause using Subquery
DROP TABLE IF EXISTS global_suppliers;
DROP TABLE IF EXISTS local_suppliers;

-- Create
CREATE TABLE global_suppliers(supplier_id INT PRIMARY KEY,
				continent VARCHAR(20),
				supplier_name VARCHAR(50),
                                total_quantity INT,
                                total_price DECIMAL(11, 2));

CREATE TABLE local_suppliers(supplier_id INT PRIMARY KEY,
				continent VARCHAR(20),
				supplier_name VARCHAR(50),
                                total_quantity INT,
                                total_price DECIMAL(11, 2));
-- Insert
INSERT INTO global_suppliers(supplier_id, continent, supplier_name, total_quantity, total_price)
VALUES (1, 'North America', 'Google Corporations', 250, 500000), 
(2, 'Asia', 'Nvidia Corporations', 500, 125000), 
(3, 'Asia', 'Icreatechs', 200, 300000);



INSERT INTO local_suppliers(supplier_id, continent, supplier_name, total_quantity, total_price)
VALUES (1, 'North America', 'Google Corporations', 250, 500000), 
(2, 'North America', 'Netflix', 500, 400000), 
(3, 'North America', 'Meta', 600, 450500);


-- Use Multiple FROM Clause and WHERE Clause to filter and additional filters
SELECT
	global.continent,
    (local.total_quantity + global.total_quantity) AS total_quantity,
	(local.total_price + global.total_price) AS total_price
FROM local_suppliers AS local, (SELECT *
                        	FROM global_suppliers) AS global
WHERE local.continent = global.continent AND local.supplier_name = global.supplier_name;






	








      






    




    


















































                        



                    
                      


    








    
































    


















    
    
    
    
    
    
    


































    

    

    











    

 








    















