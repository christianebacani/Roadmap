-- Database Name/Any Database
USE practicedb;


-- Hello! My name is Christiane A. Bacani a Data/DevOps Engineer


-- Warehouse Modeling
-- Star Schema


-- Drop Tables
DROP TABLE IF EXISTS borrows;
DROP TABLE IF EXISTS members;
DROP TABLE IF EXISTS dates;
DROP TABLE IF EXISTS book_shelves;
DROP TABLE IF EXISTS libraries;


-- Dimension Table for Fact Entity
CREATE TABLE libraries(library_id INT PRIMARY KEY,
			library TEXT);


-- Dimension Table for Fact Entity
CREATE TABLE book_shelves(shelf_id INT PRIMARY KEY,
			    shelf TEXT,
                            book_id INT,
                            book TEXT);


-- Dimension Table for Fact Entity                    
CREATE TABLE dates(date_id INT PRIMARY KEY,
		    month INT,
                    day MEDIUMINT, 
                    year MEDIUMINT);


-- Dimension Table for Fact Entity
CREATE TABLE members(member_id INT PRIMARY KEY,
		     member TEXT);

                        
-- Borrows Fact Entity
CREATE TABLE borrows(member_id INT,
                        date_id INT,
                        shelf_id INT,
                        library_id INT,
                        total_book MEDIUMINT,
                        borrow_end_date DATE,
                        FOREIGN KEY(member_id) REFERENCES members(member_id)
                        ON UPDATE CASCADE
                        ON DELETE SET NULL,
                        FOREIGN KEY(date_id) REFERENCES dates(date_id)
                        ON UPDATE SET NULL
                        ON DELETE RESTRICT,
                        FOREIGN KEY(shelf_id) REFERENCES book_shelves(shelf_id) 
                        ON UPDATE CASCADE
                        ON DELETE RESTRICT,
                        FOREIGN KEY(library_id) REFERENCES libraries(library_id)
                        ON UPDATE CASCADE
                        ON DELETE RESTRICT); 
                        

                        
	
		

