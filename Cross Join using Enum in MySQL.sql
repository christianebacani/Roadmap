-- Use any database 
USE countries;


DROP TABLE IF EXISTS chocolates;
DROP TABLE IF EXISTS ice_creams;
DROP TABLE IF EXISTS drinks;

CREATE TABLE chocolates(id INT PRIMARY KEY,
						available_chocolates ENUM('Toblerone', 'Goya', 'BengBeng'),
                        price INT,
                        datetime_ordered TIMESTAMP DEFAULT CURRENT_TIMESTAMP);

CREATE TABLE ice_creams(id INT PRIMARY KEY,
						available_ice_creams ENUM('Strawberry', 'Chocolates', 'Cookies and Cream'),
                        price INT,
                        datetime_ordered TIMESTAMP DEFAULT CURRENT_TIMESTAMP);
                        
CREATE TABLE drinks(id INT PRIMARY KEY,
						available_drinks ENUM('Softdrinks', 'Juice', 'Shakes'),
                        price INT,
                        datetime_ordered TIMESTAMP DEFAULT CURRENT_TIMESTAMP);
                        

INSERT INTO chocolates(id, available_chocolates, price) 
VALUES (1, 1, 30), (2, 2, 25), (3, 3, 20);

INSERT INTO ice_creams(id, available_ice_creams, price) 
VALUES (1, 1, 15), (2, 3, 15), (3, 2, 15);

INSERT INTO drinks(id, available_drinks, price) 
VALUES (1, 3, 20), (2, 2, 15), (3, 1, 15);

SELECT
	available_chocolates,
    c.price AS chocolate_price,
    available_ice_creams,
    i.price AS ice_cream_price,
    available_drinks, 
    d.price AS drink_price
FROM chocolates AS c
CROSS JOIN ice_creams AS i
CROSS JOIN drinks AS d
ORDER BY available_chocolates, available_ice_creams;


    

 








    















