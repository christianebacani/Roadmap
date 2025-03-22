-- Question: Show the ProductName, CompanyName, CategoryName from the products, suppliers, and categories table
-- Categories: Medium

SELECT
    products.product_name,
    suppliers.company_name,
    categories.category_name
FROM
    products
INNER JOIN
    categories
ON
    products.category_id = categories.category_id
INNER JOIN
    suppliers
ON
    products.supplier_id = suppliers.supplier_id;
