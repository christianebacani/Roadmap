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

-- Product categories table
CREATE OR REPLACE TABLE
    product_categories (
    product_category_id NUMBER(38, 0) PRIMARY KEY,
    product_category VARCHAR(255)
    );


INSERT INTO
    restaurants (
    restaurant_id,
    restaurant,
    address
    )
    VALUES
    (1, 'Mcdonalds Luisita', 'Luisita Access Road 2300 Tarlac City Tarlac');

INSERT INTO
    product_categories (
    product_category_id,
    product_category
    )
    VALUES
    (1, 'Food and Beverages');


SELECT *
FROM
    product_categories;