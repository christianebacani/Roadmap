/*
    Lesson: Snowflake Query Optimization
*/


CREATE DATABASE IF NOT EXISTS
    coffee_shop_db;

USE DATABASE
    coffee_shop_db;


--------------------------------------------------------------------------------------- Table Creation --------------------------------------------------------------------------------

// Coffee Shops Table
CREATE OR REPLACE TABLE
    coffee_shops (
    coffee_shop_id NUMBER(38, 0) PRIMARY KEY,
    coffee_shop VARCHAR(255),
    address TEXT
    );

// Branches Table
CREATE OR REPLACE TABLE
    branches (
    branch_id NUMBER(38, 0) PRIMARY KEY,
    coffee_shop_id NUMBER(38, 0),
    branch VARCHAR(255),
    address TEXT
    );

// Positions Table
CREATE OR REPLACE TABLE
    positions (
    position_id NUMBER(38, 0) PRIMARY KEY,
    position VARCHAR(255)
    );

// Employees Table
CREATE OR REPLACE TABLE
    employees (
    employee_id NUMBER(38, 0) PRIMARY KEY,
    position_id NUMBER(38, 0),
    employee VARCHAR(255),
    gender CHAR(1),
    FOREIGN KEY(position_id) REFERENCES positions(position_id)
    );

--------------------------------------------------------------------------------------- Data Insertionn -------------------------------------------------------------------------------

INSERT INTO
    coffee_shops (
    coffee_shop_id,
    coffee_shop,
    address
    )
    VALUES
    (1, 'Big Brew', '30 Romulo Boulevard, Terazza Building (in front of TSU Tarlac State University) 2300 Tarlac Central Luzon');

INSERT INTO
    branches (
    branch_id,
    coffee_shop_id,
    branch,
    address
    )
    VALUES
    (1, 1, 'Big Brew - San Isidro', 'San Isidro 2300 Tarlac Central Luzon ');

INSERT INTO
    positions (
    position_id,
    position
    )
    VALUES
    (1, 'Manager'),
    (2, 'Cashier'),
    (3, 'Brewer'),
    (4, 'Delivery Rider');

INSERT INTO
    employees(
    employee_id,
    position_id,
    employee,
    gender
    )
    VALUES
    (1, 2, 'Gavjvorzki Mae Flores', 'F');

--------------------------------------------------------------------------------------- Queries ---------------------------------------------------------------------------------------

// Avoid this type of joins (Exploding Joins) because it will result to cartesian result were every row will match to every rows of another table
SELECT *
FROM
    coffee_shops
JOIN
    branches;

// Use 'ON' condition as much as possible to avoid this mistakes
SELECT
    cs.coffee_shop,
    b.branch
FROM
    coffee_shops AS cs
JOIN
    branches AS b
ON
    cs.coffee_shop_id = b.coffee_shop_id;


// Avoid using 'UNION' if the tables does not have any duplicates
SELECT
    employee
FROM
    employees
WHERE
    gender = 'M'
UNION
SELECT
    employee
FROM
    employees
WHERE
    gender = 'F';

// Use 'UNION ALL' if you're sure there's no duplicate
SELECT
    employee
FROM
    employees
WHERE
    gender = 'M'
UNION ALL
SELECT
    employee
FROM
    employees
WHERE
    gender = 'F';