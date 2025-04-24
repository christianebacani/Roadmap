-- Question: Write an SQL query to retrieve employees with non-standard job titles
-- Categories: Medium

SELECT
    emp_name
FROM
    Employees
WHERE
    job_title NOT LIKE '%Manager%' AND
    job_title NOT LIKE '%Engineer%';
