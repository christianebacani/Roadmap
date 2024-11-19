-- Database Name/Any Database
USE practicedb;

-- Hello! My name is Christiane A. Bacani a Data/DevOps Engineer

-- 8-Week SQL Challenge
-- Case Study #1 - Danny's Diner

DROP TABLE IF EXISTS sales;
DROP TABLE IF EXISTS members;
DROP TABLE IF EXISTS menu;

CREATE TABLE sales (
  customer_id VARCHAR(1),
  order_date DATE,
  product_id INTEGER
);

INSERT INTO sales
  (customer_id, order_date, product_id)
VALUES
  ('A', '2021-01-01', '1'),
  ('A', '2021-01-01', '2'), -- 24
  ('A', '2021-01-07', '2'), -- 30
  ('A', '2021-01-10', '3'), -- 24
  ('A', '2021-01-11', '3'), -- 24
  ('A', '2021-01-11', '3'), -- 24
  ('B', '2021-01-01', '2'),
  ('B', '2021-01-02', '2'),
  ('B', '2021-01-04', '1'),
  ('B', '2021-01-11', '1'),
  ('B', '2021-01-16', '3'),
  ('B', '2021-02-01', '3'),
  ('C', '2021-01-01', '3'),
  ('C', '2021-01-01', '3'),
  ('C', '2021-01-07', '3');
 

CREATE TABLE menu (
  product_id INTEGER,
  product_name VARCHAR(5),
  price INTEGER
);

INSERT INTO menu
  (product_id, product_name, price)
VALUES
  ('1', 'sushi', '10'),
  ('2', 'curry', '15'),
  ('3', 'ramen', '12');
  

CREATE TABLE members (
  customer_id VARCHAR(1),
  join_date DATE
);

INSERT INTO members
  (customer_id, join_date)
VALUES
  ('A', '2021-01-07'),
  ('B', '2021-01-09');








-- 1.) What is the total amount each customer spent at the restaurant?
SELECT
    customer_id,
    SUM(price) AS total_customer_spent
FROM sales
INNER JOIN menu
USING(product_id)
GROUP BY 
	customer_id;

-- 2.) How many days has each customer visited the restaurant?
SELECT
    customer_id,
    COUNT(DISTINCT order_date) AS number_days
FROM sales
INNER JOIN menu
USING(product_id)
GROUP BY
	customer_id;


-- 3.) What was the first item from the menu purchased by each customer?
SELECT
    customer_id,
    product_id,
    product_name
FROM (
SELECT
	*,
	ROW_NUMBER() OVER (PARTITION BY customer_id
	ORDER BY order_date) AS visit
FROM sales
INNER JOIN menu
USING(product_id)
) AS subquery
WHERE 
	visit = 1;

-- 4.) What was the first item from the menu purchased by each customer?
SELECT	
	product_id,
    	COUNT(product_id) AS purchased_count
FROM sales
GROUP BY
	product_id
ORDER BY 
	purchased_count DESC;

-- 5.) Which item was the most popular for each customer?
WITH cte AS (SELECT 
		*,
		ROW_NUMBER() OVER (PARTITION BY sub.customer_id ORDER BY purchased_count DESC) AS popular_product_rank
FROM (SELECT 
		customer_id,
		product_id,
		COUNT(product_id) AS purchased_count
	  FROM sales
	  GROUP BY 
		customer_id, product_id
	  ORDER BY
		purchased_count DESC) AS sub -- Subquery using From Clause of the total number of orders per product, and customer
ORDER BY 
	popular_product_rank)

SELECT
    customer_id,
    product_id,
    purchased_count
FROM cte
WHERE popular_product_rank = 1;

-- 6.) Which item was purchased first by the customer after they became a member?
WITH cte AS (
SELECT
	* 
FROM (
SELECT *,
        ROW_NUMBER() OVER (PARTITION BY customer_id ORDER BY join_date) AS join_date_sort
FROM sales
INNER JOIN members
USING(customer_id)
ORDER BY 
	customer_id, join_date_sort) AS sub
WHERE 
	(customer_id = 'A' AND order_date > '2021-01-07') OR (customer_id = 'B' AND order_date > '2021-01-09')
)
SELECT
    customer_id,
    product_id
FROM cte
WHERE 
	join_date_sort = 4;


 -- 7.) Which item was purchased just before the customer became a member?
 WITH cte AS (
 SELECT
    sales.customer_id,
    sales.product_id,
    sales.order_date,
    members.join_date,
    ROW_NUMBER() OVER (PARTITION BY sales.customer_id
ORDER BY 
	 sales.order_date) transaction_history_asc
FROM sales
JOIN members
	ON members.customer_id = sales.customer_id
WHERE 
	  (sales.customer_id = 'A' AND order_date < '2021-01-07') OR 
	  (sales.customer_id = 'B' AND order_date < '2021-01-09')
ORDER BY 
	 sales.customer_id
)
SELECT *
FROM cte; -- Customer C purchased product_id = 3 which is ramen and didn`t became a member


-- 8.) What is the total items and amount spent for each member before they became a member?
SELECT 
    sales.customer_id, 
    COUNT(sales.product_id) AS total_items,
    SUM(menu.price) AS total_price
FROM members
INNER JOIN sales
USING(customer_id) 
INNER JOIN menu
	ON menu.product_id = sales.product_id
WHERE 
	(customer_id = 'A' AND order_date > '2021-01-07') OR (customer_id = 'B' AND order_date > '2021-01-09')
GROUP BY
	sales.customer_id
UNION
SELECT 
    sales.customer_id,
    COUNT(sales.product_id) AS total_items,
    SUM(menu.price) AS total_price
FROM sales
INNER JOIN menu
USING(product_id) 
WHERE sales.customer_id = 'C'
GROUP BY 
	sales.customer_id
ORDER BY
	total_price DESC;

-- 9.) If each $1 spent equates to 10 points and sushi has a 2x points multiplier - how many points would each customer have?
SELECT
    customer_id,
    SUM(CASE WHEN sales.product_id = '1' THEN menu.price * 20 ELSE menu.price * 10 END) AS total_points
FROM sales
INNER JOIN menu
USING(product_id)
GROUP BY 
	customer_id;


-- 10.) In the first week after a customer joins the program (including their join date) they earn 2x points on all items, not just sushi - how many points do customer A and B have at the end of January?

SELECT
    customer_id,
    SUM(CASE WHEN order_date BETWEEN '2021-01-07' AND '2021-01-13' THEN (menu.price * 2) ELSE menu.price * 1 END) AS total_points
FROM sales
INNER JOIN menu
USING(product_id)
WHERE 
	customer_id = 'A' AND order_date <= '2021-01-31'
GROUP BY
	customer_id
UNION ALL
SELECT 
    customer_id,
    SUM(CASE WHEN order_date BETWEEN '2021-01-09' AND '2021-01-15' THEN (menu.price * 2) ELSE (menu.price * 1) END) AS total_points
FROM sales
INNER JOIN menu
	USING(product_id)
WHERE 
	customer_id = 'B' AND order_date <= '2021-01-31'
GROUP BY
	customer_id;
