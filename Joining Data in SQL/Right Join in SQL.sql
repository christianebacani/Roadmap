-- Use any database 
USE countries;

-- Right Joins in MySQL

-- Create
CREATE TABLE artificial_intelligences(ai_id INT PRIMARY KEY,
										name VARCHAR(50));

CREATE TABLE models(model_id INT PRIMARY KEY,
					model_name VARCHAR(20),
					ai_id INT,
                    start_year YEAR,
                    release_date DATE,
                    FOREIGN KEY (ai_id) REFERENCES artificial_intelligences(ai_id));

-- Insert
INSERT INTO artificial_intelligences(ai_id, name) 
VALUES (1, 'Generative AI'), (2, 'Machine Learning');

INSERT INTO models(model_id,
					model_name,
					ai_id,
                    start_year,
                    release_date)
VALUES (1, 'ChatGPT', 1, '2021', '2022-11-30'), (2, 'Copilot', 1, '2021', '2021-10-30');

-- Query
SELECT 
	ai.ai_id AS ai_id,
    name,
    model_id,
    model_name
FROM models AS m
RIGHT JOIN artificial_intelligences AS ai
	USING(ai_id);
    
-- All of the datas here can be wrong or correct!
                    


    

    
    








                                


