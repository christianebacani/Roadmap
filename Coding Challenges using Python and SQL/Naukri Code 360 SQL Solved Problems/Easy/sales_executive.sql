-- Question: Sales Executive
-- Categories: Easy

WITH
    combined_table_of_red_company_sales AS (
SELECT
    Orders.order_id,
    Orders.order_date,
    Orders.amount,
    Salesperson.name AS salesperson_name,
    Company.name AS company_name
FROM
    Orders
INNER JOIN
    Salesperson
ON
    Orders.sales_id = Salesperson.sales_id
INNER JOIN
    Company
ON
    Orders.com_id = Company.com_id
WHERE
    Company.name = 'RED')

SELECT
    Salesperson.name
FROM
    Salesperson
WHERE
    Salesperson.name NOT IN (SELECT combined_table_of_red_company_sales.salesperson_name FROM combined_table_of_red_company_sales);

