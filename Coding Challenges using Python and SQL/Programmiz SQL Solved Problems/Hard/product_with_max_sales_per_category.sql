-- Question: Write an SQL query to return the product with the highest total sales amount within each category
-- Categories: Hard

SELECT
    category,
    product_name,
    sales_amount AS max_sales_amount
FROM
    Sales_Data
WHERE
    sales_amount = (SELECT MAX(sales_amount) FROM Sales_Data AS Inner_Table WHERE Inner_Table.category = Sales_Data.category);