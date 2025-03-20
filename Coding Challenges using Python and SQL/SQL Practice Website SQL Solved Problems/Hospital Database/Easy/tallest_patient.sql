-- Question: Show the first_name, last_name, and height of the patient with the greatest height.
-- Category: Easy

SELECT
    first_name,
    last_name,
    height
FROM
    patients
ORDER BY
    height DESC
LIMIT
    1;
   
