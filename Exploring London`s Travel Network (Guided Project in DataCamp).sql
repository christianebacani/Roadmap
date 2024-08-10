-- Use any database
USE countries;

-- Exploring London`s Travel Network (Guided Project in DataCamp)

-- Total number of journeys per journey type
SELECT
	journey_type,
    SUM(journeys_millions) AS total_journeys_millions
FROM journeys
GROUP BY journey_type
ORDER BY total_journeys_millions DESC;


-- Five months, and years that is most popular journeys for Emirates Airline
SELECT
	month,
    year,
    ROUND(journeys_millions, 2) AS journeys_millions
FROM journeys
WHERE journey_type = 'Emirates Airline' AND (month IS NOT NULL AND year IS NOT NULL AND journeys_millions IS NOT NULL)
ORDER BY journeys_millions DESC
LIMIT 5;


SELECT
	year,
    journey_type,
    SUM(journeys_millions) AS journeys_millions
FROM journeys
WHERE journey_type = 'Underground & DLR'
GROUP BY year, journey_type
ORDER BY journeys_millions
LIMIT 5;



























	








      






    




    


















































                        



                    
                      


    








    
































    


















    
    
    
    
    
    
    


































    

    

    











    

 








    















