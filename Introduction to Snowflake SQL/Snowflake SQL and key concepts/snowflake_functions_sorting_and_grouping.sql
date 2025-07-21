/*
    Lesson: Snowflake Functions, sorting, and grouping
*/


// Item Delivery Application Database
USE DATABASE
    item_delivery_app_db;


// Customers Table
CREATE OR REPLACE TABLE
    customers (
    customer_id INTEGER PRIMARY KEY,
    first_name VARCHAR(255),
    middle_name VARCHAR(255),
    last_name VARCHAR(255),
    created_at TIMESTAMP_LTZ
    );

// Insert customers data to 'customers' table
INSERT INTO
    customers (
    customer_id,
    first_name,
    middle_name,
    last_name,
    created_at
    )
VALUES (1, 'chRistianE rhELY joSELLE', 'aguibitiN', 'bacani', CURRENT_TIMESTAMP());


// Item Categories Table
CREATE OR REPLACE TABLE
    item_categories (
    category_id INTEGER PRIMARY KEY,
    category VARCHAR(255)
    );

// Insert item category data to 'item_categories' table
INSERT INTO
    item_categories (
    category_id,
    category
    )
VALUES
    (1, 'Beauty Products'),
    (2, 'Food and Beverages'),
    (3, 'Gadgets');

    
// Items Table
CREATE OR REPLACE TABLE
    items (
    item_id INTEGER PRIMARY KEY,
    category_id INTEGER,
    item_name VARCHAR(255),
    price NUMBER(11, 2),
    FOREIGN KEY(category_id) REFERENCES item_categories(category_id)
    );

// Insert items data to 'items' table
INSERT INTO
    items (
    item_id,
    category_id,
    item_name,
    price
    )
VALUES
    (1, 1, 'Milk Scrub', 99.44),
    (2, 2, 'Buldak', 78.99),
    (3, 3, 'Samsung', 20999);


// Snowflake Functions
SELECT
    customer_id,
    first_name,
    INITCAP(first_name) AS cap_first_name // Using INITCAP() to capitalize each word of the string
FROM
    customers;

    
SELECT
    first_name,
    middle_name,
    last_name,
    CONCAT(first_name, ' ', middle_name, ' ', last_name) AS full_name, // Using CONCAT() to join strings into one single string
    CONCAT(INITCAP(first_name), ' ', INITCAP(middle_name), ' ', INITCAP(last_name)) AS cap_full_name // We can combine INITCAP() and CONCAT() for better data manipulation of string data types
FROM
    customers;


SELECT
    items.item_id,
    items.item_name,
    item_categories.category,
    CURRENT_DATE() AS date_item_was_created, // Using CURRENT_DATE() to display the current date
    CURRENT_TIME() as time_item_was_created // Using CURRENT_TIME() to display the current time
FROM
    items
INNER JOIN
    item_categories
ON
    items.category_id = item_categories.category_id;


SELECT
    customer_id,
    created_at,
    EXTRACT(YEAR FROM created_at) AS year_created // EXTRACT() to extract specific parts from date, time, datetime, or timestamp data
FROM
    customers;


SELECT
    item_id,
    item_categories.category_id,
    ROUND(AVG(price), 2) AS avg_price
FROM
    items
INNER JOIN
    item_categories
ON
    items.category_id = item_categories.category_id
GROUP BY ALL // USING 'GROUP BY ALL' to implicitly specify the columns to group that was specified in the 'SELECT' command
ORDER BY
    avg_price DESC;