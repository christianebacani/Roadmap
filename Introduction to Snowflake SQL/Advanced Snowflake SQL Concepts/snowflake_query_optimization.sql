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
    (2, NULL, 3, 2, 'Oxecure Facial Cleanser', 219),
    (3, 2, NULL, 1, '1 - pc. Chickenjoy w/ Jolly Spaghetti Solo', 152);


SELECT *
FROM
    products;