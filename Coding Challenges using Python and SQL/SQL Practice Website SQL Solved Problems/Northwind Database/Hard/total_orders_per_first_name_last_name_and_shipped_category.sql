-- Question: Show the employee's first_name and last_name, a "num_orders" column with a count of the orders taken, and a column called "Shipped" that displays "On Time" if the order shipped_date is less or equal to the required_date, "Late" if the order shipped late, "Not Shipped" if shipped_date is null. Order by employee last_name, then by first_name, and then descending by number of orders.
-- Categories: Hard

WITH
    employee_orders AS (
SELECT
    employees.first_name,
    employees.last_name,
    orders.order_id,
    CASE
        WHEN orders.shipped_date <= orders.required_date THEN 'On Time'
        WHEN orders.shipped_date > orders.required_date THEN 'Late'
        WHEN orders.shipped_date IS NULL THEN 'Not Shipped'
    END AS shipped
FROM
    orders
INNER JOIN
    employees
ON
    orders.employee_id = employees.employee_id)

SELECT
    first_name,
    last_name,
    COUNT(order_id) AS num_orders,
    shipped
FROM
    employee_orders
GROUP BY
    first_name,
    last_name,
    shipped
ORDER BY
    last_name ASC,
    first_name ASC,
    num_orders DESC;