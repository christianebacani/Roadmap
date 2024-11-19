-- Database Name/Any Database
USE practicedb;

-- 8-Week SQL Challenge
-- Case Study #2 - Pizza Runner


-- Drop Table
DROP TABLE IF EXISTS pizza_toppings;
DROP TABLE IF EXISTS pizza_recipes;
DROP TABLE IF EXISTS pizza_names;
DROP TABLE IF EXISTS customer_orders;
DROP TABLE IF EXISTS runner_orders;
DROP TABLE IF EXISTS runners;


-- Define the Schema
CREATE TABLE runners (
  runner_id INTEGER,
  registration_date DATE
);
INSERT INTO runners
  (runner_id, registration_date)
VALUES
  (1, '2021-01-01'),
  (2, '2021-01-03'),
  (3, '2021-01-08'),
  (4, '2021-01-15');


DROP TABLE IF EXISTS customer_orders;
CREATE TABLE customer_orders (
  order_id INTEGER,
  customer_id INTEGER,
  pizza_id INTEGER,
  exclusions VARCHAR(4),
  extras VARCHAR(4),
  order_time TIMESTAMP
);

INSERT INTO customer_orders
  (order_id, customer_id, pizza_id, exclusions, extras, order_time)
VALUES
  ('1', '101', '1', '', '', '2020-01-01 18:05:02'),
  ('2', '101', '1', '', '', '2020-01-01 19:00:52'),
  ('3', '102', '1', '', '', '2020-01-02 23:51:23'),
  ('3', '102', '2', '', NULL, '2020-01-02 23:51:23'),
  ('4', '103', '1', '4', '', '2020-01-04 13:23:46'),
  ('4', '103', '1', '4', '', '2020-01-04 13:23:46'),
  ('4', '103', '2', '4', '', '2020-01-04 13:23:46'),
  ('5', '104', '1', 'null', '1', '2020-01-08 21:00:29'),
  ('6', '101', '2', 'null', 'null', '2020-01-08 21:03:13'),
  ('7', '105', '2', 'null', '1', '2020-01-08 21:20:29'),
  ('8', '102', '1', 'null', 'null', '2020-01-09 23:54:33'),
  ('9', '103', '1', '4', '1, 5', '2020-01-10 11:22:59'),
  ('10', '104', '1', 'null', 'null', '2020-01-11 18:34:49'),
  ('10', '104', '1', '2, 6', '1, 4', '2020-01-11 18:34:49');


DROP TABLE IF EXISTS runner_orders;
CREATE TABLE runner_orders (
  order_id INTEGER,
  runner_id INTEGER,
  pickup_time VARCHAR(19),
  distance VARCHAR(7),
  duration VARCHAR(10),
  cancellation VARCHAR(23)
);

INSERT INTO runner_orders
  (order_id, runner_id, pickup_time, distance, duration, cancellation)
VALUES
  ('1', '1', '2020-01-01 18:15:34', '20km', '32 minutes', ''),
  ('2', '1', '2020-01-01 19:10:54', '20km', '27 minutes', ''),
  ('3', '1', '2020-01-03 00:12:37', '13.4km', '20 mins', NULL),
  ('4', '2', '2020-01-04 13:53:03', '23.4', '40', NULL),
  ('5', '3', '2020-01-08 21:10:57', '10', '15', NULL),
  ('6', '3', 'null', 'null', 'null', 'Restaurant Cancellation'),
  ('7', '2', '2020-01-08 21:30:45', '25km', '25mins', 'null'),
  ('8', '2', '2020-01-10 00:15:02', '23.4 km', '15 minute', 'null'),
  ('9', '2', 'null', 'null', 'null', 'Customer Cancellation'),
  ('10', '1', '2020-01-11 18:50:20', '10km', '10minutes', 'null');


DROP TABLE IF EXISTS pizza_names;
CREATE TABLE pizza_names (
  pizza_id INTEGER,
  pizza_name TEXT
);
INSERT INTO pizza_names
  (pizza_id, pizza_name)
VALUES
  (1, 'Meatlovers'),
  (2, 'Vegetarian');


DROP TABLE IF EXISTS pizza_recipes;
CREATE TABLE pizza_recipes (
  pizza_id INTEGER,
  toppings TEXT
);
INSERT INTO pizza_recipes
  (pizza_id, toppings)
VALUES
  (1, '1, 2, 3, 4, 5, 6, 8, 10'),
  (2, '4, 6, 7, 9, 11, 12');
  
DROP TABLE IF EXISTS pizza_toppings;
CREATE TABLE pizza_toppings (
  topping_id INTEGER,
  topping_name TEXT
);
INSERT INTO pizza_toppings
  (topping_id, topping_name)
VALUES
  (1, 'Bacon'),
  (2, 'BBQ Sauce'),
  (3, 'Beef'),
  (4, 'Cheese'),
  (5, 'Chicken'),
  (6, 'Mushrooms'),
  (7, 'Onions'),
  (8, 'Pepperoni'),
  (9, 'Peppers'),
  (10, 'Salami'),
  (11, 'Tomatoes'),
  (12, 'Tomato Sauce');

-- Data Cleaning
UPDATE customer_orders
SET extras = 0
WHERE 
	extras = '' OR extras = 'null' OR extras IS NULL;

UPDATE customer_orders
SET exclusions = 0
WHERE exclusions = '' OR exclusions = 'null';


-- 1.) What are the standard ingredients for each pizza?
SELECT *
FROM pizza_names
INNER JOIN pizza_recipes
USING(pizza_id); 


-- 2.) What was the most commonly added extra?
SELECT
     extras,
    COUNT(extras) AS total_extras_per_orders
FROM customer_orders
WHERE 
	extras <> 0
GROUP BY
	extras;


-- 3.) What was the most common exclusion?
SELECT 
    exclusions,
    COUNT(exclusions) AS total_exclusions_per_orders
FROM customer_orders
WHERE 
	exclusions <> 0
GROUP BY 
	exclusions;


-- 4.) Generate an order item for each record in the customers_orders table in the format of one of the following:
-- Meat Lovers
-- Meat Lovers - Exclude Beef '3'
-- Meat Lovers - Extra Bacon '1'
-- Meat Lovers - Exclude Cheese '4', Bacon '1' - Extra Mushroom '6', Peppers '9'
SELECT
	order_id AS `Meat Lovers`
FROM customer_orders
WHERE 
	pizza_id = 1;

SELECT 
	order_id AS `Meat Lovers - Exclude Beef '3'`
FROM customer_orders
WHERE 
	pizza_id = 1 AND exclusions LIKE '%3%'

UNION ALL
SELECT 
	order_id AS `Meat Lovers - Exclude Beef '3'`
FROM customer_orders
WHERE 
	pizza_id = 1 AND exclusions LIKE '%3%';

SELECT 
	order_id AS `Meat Lovers - Extra Bacon '1'`
FROM customer_orders
WHERE 
	pizza_id = 1 AND extras LIKE '%1%';

SELECT
	order_id AS `Meat Lovers - Exclude Cheese '4', Bacon '1' - Extra Mushrooms '6', Peppers '9'`
FROM customer_orders
WHERE 
	pizza_id = 1 AND (exclusions LIKE '%4%' OR exclusions LIKE '%1%') AND (extras LIKE '%6%' OR extras LIKE '%9%');
 
 
 -- 5.) Generate an alphabetically ordered comma separated ingredient list for each pizza order from the customer_orders table and add a 2x in front of any relevant ingredients
-- For example: "Meat Lovers: 2xBacon, Beef, ... , Salami"
 WITH cte AS(
SELECT
    order_id,
    (CASE
	WHEN extras LIKE '%1, 5%' THEN '2xBacon, BBQ Sauce, Beef, Cheese, 2xChicken, Mushrooms, Onions, Pepperoni, Peppers, Salami, Tomatoes, Tomato Sauce'
        WHEN extras LIKE '%1, 4%' THEN '2xBacon, BBQ Sauce, Beef, 2xCheese, Chicken, Mushrooms, Onions, Pepperoni, Peppers, Salami, Tomatoes, Tomato Sauce'
	WHEN extras LIKE '%1%' THEN '2xBacon, BBQ Sauce, Beef, Cheese, Chicken, Mushrooms, Onions, Pepperoni, Peppers, Salami, Tomatoes, Tomato Sauce'
        WHEN extras LIKE '%2%' THEN 'Bacon, 2xBBQ Sauce, Beef, Cheese, Chicken, Mushrooms, Onions, Pepperoni, Peppers, Salami, Tomatoes, Tomato Sauce'
        WHEN extras LIKE '%3%' THEN 'Bacon, BBQ Sauce, 2xBeef, Cheese, Chicken, Mushrooms, Onions, Pepperoni, Peppers, Salami, Tomatoes, Tomato Sauce'
        WHEN extras LIKE '%4%' THEN 'Bacon, BBQ Sauce, Beef, 2xCheese, Chicken, Mushrooms, Onions, Pepperoni, Peppers, Salami, Tomatoes, Tomato Sauce'
        WHEN extras LIKE '%5%' THEN 'Bacon, BBQ Sauce, Beef, Cheese, 2xChicken, Mushrooms, Onions, Pepperoni, Peppers, Salami, Tomatoes, Tomato Sauce'
        WHEN extras LIKE '%6%' THEN 'Bacon, BBQ Sauce, Beef, Cheese, Chicken, 2xMushrooms, Onions, Pepperoni, Peppers, Salami, Tomatoes, Tomato Sauce'
        WHEN extras LIKE '%7%' THEN 'Bacon, BBQ Sauce, Beef, Cheese, Chicken, Mushrooms, 2xOnions, Pepperoni, Peppers, Salami, Tomatoes, Tomato Sauce'
        WHEN extras LIKE '%8%' THEN 'Bacon, BBQ Sauce, Beef, Cheese, Chicken, Mushrooms, Onions, 2xPepperoni, Peppers, Salami, Tomatoes, Tomato Sauce' 
        WHEN extras LIKE '%9%' THEN 'Bacon, BBQ Sauce, Beef, Cheese, Chicken, Mushrooms, Onions, Pepperoni, 2xPeppers, Salami, Tomatoes, Tomato Sauce'
        WHEN extras LIKE '%10%' THEN 'Bacon, BBQ Sauce, Beef, Cheese, Chicken, Mushrooms, Onions, Pepperoni, Peppers, 2xSalami, Tomatoes, Tomato Sauce' 
        WHEN extras LIKE '%11%' THEN 'Bacon, BBQ Sauce, Beef, Cheese, Chicken, Mushrooms, Onions, Pepperoni, Peppers, Salami, 2xTomatoes, Tomato Sauce' 
        WHEN extras LIKE '%12%' THEN 'Bacon, BBQ Sauce, Beef, Cheese, Chicken, Mushrooms, Onions, Pepperoni, Peppers, Salami, Tomatoes, 2xTomato Sauce'
	END) AS ingredient_list
FROM customer_orders
WHERE 
	 pizza_id = 1 AND extras <> '0'
ORDER BY 
	 ingredient_list
)

SELECT 
    cte.order_id,
    customer_id,
    CONCAT('Meat Lovers: ', cte.ingredient_list) AS ingredient_list
FROM customer_orders
INNER JOIN cte
	ON cte.order_id = customer_orders.order_id
WHERE 
	 customer_orders.pizza_id = 1 AND customer_orders.extras <> '0'
ORDER BY 
	 ingredient_list;


-- 6.) What is the total quantity of each ingredient used in all delivered pizzas sorted by most frequent first?
WITH toppings_count AS (
SELECT
    '1' AS ingredient,
    SUM(CASE WHEN extras LIKE '%1%' AND runner_orders.cancellation REGEXP '[null|NULL|'']' THEN 1 ELSE 0 END) AS ingredient_count
FROM runner_orders
INNER JOIN customer_orders
USING(order_id)

UNION ALL 

SELECT
    '4' AS ingredient,
    SUM(CASE WHEN extras LIKE '%4%' AND runner_orders.cancellation REGEXP '[null|NULL|'']' THEN 1 ELSE 0 END) AS ingredient_count
FROM runner_orders
INNER JOIN customer_orders
USING(order_id)
    
UNION ALL 

SELECT
    '5' AS ingredient,
    SUM(CASE WHEN extras LIKE '%5%' AND runner_orders.cancellation REGEXP '[null|NULL|'']' THEN 1 ELSE 0 END) AS ingredient_count
FROM runner_orders
INNER JOIN customer_orders
USING(order_id)

UNION ALL

SELECT
    '1' AS ingredient,
    SUM(CASE WHEN (customer_orders.pizza_id = 1 AND exclusions NOT LIKE '%1%') AND runner_orders.cancellation REGEXP '[null|NULL|'']' THEN 1 ELSE 0 END) AS ingredient_count
FROM runner_orders
INNER JOIN customer_orders
USING(order_id)

UNION 

SELECT
    '2' AS ingredient,
    SUM(CASE WHEN (customer_orders.pizza_id = 1 AND exclusions NOT LIKE '%2%') AND runner_orders.cancellation REGEXP '[null|NULL|'']' THEN 1 ELSE 0 END) AS ingredient_count
FROM runner_orders
INNER JOIN customer_orders
USING(order_id)
    
UNION 

SELECT
    '3' AS ingredient,
    SUM(CASE WHEN (customer_orders.pizza_id = 1 AND exclusions NOT LIKE '%3%') AND runner_orders.cancellation REGEXP '[null|NULL|'']' THEN 1 ELSE 0 END) AS ingredient_count
FROM runner_orders
INNER JOIN customer_orders
USING(order_id)
    
UNION 

SELECT
    '4' AS ingredient,
    SUM(CASE WHEN (customer_orders.pizza_id IS NOT NULL AND exclusions NOT LIKE '%4%') AND runner_orders.cancellation REGEXP '[null|NULL|'']' THEN 1 ELSE 0 END) AS ingredient_count
FROM runner_orders
INNER JOIN customer_orders
USING(order_id)

UNION

SELECT
    '5' AS ingredient,
    SUM(CASE WHEN (customer_orders.pizza_id = 1 AND exclusions NOT LIKE '%5%') AND runner_orders.cancellation REGEXP '[null|NULL|'']' THEN 1 ELSE 0 END) AS ingredient_count
FROM runner_orders
INNER JOIN customer_orders
USING(order_id)
    
UNION

SELECT
    '6' AS ingredient,
    SUM(CASE WHEN (customer_orders.pizza_id IS NOT NULL AND exclusions NOT LIKE '%6%') AND runner_orders.cancellation REGEXP '[null|NULL|'']' THEN 1 ELSE 0 END) AS ingredient_count
FROM runner_orders
INNER JOIN customer_orders
USING(order_id)
    
UNION

SELECT  
    '7' AS ingredient,
    SUM(CASE WHEN (customer_orders.pizza_id = 2 AND exclusions NOT LIKE '%7%') AND runner_orders.cancellation REGEXP '[null|NULL|'']' THEN 1 ELSE 0 END) AS ingredient_count
FROM runner_orders
INNER JOIN customer_orders
USING(order_id)
    
UNION
 
SELECT 
    '8' AS ingredient,
    SUM(CASE WHEN (customer_orders.pizza_id = 1 AND exclusions NOT LIKE '%8%') AND runner_orders.cancellation REGEXP '[null|NULL|'']' THEN 1 ELSE 0 END) AS ingredient_count
FROM runner_orders
INNER JOIN customer_orders
USING(order_id)

UNION 
 
SELECT 
    '9' AS ingredient,
    SUM(CASE WHEN (customer_orders.pizza_id = 2 AND exclusions NOT LIKE '%9%') AND runner_orders.cancellation REGEXP '[null|NULL|'']' THEN 1 ELSE 0 END) AS ingredient_count
FROM runner_orders
INNER JOIN customer_orders
USING(order_id)

UNION

SELECT 
    '10' AS ingredient,
    SUM(CASE WHEN (customer_orders.pizza_id = 1 AND exclusions NOT LIKE '%10%') AND runner_orders.cancellation REGEXP '[null|NULL|'']' THEN 1 ELSE 0 END) AS ingredient_count
FROM runner_orders
INNER JOIN customer_orders
USING(order_id)
    
UNION

SELECT 
    '11' AS ingredient,
    SUM(CASE WHEN (customer_orders.pizza_id = 2 AND exclusions NOT LIKE '%11%') AND runner_orders.cancellation REGEXP '[null|NULL|'']' THEN 1 ELSE 0 END) AS ingredient_count
FROM runner_orders
INNER JOIN customer_orders
USING(order_id)   

UNION

SELECT 
    '12' AS ingredient,
    SUM(CASE WHEN (customer_orders.pizza_id = 2 AND exclusions NOT LIKE '%12%') AND runner_orders.cancellation REGEXP '[null|NULL|'']' THEN 1 ELSE 0 END) AS ingredient_count
FROM runner_orders
INNER JOIN customer_orders
USING(order_id)
)

SELECT
    ingredient,
    SUM(ingredient_count) AS total_ingredient_count
FROM toppings_count
GROUP BY 
	ingredient
ORDER BY
	total_ingredient_count DESC;








