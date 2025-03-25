-- 11.) Actors' last name
-- Categories: Easy

SELECT
    last_name,
    COUNT(*) AS count
FROM
    actor
WHERE
    last_name IN ('DAVIS', 'BRODY', 'ALLEN', 'BERRY')
GROUP BY 
    last_name;

