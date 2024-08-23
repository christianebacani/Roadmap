-- Database Name
USE practicedb;
-- I am a Data Engineer!

-- Creating/Adding a Surrogate Key

-- Drop Table
SET foreign_key_checks = 0;

DROP TABLE IF EXISTS user_interactions;
DROP TABLE IF EXISTS user_sessions;
DROP TABLE IF EXISTS user_registrations;
DROP TABLE IF EXISTS users;
DROP TABLE IF EXISTS contracts;
DROP TABLE IF EXISTS content_creators;
DROP TABLE IF EXISTS sponsors;
DROP TABLE IF EXISTS contents;

SET foreign_key_checks = 1;

-- Create Table
CREATE TABLE contents(content_id INT PRIMARY KEY,
						content_type VARCHAR(50));

CREATE TABLE sponsors(sponsor_id INT PRIMARY KEY,
						sponsor_name VARCHAR(50),
						product_type VARCHAR(50));

CREATE TABLE content_creators(creator_id INT PRIMARY KEY,
								content_id INT,
								username TEXT NOT NULL,
                                location TEXT,
                                FOREIGN KEY(content_id) REFERENCES contents(content_id));

-- Junction Table for Creators and Sponsors
CREATE TABLE contracts(id SERIAL PRIMARY KEY,
						creator_id INT,
                        sponsor_id INT,
                        contract_start DATE,
                        contract_end DATE,
                        FOREIGN KEY(creator_id) REFERENCES content_creators(creator_id),
                        FOREIGN KEY(sponsor_id) REFERENCES sponsors(sponsor_id));

CREATE TABLE user_registrations(gmail VARCHAR(50) UNIQUE NOT NULL,
								username VARCHAR(75) UNIQUE,
                                `password` TEXT,
								firstname TEXT,
                                middlename TEXT,
                                lastname TEXT);

CREATE TABLE users(user_id INT PRIMARY KEY,
					username VARCHAR(75) UNIQUE,
                    location TEXT);

-- Junction Table 
CREATE TABLE user_sessions(user_id INT,
							creator_id INT,
                            session_duration TIME,
                            FOREIGN KEY(user_id) REFERENCES users(user_id),
                            FOREIGN KEY(creator_id) REFERENCES content_creators(creator_id));
                            
-- Junction Table
CREATE TABLE user_interactions(user_id INT,
								creator_id INT,
                                user_like BOOLEAN,
                                user_dislike BOOLEAN,
                                user_subscribe BOOLEAN,
                                user_comment TEXT,
                                user_reply TEXT,
                                FOREIGN KEY(user_id) REFERENCES users(user_id),
                                FOREIGN KEY(creator_id) REFERENCES content_creators(creator_id));

-- Alter Table
ALTER TABLE sponsors
MODIFY COLUMN sponsor_name TEXT;

ALTER TABLE sponsors
MODIFY COLUMN product_type TEXT;

ALTER TABLE user_sessions
ADD COLUMN session_id SERIAL PRIMARY KEY;

ALTER TABLE user_interactions
ADD COLUMN interaction_id SERIAL PRIMARY KEY;

-- Insert Data
INSERT INTO contents(content_id, content_type) 
VALUES (1, 'Technologies');

INSERT INTO sponsors(sponsor_id, sponsor_name, product_type) 
VALUES (1, 'Redragon', 'Gadgets and Technology Equipment');

INSERT INTO content_creators(creator_id, content_id, username, location) 
VALUES (1, 1, 'IBM Technology', 'Wisconsin, USA');

INSERT INTO contracts(creator_id, sponsor_id, contract_start, contract_end) 
VALUES (1, 1, CURDATE(), NULL);

INSERT INTO user_registrations(gmail, username, `password`, firstname, middlename, lastname) 
VALUES ('crjabacani@bpsu.edu.ph', 'crjabacani04', '12-04-2003', 'Christiane', 'Aguibitin', 'Bacani');

INSERT INTO users(user_id, username, location)
VALUES (1, 'crjabacani04', 'Bataan, Philippines');

INSERT INTO user_sessions(user_id, creator_id, session_duration) 
VALUES (1, 1, '00:25:28');

INSERT INTO user_interactions(user_id, creator_id, user_like, user_dislike, user_subscribe, user_comment, user_reply)
VALUES (1, 1, true, false, true, 'Great! Nice Explanation', NULL);

ALTER TABLE user_registrations
ADD COLUMN registration_code VARCHAR(150);

UPDATE user_registrations
SET registration_code = CONCAT(SUBSTR(gmail, 1, 3), '-', SUBSTR(username, 3, 3), '-', password);

ALTER TABLE user_registrations
ADD CONSTRAINT registration_code_pk PRIMARY KEY(registration_code);

-- Query Data
SELECT *
FROM user_registrations;





                        
	



