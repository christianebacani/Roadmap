-- Database Name
USE practicedb;

-- Simple Data Migration

-- Drop Tables
DROP TABLE IF EXISTS job_postings;
DROP TABLE IF EXISTS data_engineer_jobs;

-- Original Table Source
CREATE TABLE job_postings(job_title VARCHAR(100),
							location TEXT,
                            link TEXT,
							year_exp INT,
                            position_level VARCHAR(100),
                            salary DECIMAL(11, 2));

-- Target Table Source
CREATE TABLE data_engineer_jobs(job_title VARCHAR(100), 
								location TEXT, 
                                year_exp INT, 
                                position_level VARCHAR(100), 
                                salary DECIMAL(11, 2));

-- Insert Manual Data from Indeed Website                                
INSERT INTO job_postings(job_title, location, link, year_exp, position_level, salary) 
VALUES ('Data Engineer', 'Philippines', 'https://ph.indeed.com/jobs?q=data+engineer&l=&vjk=8fb7675c6c863aeb&advn=4859358672523588', 3, 'Mid', 78000),
('Senior Data Engineer', 'Philippines', 'https://ph.indeed.com/jobs?q=data+engineer&l=&vjk=8fb7675c6c863aeb&advn=4859358672523588', 5, 'Senior', NULL),
('Senior/Data Engineer', 'Philippines', 'https://ph.indeed.com/jobs?q=data+engineer&l=&vjk=8fb7675c6c863aeb&advn=4859358672523588',  3, 'Senior', 60000);

-- Migrate
INSERT INTO data_engineer_jobs
	SELECT
		job_title,
        location,
        year_exp,
        position_level,
        salary
	FROM job_postings
    WHERE job_title LIKE '%Data Engineer%';

-- Query
SELECT *
FROM data_engineer_jobs;



