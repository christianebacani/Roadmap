USE kaggle_db;
    
    
-- Build Materilized Views in MySQL (Improvised)


DROP VIEW IF EXISTS 
	average_country_gdp_growth_per_year;
DROP TABLE IF EXISTS
	materialized_avg_country_gdp_growth_per_year;

DROP VIEW IF EXISTS 
	non_materialized_total_growth_rate_pop_pct;
DROP TABLE IF EXISTS 
	materialized_view_total_growth_rate_pop_pct;
    

-- Creating non-materialized views
CREATE VIEW
	average_country_gdp_growth_per_year AS
SELECT 
	`Country`,
	ROUND(AVG(`GDP growth (annual %)`), 2) AS `Average GDP growth per year`
FROM 
	south_asian_dataset
GROUP BY 
	`Country`
ORDER BY 
	`Average GDP growth per year` DESC;


-- Creating materialized views
-- NOTE : MySQL doesn't support materialized views so I just improvised
CREATE TABLE materialized_avg_country_gdp_growth_per_year (`Country` TEXT,
							   `Average GDP growth per year` FLOAT);


-- Storing query results into materialized view
INSERT INTO 
	materialized_avg_country_gdp_growth_per_year
SELECT *
FROM 
	average_country_gdp_growth_per_year;
	
    
-- Creating non-materialize view (-- Total growth rate of population per country of all years)
CREATE VIEW
	non_materialized_total_growth_rate_pop_pct AS
	WITH 
		country_cte AS (
	SELECT
		`Country`,
		`Year`, 
    `Population, total`,
    ROW_NUMBER() OVER (PARTITION BY `Country`
			ORDER BY Year DESC) AS year_sorted
	FROM 
		south_asian_dataset)

	SELECT
		DISTINCT `Country`,
		ROUND(((SELECT 
		`Population, total`
	FROM 
		country_cte AS cc1
	WHERE
		cc1.`Country` = country_cte.`Country` AND
        cc1.year_sorted = (SELECT MIN(year_sorted) FROM country_cte AS inner_country_cte WHERE inner_country_cte.`Country` = cc1.`Country`)
	) /
    (SELECT 
		`Population, total`
	FROM 
		country_cte AS cc2
	WHERE 
		cc2.`Country` = country_cte.`Country` AND
        cc2.year_sorted = (SELECT MAX(year_sorted) FROM country_cte AS inner_country_cte WHERE inner_country_cte.`Country` = cc2.`Country`)
	) - 1), 2) AS `Total Growth Rate Percentage`
	FROM 
		country_cte
	ORDER BY 
		`Total Growth Rate Percentage` DESC;

    
-- Creating materialized view
CREATE TABLE
		materialized_view_total_growth_rate_pop_pct (`Country` TEXT, `Total Growth Rate Percentage` FLOAT);


-- Storing query results
INSERT INTO 
	materialized_view_total_growth_rate_pop_pct
SELECT *
FROM 
	non_materialized_total_growth_rate_pop_pct;
    


-- Querying materialized view (Average Country GDP Growth Per Year)
SELECT *
FROM 
	materialized_avg_country_gdp_growth_per_year;

-- Querying materialized view (Total Growth Rate of Population per country of all years)
SELECT *
FROM 
	materialized_view_total_growth_rate_pop_pct;
    
    
    
    

    

    
    



    
    
    
    
    


    
    


		
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    


    
    
    
    
    


    
    
    
    
    
    
    
    



    
    
    

    


    
    
    

















    
    
    
    
    
    
    
    
    
    

    
    
    
    


    
    
    
    
