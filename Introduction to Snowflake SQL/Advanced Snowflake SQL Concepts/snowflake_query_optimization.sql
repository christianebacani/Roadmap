/*
    Lesson: Snowflake Query Optimizations
*/


// Create Database
CREATE DATABASE IF NOT EXISTS
    social_media_db;

// Use Database
USE DATABASE
    social_media_db;


// Genders Table
CREATE OR REPLACE TABLE
    genders (
    gender_id CHAR(1) PRIMARY KEY,
    gender VARCHAR(10)
    );

// User Registrations Table
CREATE OR REPLACE TABLE
    user_registrations (
    user_id NUMBER(38, 0) AUTOINCREMENT START 1 INCREMENT 1,
    gender_id CHAR(1),
    username VARCHAR(40),
    password VARCHAR(40),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    PRIMARY KEY(user_id),
    FOREIGN KEY(gender_id) REFERENCES genders(gender_id)
    );

// Users Table
CREATE OR REPLACE TABLE
    users (
    user_id NUMBER(38, 0) AUTOINCREMENT START 1 INCREMENT 1,
    gender_id CHAR(1),
    username VARCHAR(40),
    password VARCHAR(40),
    PRIMARY KEY(user_id),
    FOREIGN KEY(gender_id) REFERENCES genders(gender_id)
    );

// Post Owners Table
CREATE OR REPLACE TABLE
    post_owners (
    post_id NUMBER(38, 0) PRIMARY KEY,
    owner_id NUMBER(38, 0),
    FOREIGN KEY(owner_id) REFERENCES users(user_id)
    );


INSERT INTO
    genders (
    gender_id,
    gender
    )
    VALUES 
    ('M', 'Male'),
    ('F', 'Female');

INSERT INTO
    user_registrations (
    gender_id,
    username,
    password
    )
    VALUES
    ('M', 'example_username(1)', 'example_password(1)'),
    ('F', 'example_username(2)', 'example_password(2)');

INSERT INTO
    users (
    gender_id,
    username,
    password
    )
    VALUES
    ('M', 'example_username(1)', 'example_password(1)'),
    ('F', 'example_username(2)', 'example_password(2)');

INSERT INTO
    post_owners (
    post_id,
    owner_id
    )
    VALUES
    (1, 1);

/*
    Common Query Problems
*/


// Not using 'ON' when joining table will yields cartesian product (every record from the first table will match to every record from the second table) which produce bigger results
SELECT *
FROM
    genders
JOIN
    user_registrations;

// Use 'ON' condition when joining TABLE
SELECT *
FROM
    genders AS g
JOIN
    user_registrations AS ur
ON
    g.gender_id = ur.gender_id;


// Using 'UNION' when removing duplicates which will affect query time and consumes more resources
SELECT
    username,
    password
FROM
    user_registrations
WHERE
    gender_id = 'M'
UNION
SELECT
    username,
    password
FROM
    user_registrations
WHERE
    gender_id = 'F';

// Use 'UNION ALL' when you're sure there's no duplicate
SELECT
    username,
    password
FROM
    user_registrations
WHERE
    gender_id = 'M'
UNION ALL
SELECT
    username,
    password
FROM
    user_registrations
WHERE
    gender_id = 'F';


// Using filters and and limits can yield for quicker results
SELECT
    username,
    password
FROM
    users
WHERE
    gender_id = 'F'
LIMIT
    3;


SELECT *
FROM
    post_owners;