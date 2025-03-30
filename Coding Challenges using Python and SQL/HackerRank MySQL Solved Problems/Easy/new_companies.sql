-- Question: New Companies
-- Categories: Advanced Select

SELECT
    Company.company_code AS company_code,
    Company.founder AS founder,
    COUNT(DISTINCT Lead_Manager.lead_manager_code) AS total_number_of_lead_managers,
    COUNT(DISTINCT Senior_Manager.senior_manager_code) AS total_number_of_senior_managers,
    COUNT(DISTINCT Manager.manager_code) AS total_number_of_managers,
    COUNT(DISTINCT Employee.employee_code) AS total_number_of_employees
FROM
    Company
INNER JOIN
    Lead_Manager
ON
    Company.company_code = Lead_Manager.company_code
INNER JOIN
    Senior_Manager
ON
    Company.company_code = Senior_Manager.company_code
INNER JOIN
    Manager
ON
    Company.company_code = Manager.company_code
INNER JOIN
    Employee
ON
    Company.company_code = Employee.company_code
GROUP BY
    Company.company_code,
    Company.founder
ORDER BY
    Company.company_code ASC;

    