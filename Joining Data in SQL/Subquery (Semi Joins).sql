-- Use any database 
USE countries;

-- Semi Joins (Subquery)
DROP TABLE IF EXISTS olympians;
DROP TABLE IF EXISTS winner_olympians;

-- Create columns
CREATE TABLE olympians(id INT PRIMARY KEY,
						name VARCHAR(50),
                        country VARCHAR(50));

CREATE TABLE winner_olympians(id INT PRIMARY KEY,
								name VARCHAR(50),
                                medal VARCHAR(50),
                                country VARCHAR(50));
                                
-- Insert the data
INSERT INTO olympians(id, name, country) 
VALUES (1, 'EJ Obiena', 'PH'), (2, 'Carlos Yulo', 'PH'), (3, 'Jenny Hoffman', 'PH');

INSERT INTO winner_olympians(id, name, medal, country) 
VALUES (1, 'Carlos Yulo', 'Gold', 'PH'), (2, 'Hidilyn Diaz', 'Gold', 'PH'), (3, 'Carlo Paalam', 'Bronze', 'PH');

-- Query
-- Semi Joins (Subquery)
SELECT
	name AS gold_medal_olympian,
    country
FROM olympians
WHERE name IN (SELECT
						name
				  FROM winner_olympians
				  WHERE medal = 'Gold');
                

    








    
































    


















    
    
    
    
    
    
    


































    

    

    











    

 








    















