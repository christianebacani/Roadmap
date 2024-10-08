-- Use any database
USE countries;

-- Subquery using SELECT keyword
SELECT
	country_name,
    (SELECT 
		ROUND(AVG(life_expectancy), 2)
	FROM populations AS p
    WHERE p.country_code = c.code) AS avg_life_exp
FROM countries AS c
ORDER BY avg_life_exp DESC
LIMIT 9;
-- Query the country and it`s average life expectancy




    




    


















































                        



                    
                      


    








    
































    


















    
    
    
    
    
    
    


































    

    

    











    

 








    















