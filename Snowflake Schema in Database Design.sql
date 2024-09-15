-- Database Name/Any Database
USE practicedb;


-- Hello! My name is Christiane A. Bacani a Data/DevOps Engineer


-- Warehouse Modeling
-- Snowflake Schema (Extended Version of Star Schema)


-- Drop Tables
DROP TABLE IF EXISTS borrows;
DROP TABLE IF EXISTS members;
DROP TABLE IF EXISTS genders;
DROP TABLE IF EXISTS dates;
DROP TABLE IF EXISTS months;
DROP TABLE IF EXISTS quarters;
DROP TABLE IF EXISTS years;
DROP TABLE IF EXISTS books;
DROP TABLE IF EXISTS authors;
DROP TABLE IF EXISTS publishers;
DROP TABLE IF EXISTS book_shelves;
DROP TABLE IF EXISTS genres;
DROP TABLE IF EXISTS libraries;
DROP TABLE IF EXISTS cities;
DROP TABLE IF EXISTS countries;
DROP TABLE IF EXISTS continents;


-- Normalized Dimension Table for Countries Entity
CREATE TABLE continents(continent_id INT PRIMARY KEY,
						continent TEXT);
                        
                        
-- Normalized Dimension Table for Cities Entity
CREATE TABLE countries(country_id INT PRIMARY KEY,
						country TEXT,
                        continent_id INT,
                        FOREIGN KEY (continent_id) REFERENCES continents (continent_id) 
                        ON DELETE RESTRICT
                        ON UPDATE CASCADE);
                        

-- Normalized Dimension Table for Libraries Entity
CREATE TABLE cities(city_id INT PRIMARY KEY,
					city TEXT,
                    country_id INT,
                    FOREIGN KEY (country_id) REFERENCES countries (country_id) 
                    ON DELETE RESTRICT
                    ON UPDATE CASCADE);
                    

-- Dimension Table for Borrows Fact Entity
CREATE TABLE libraries(library_id INT PRIMARY KEY,
						library TEXT,
                        city_id INT,
                        FOREIGN KEY (city_id) REFERENCES cities (city_id) 
                        ON DELETE SET NULL
                        ON UPDATE CASCADE);
                        

-- Normalized Dimension Table for Books Entity
CREATE TABLE genres(genre_id INT PRIMARY KEY,
					genre TEXT);
                    

-- Normalized Dimension Table for Books Entity
CREATE TABLE book_shelves(shelf_id INT PRIMARY KEY,
							shelf TEXT);
                            

-- Normalized Dimension Table for Books Entity
CREATE TABLE publishers(publisher_id INT PRIMARY KEY,
						publisher TEXT);


-- Normalized Dimension Table for Books Entity
CREATE TABLE authors(author_id INT PRIMARY KEY,
					author TEXT);
                    

-- Dimension Table for Borrows Fact Entity
CREATE TABLE books(book_id INT PRIMARY KEY,
					book TEXT,
                    published_date DATE,
                    author_id INT,
                    FOREIGN KEY (author_id) REFERENCES authors (author_id)
                    ON DELETE NO ACTION
                    ON UPDATE CASCADE,
                    publisher_id INT,
                    FOREIGN KEY (publisher_id) REFERENCES publishers (publisher_id) 
                    ON DELETE NO ACTION
                    ON UPDATE CASCADE,
                    shelf_id INT,
                    FOREIGN KEY (shelf_id) REFERENCES book_shelves (shelf_id) 
                    ON DELETE RESTRICT
                    ON UPDATE CASCADE,
                    genre_id INT,
                    FOREIGN KEY (genre_id) REFERENCES genres (genre_id) 
                    ON DELETE RESTRICT
                    ON UPDATE SET NULL);
                    

-- Normalized Dimension Table for Quarters Entity
CREATE TABLE years(year_id INT PRIMARY KEY,
					year INT);


-- Normalized Dimension Table for Months Entity
CREATE TABLE quarters(quarter_id INT PRIMARY KEY,
						quarter INT,
                        year_id INT,
                        FOREIGN KEY (year_id) REFERENCES years (year_id) 
                        ON DELETE RESTRICT
                        ON UPDATE RESTRICT);
                        
                        
-- Normalized Dimension Table for Dates Entity
CREATE TABLE months(month_id INT PRIMARY KEY,
					month VARCHAR(30),
                    quarter_id INT,
                    FOREIGN KEY (quarter_id) REFERENCES quarters (quarter_id) 
                    ON DELETE RESTRICT
                    ON UPDATE RESTRICT);
                    
                    
-- Dimension Table for Borrows Fact Entity
CREATE TABLE dates(date_id INT PRIMARY KEY,
					date DATE,
					month_id INT,
                    FOREIGN KEY (month_id) REFERENCES months (month_id) 
                    ON DELETE RESTRICT
                    ON UPDATE RESTRICT);


-- Normalized Dimension Table for Members Entity
CREATE TABLE genders(gender_id INT PRIMARY KEY,
					gender TEXT);
                    
                    
-- Dimension Table for Borrows Fact Entity
CREATE TABLE members(member_id INT PRIMARY KEY,
						member TEXT,
                        join_date DATE,
                        member_id INT,
                        FOREIGN KEY (gender_id) REFERENCES genders (gender_id) 
                        ON DELETE RESTRICT
                        ON UPDATE RESTRICT);
                        
                        
-- Borrows Fact Entity
CREATE TABLE borrows(borrow_id SERIAL PRIMARY KEY,
						member_id INT,
                        date_id INT,
                        book_id INT,
                        library_id INT,
                        total_book MEDIUMINT,
                        borrow_end_date DATE,
                        FOREIGN KEY(member_id) REFERENCES members(member_id)
                        ON UPDATE CASCADE
                        ON DELETE SET NULL,
                        FOREIGN KEY(date_id) REFERENCES dates(date_id)
                        ON UPDATE SET NULL
                        ON DELETE RESTRICT,
                        FOREIGN KEY(book_id) REFERENCES books(book_id) 
                        ON UPDATE CASCADE
                        ON DELETE RESTRICT,
                        FOREIGN KEY(library_id) REFERENCES libraries(library_id)
                        ON UPDATE CASCADE
                        ON DELETE RESTRICT); 
                        





