-- Horizontal by Range of Month and Vertical Partitioning of daily_weather_data_from_2024 of Balanga City, Bataan


-- Horizontal partitinong by range of months
CREATE TABLE
	daily_weather_data_from_2024_partitioned (
	date DATE, weather_code INTEGER, temperature_2m_max NUMERIC,
    	temperature_2m_min NUMERIC, temperature_2m_mean NUMERIC, apparent_temperature_max NUMERIC,
    	apparent_temperature_min NUMERIC, apparent_temperature_mean NUMERIC, sunrise_time VARCHAR(50),
    	sunset_time VARCHAR(50), daylight_duration NUMERIC, sunshine_duration NUMERIC, 
    	precipitation_sum NUMERIC, rain_sum NUMERIC, snowfall_sum INTEGER, 
    	precipitation_hours INTEGER, wind_speed_10m_max NUMERIC, wind_gusts_10m_max NUMERIC, 
    	wind_direction_10m_dominant INTEGER, shortwave_radiation_sum NUMERIC, et0_fao_evapotranspiration NUMERIC)
    
PARTITION BY RANGE (MONTH(date)) (
	PARTITION january VALUES LESS THAN (02),
	PARTITION february VALUES LESS THAN (03),
    	PARTITION march VALUES LESS THAN (04),
    	PARTITION april VALUES LESS THAN (05),
    	PARTITION may VALUES LESS THAN (06),
    	PARTITION june VALUES LESS THAN (07),
    	PARTITION july VALUES LESS THAN (08),
    	PARTITION august VALUES LESS THAN (09),
    	PARTITION september VALUES LESS THAN (10),
    	PARTITION october VALUES LESS THAN (11),
    	PARTITION november VALUES LESS THAN (12),
   	PARTITION december VALUES LESS THAN (13)
);

CREATE INDEX date_index
	ON daily_weather_data_from_2024_partitioned (date);

INSERT INTO
	daily_weather_data_from_2024_partitioned (
    	date, weather_code, temperature_2m_max,
    	temperature_2m_min, temperature_2m_mean, apparent_temperature_max,
    	apparent_temperature_min, apparent_temperature_mean, sunrise_time,
    	sunset_time, daylight_duration, sunshine_duration,
    	precipitation_sum, rain_sum, snowfall_sum,
    	precipitation_hours, wind_speed_10m_max, wind_gusts_10m_max,
    	wind_direction_10m_dominant, shortwave_radiation_sum, et0_fao_evapotranspiration)
SELECT *
FROM 
	daily_weather_data_from_2024;



-- Vertical Partitioning
CREATE TABLE 
	regular_metrics AS
    SELECT 
	date, temperature_2m_max, temperature_2m_min,
        temperature_2m_mean, apparent_temperature_max, apparent_temperature_min,
        apparent_temperature_mean, precipitation_sum, precipitation_hours
    FROM
	practice_db.daily_weather_data_from_2024;
	
CREATE TABLE 
	practice_db.advance_metrics AS
    SELECT
	date, wind_speed_10m_max, wind_gusts_10m_max, 
	wind_direction_10m_dominant, shortwave_radiation_sum, et0_fao_evapotranspiration
    FROM  
	daily_weather_data_from_2024;
	
    
    
