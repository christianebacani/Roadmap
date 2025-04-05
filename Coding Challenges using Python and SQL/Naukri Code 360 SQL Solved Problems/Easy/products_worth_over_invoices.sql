-- Question: Product's Worth Over Invoices
-- Categories: Easy

SELECT
    Product.name AS name,
    SUM(Invoice.rest) AS rest,
    SUM(Invoice.paid) AS paid,
    SUM(Invoice.canceled) AS canceled,
    SUM(Invoice.refunded) AS refunded
FROM
    Invoice
INNER JOIN
    Product
ON
    Invoice.product_id = Product.product_id
GROUP BY
    Product.name
ORDER BY
    name;
