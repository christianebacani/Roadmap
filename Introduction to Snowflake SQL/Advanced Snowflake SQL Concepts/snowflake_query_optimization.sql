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
    (1, 'Mang Inasal - Robinsons Tarlac', 'Robinsons Luisita McArthur Highway Barangay San Miguel 2nd District');

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
    (1, 2, 'Jelexie (San Miguel)', '28 McArthur Highway Barangay San Miguel 53rd District');

INSERT INTO
    product_categories (
    product_category_id,
    product_category
    )
    VALUES
    (1, 'Food and Beverages');


SELECT *
FROM
    products;