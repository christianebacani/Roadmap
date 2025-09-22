-- Create database
CREATE DATABASE IF NOT EXISTS
    food_delivery_app_db;

-- Use database
USE DATABASE
    food_delivery_app_db;


-- Restaurants table
CREATE OR REPLACE TABLE
    restaurants (
    restaurant_id NUMBER(38, 0) PRIMARY KEY,
    restaurant VARCHAR(255),
    address TEXT
    );

-- Shop types table
CREATE OR REPLACE TABLE
    shop_types (
    shop_type_id NUMBER(38, 0) PRIMARY KEY,
    shop_type VARCHAR(255)
    );

-- Shops table
CREATE OR REPLACE TABLE
    shops (
    shop_id NUMBER(38, 0) PRIMARY KEY,
    shop_type_id NUMBER(38, 0),
    shop VARCHAR(255),
    address TEXT
    );

-- Product categories table
CREATE OR REPLACE TABLE
    product_categories (
    product_category_id NUMBER(38, 0) PRIMARY KEY,
    product_category VARCHAR(255)
    );

-- Products table
CREATE OR REPLACE TABLE
    products (
    product_id NUMBER(38, 0) PRIMARY KEY,
    restaurant_id NUMBER(38, 0),
    shop_id NUMBER(38, 0),
    product_category_id NUMBER(38, 0),
    product VARCHAR(255),
    price NUMBER(11, 2)
    );

-- Delivery riders table
CREATE OR REPLACE TABLE
    delivery_riders (
    delivery_rider_id NUMBER(38, 0) PRIMARY KEY,
    first_name VARCHAR(255),
    middle_name VARCHAR(255),
    last_name VARCHAR(255),
    gender CHAR(6),
    contact_number CHAR(11),
    delivery_rider_since DATE
    );

-- Customers table
CREATE OR REPLACE TABLE
    customers (
    customer_id NUMBER(38, 0) PRIMARY KEY,
    first_name VARCHAR(255),
    middle_name VARCHAR(255),
    last_name VARCHAR(255),
    gender CHAR(6),
    contact_number CHAR(11),
    customer_since DATE
    );

-- Payment methods table
CREATE OR REPLACE TABLE
    payment_methods (
    payment_method_id NUMBER(38, 0) PRIMARY KEY,
    payment_method VARCHAR(255)
    );

-- Orders table
CREATE OR REPLACE TABLE
    orders (
    order_id NUMBER(38, 0) AUTOINCREMENT START 1 INCREMENT 1 PRIMARY KEY,
    delivery_rider_id (38, 0),
    customer_id NUMBER(38, 0),
    payment_method_id NUMBER(38, 0),
    recipient_full_name VARCHAR(255),
    order_datetime TIMESTAMP
    );


INSERT INTO
    restaurants (
    restaurant_id,
    restaurant,
    address
    )
    VALUES
    (1, 'Mang Inasal - Robinsons Tarlac', 'Robinsons Luisita McArthur Highway Barangay San Miguel 2nd District'),
    (2, 'Jollibee - Luisita', 'Plaza Luisita Mall McArthur Highway Barangay San Miguel 1st District'),
    (3, 'McDonald''s - Robinson''s Luisita', 'Mac Arthur Hiway San Miguel 1st District');

INSERT INTO
    shop_types (
    shop_type_id,
    shop_type
    )
    VALUES
    (1, 'Bakery'),
    (2, 'Bakery & Sweets'),
    (3, 'Health & Wellness'),
    (4, 'Pharmacy'),
    (5, 'Supermarket');

INSERT INTO
    shops (
    shop_id,
    shop_type_id,
    shop,
    address
    )
    VALUES
    (1, 2, 'Jelexie (San Miguel)', '28 McArthur Highway Barangay San Miguel 53rd District'),
    (2, 5, 'Puregold - Tarlac City', 'Palm Plaza Building, MacArthur Highway, Brgy.Matatalaib, Tarlac City, 2300 Tarlac, Philippines'),
    (3, 5, 'Robinson - Luisita', 'Luisita Access Road 2300 Tarlac City Tarlac');

INSERT INTO
    product_categories (
    product_category_id,
    product_category
    )
    VALUES
    (1, 'Food and Beverages'),
    (2, 'Beauty Products'),
    (3, 'Fashion & Accessories');

INSERT INTO
    products (
    product_id,
    restaurant_id,
    shop_id,
    product_category_id,
    product,
    price
    )
    VALUES
    (1, 1, NULL, 1, '2 Pc Pork BBQ Solo Fiesta', 225),
    (2, NULL, 3, 2, 
'Oxecure Facial Cleanser', 219),
    (3, 2, NULL, 1, '1 - pc. Chickenjoy w/ Jolly Spaghetti Solo', 152);

INSERT INTO
    delivery_riders (
    delivery_rider_id,
    first_name,
    middle_name,
    last_name,
    gender,
    contact_number,
    delivery_rider_since
    )
    VALUES
    (1, 'Saber', 'Smith', 'Sanford', 'Male', '09999999999', '2025-09-20'),
    (2, 'Layla', 'Shem', 'Shimineth', 'Female', '09999999998', '2025-09-15'),
    (3, 'Snoop', 'Lai', 'Dog', 'Male', '09999999997', '2025-09-20');

INSERT INTO
    customers (
    customer_id,
    first_name,
    middle_name,
    last_name,
    gender,
    contact_number,
    customer_since
    )
    VALUES
    (1, 'Chris', 'Agi', 'Bacs', 'Male', '09444444444', '2025-09-20'),
    (2, 'Yuki', 'Tilapia', 'Tilaps', 'Female', '09444444445', '2025-09-15'),
    (3, 'Flabby', 'Tilapia', 'Tilaps', 'Female', '09444444446', '2025-09-10');

INSERT INTO
    payment_methods (
    payment_method_id,
    payment_method
    )
    VALUES
    (1, 'Gcash'),
    (2, 'Link Bank Account'),
    (3, 'Cash on Delivery'),
    (4, 'Credit or Debit Card');


SELECT *
FROM
    orders;