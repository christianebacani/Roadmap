-- Create database
CREATE DATABASE IF NOT EXISTS
    food_delivery_app_db;

-- Use database
USE DATABASE
    food_delivery_app_db;


-- Restaurant categories table
CREATE OR REPLACE TABLE
    restaurant_categories (
    restaurant_category_id NUMBER(38, 0) PRIMARY KEY,
    restaurant_category VARCHAR(255)
    );

-- Restaurants table
CREATE OR REPLACE TABLE
    restaurants (
    restaurant_id NUMBER(38, 0) PRIMARY KEY,
    restaurant_category_id NUMBER(38, 0),
    restaurant VARCHAR(255),
    address TEXT,
    FOREIGN KEY(restaurant_category_id) REFERENCES restaurant_categories(restaurant_category_id)
    );


INSERT INTO
    restaurant_categories (
    restaurant_category_id,
    restaurant_category
    )
    VALUES
    (1, 'Fast-food');

INSERT INTO
    restaurants (
    restaurant_id,
    restaurant_category_id,
    restaurant,
    address
    )
    VALUES
    (1, 1, 'Mcdonalds Luisita', 'Luisita Access Road 2300 Tarlac City Tarlac');


SELECT *
FROM
    restaurants;