/*
    Lesson: Snowflake Query Optimization
*/


-- Create database
CREATE DATABASE IF NOT EXISTS
    library_db;

-- Use database
USE DATABASE
    library_db;


-- Libraries table
CREATE OR REPLACE TABLE
    libraries (
    library_id NUMBER(38, 0) PRIMARY KEY,
    library VARCHAR(255),
    address TEXT
    );

-- Librarians table
CREATE OR REPLACE TABLE
    librarians (
    librarian_id NUMBER(38, 0) PRIMARY KEY,
    librarian VARCHAR(255),
    gender CHAR(1),
    start_date DATE,
    end_date DATE
    );

-- Bookshelves table
CREATE OR REPLACE TABLE
    bookshelves (
    bookshelf_id NUMBER(38, 0) PRIMARY KEY,
    library_id NUMBER(38, 0),
    bookshelf VARCHAR(255),
    FOREIGN KEY(library_id) REFERENCES libraries(library_id)
    );

-- Authors table
CREATE OR REPLACE TABLE
    authors (
    author_id NUMBER(38, 0) PRIMARY KEY,    
    author VARCHAR(255),
    gender CHAR(1)
    );

-- Categories table
CREATE OR REPLACE TABLE
    categories (
    category_id NUMBER(38, 0) PRIMARY KEY,
    category VARCHAR(255)
    );

-- Books table
CREATE OR REPLACE TABLE
    books (
    book_id NUMBER(38, 0) PRIMARY KEY,
    bookshelf_id NUMBER(38, 0),
    author_id NUMBER(38, 0),
    category_id NUMBER(38, 0),
    book VARCHAR(255),
    FOREIGN KEY(bookshelf_id) REFERENCES bookshelves(bookshelf_id),
    FOREIGN KEY(author_id) REFERENCES authors(author_id),
    FOREIGN KEY(category_id) REFERENCES categories(category_id)
    );

-- Borrowers table
CREATE OR REPLACE TABLE
    borrowers (
    borrower_id NUMBER(38, 0) PRIMARY KEY,
    borrowed_book_id NUMBER(38, 0),
    borrower VARCHAR(255),
    gender CHAR(1),
    borrowed_timestamp TIMESTAMP,
    FOREIGN KEY(borrowed_book_id) REFERENCES books(book_id)
    );

-- Returnees table
CREATE OR REPLACE TABLE
    returnees (
    returnee_id NUMBER(38, 0) PRIMARY KEY,
    returned_book_id NUMBER(38, 0),
    returnee VARCHAR(255),
    gender CHAR(1),
    returned_timestamp TIMESTAMP,
    FOREIGN KEY(returned_book_id) REFERENCES books(book_id)
    );


INSERT INTO
    libraries (
    library_id,
    library,
    address
    )
    VALUES
    (1, 'BPSU Library', 'Brgy. Tenejero, Balanga City, Bataan 2100');

INSERT INTO
    librarians (
    librarian_id,
    librarian,
    gender,
    start_date,
    end_date
    )
    VALUES
    (1, 'Chrae Flores-Bacani', 'F', CURRENT_DATE(), NULL);

INSERT INTO
    bookshelves (
    bookshelf_id,
    library_id,
    bookshelf
    )
    VALUES
    (1, 1, 'Computer Science Bookshelf');

INSERT INTO
    authors (
    author_id,
    author,
    gender
    )
    VALUES
    (1, 'Joe Reis', 'M');

INSERT INTO
    categories (
    category_id,
    category
    )
    VALUES
    (1, 'Computer Science');

INSERT INTO
    books (
    book_id,
    bookshelf_id,
    author_id,
    category_id,
    book
    )
    VALUES
    (1, 1, 1, 1, 'Fundamentals of Data Engineering');

INSERT INTO
    borrowers (
    borrower_id,
    borrowed_book_id,
    borrower,
    gender,
    borrowed_timestamp
    )
    VALUES
    (1, 1, 'Nathan Skeen', 'M', '2025-09-20 02:17:44.444');

INSERT INTO
    returnees (
    returnee_id,
    returned_book_id,
    returnee,
    gender,
    returned_timestamp
    )
    VALUES
    (1, 1, 'Nathan Skeen', 'M', '2025-09-20 03:39:44.444');


/*
    Common Query Problems
*/

-- Exploding Joins
SELECT *
FROM
    libraries
INNER JOIN
    bookshelves;

-- Instead, Use 'ON' statement when joining two tables
SELECT *
FROM
    libraries AS l
INNER JOIN
    bookshelves AS b
ON
    l.library_id = b.library_id;


-- Using 'UNION' statement
SELECT
    library_id
FROM
    libraries
UNION
SELECT
    library_id
FROM
    bookshelves;

-- Instead, Use 'UNION ALL' if were're sure that the data does not have any duplicates
SELECT
    library_id
FROM
    libraries
UNION ALL
SELECT
    library_id
FROM
    bookshelves;


/*
    Query Optimizations
*/

-- Using filters and limits to yield quicker and cost-effective results
SELECT
    l.library,
    b.bookshelf
FROM
    libraries  AS l
INNER JOIN
    bookshelves AS b
ON
    l.library_id = b.library_id
WHERE
    l.address LIKE '%Balanga City%'
LIMIT
    5;


-- Specify the column when using 'SELECT' statement and avoid 'SELECT *'
SELECT
    bookshelf_id,
    library_id
FROM
    bookshelves;


-- Use 'WHERE' clause before joining tables for faster processes of fewer rows before joining it
WITH
    balanga_libraries AS (
SELECT
    library_id,
    library
FROM
    libraries
WHERE
    address LIKE '%Balanga City%'
    )

SELECT
    bl.library,
    b.bookshelf
FROM
    balanga_libraries AS bl
INNER JOIN
    bookshelves AS b
ON
    bl.library_id = b.library_id;


-- Examine the query history to analyze what needs to be optimize in your query using 'query_history' view of 'account_usage' schema
WITH
    my_table_queries AS 
(SELECT
    query_text,
    start_time,
    end_time,
    execution_time,
    query_type
FROM
    snowflake.account_usage.query_history
WHERE
    query_text ILIKE '%libraries%' OR
    query_text ILIKE '%bookshelves%')

SELECT *
FROM
    my_table_queries
WHERE
    query_text NOT ILIKE '%INSERT INTO%' AND
    query_text ILIKE '%my_table_queries%'
ORDER BY
    start_time DESC;