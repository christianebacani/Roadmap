-- Views, Roles and Privileges, Procedures, and Triggers of daily_weather_data_from_2024 of Balanga Cit, Bataan for OLAP Systems


-- Monthly weather trends view
CREATE VIEW 
    	monthly_weather_trends AS
SELECT
    	MONTH(STR_TO_DATE(date, '%Y-%m-%d')) AS month,
    	ROUND(AVG(temperature_2m_mean), 2) AS average_monthly_temperature,
    	ROUND(AVG(apparent_temperature_mean), 2) AS average_monthly_apparent_temperature,
    	ROUND(AVG(daylight_duration), 2) AS average_monthly_daylight_duration,
    	ROUND(AVG(sunshine_duration), 2) AS average_monthly_sunshine_duration,
    	ROUND(SUM(precipitation_sum), 2) AS total_monthly_precipitation,
    	ROUND(SUM(rain_sum), 2) AS total_monthly_rain,
    	ROUND(AVG(wind_speed_10m_max), 2) AS average_monthly_wind_speed_10m_max
FROM
	daily_weather_data_from_2024
GROUP BY
	MONTH(STR_TO_DATE(date, '%Y-%m-%d'))
ORDER BY 	
	month;


-- Radiation and wind data view
CREATE VIEW
    radiation_and_wind_data AS
SELECT 
    date,
    wind_speed_10m_max,
    wind_gusts_10m_max,
    wind_direction_10m_dominant,
    shortwave_radiation_sum
FROM 
    daily_weather_data_from_2024;
    

-- Create weather_analysts role
CREATE ROLE
	weather_analysts;

-- Grant `SELECT` permission to weather_analysts_role from daily_weather_data_from_2024 table and monthly_weather_trends view
GRANT SELECT
ON
	daily_weather_data_from_2024
TO
	weather_analysts;

GRANT SELECT
ON
	monthly_weather_trends
TO
	weather_analysts;


-- Create climate_researchers
CREATE ROLE 
	climate_researchers;

-- Grant `SELECT` permission to the climate_researchers role to access radiation_and_wind_data view
GRANT SELECT
ON
	radiation_and_wind_data
TO 
	climate_researchers;


-- Procedure to delete duplicate records and insert new records in daily_weather_data_from_2024 data
DELIMITER //
CREATE PROCEDURE insert_new_records (IN weatherDate DATE, IN weatherCode INT, IN temperature2mMax NUMERIC, 
				     IN  temperature2mMin NUMERIC, IN temperature2mMean NUMERIC, IN apparentTemperatureMax NUMERIC,
                                     IN apparentTemperatureMin NUMERIC, IN apparentTemperatureMean NUMERIC, IN sunriseTime VARCHAR(50),
                                     IN sunsetTime VARCHAR(50), IN daylightDuration NUMERIC, IN sunshineDuration NUMERIC,
                                     IN precipitationSum NUMERIC, IN rainSum NUMERIC, IN snowfallSum INTEGER,
                                     IN precipitationHours INTEGER, IN windSpeed10mMax NUMERIC, IN windGusts10mMax NUMERIC,
				     IN windDirection10mDominant INTEGER, IN shorwaveRadiationSum NUMERIC, IN et0FaoEvapotranspiration NUMERIC) 
BEGIN
	DELETE FROM 
		daily_weather_data_from_2024
	WHERE 
		date = weatherDate;
        
    	INSERT INTO
		daily_weather_data_from_2024 (
        	date, weather_code, temperature_2m_max,
        	temperature_2m_min, temperature_2m_mean, apparent_temperature_max,
        	apparent_temperature_min, apparent_temperature_mean, sunrise_time,
        	sunset_time, daylight_duration, sunshine_duration,
        	precipitation_sum, rain_sum, snowfall_sum,
        	precipitation_hours, wind_speed_10m_max, wind_gusts_10m_max,
        	wind_direction_10m_dominant, shortwave_radiation_sum, et0_fao_transpiration)
		VALUES (weatherDate, weatherCode, temperature2mMax,
		temperature2mMin, temperature2mMean, apparentTemperatureMax,
		apparentTemperatureMin, apparentTemperatureMean, sunriseTime,
		sunsetTime, daylightDuration, sunshineDuration,
		precipitationSum, rainSum, snowfallSum,
		precipitationHours, windSpeed10mMax, windGusts10mMax,
		windDirection10mDominant, shortwaveRadiationSum, et0FaoTranspiration);
END //
DELIMITER ;


-- Trigger to automatically calculates and updates the daylight_duration after the sunrise_time or sunset_time is updated
DELIMITER //
CREATE TRIGGER 
	update_daylight_duration 
AFTER UPDATE ON 
	daily_weather_data_from_2024
FOR EACH ROW
BEGIN
	UPDATE
		daily_weather_data_from_2024
	SET
		daylight_duration = CAST(CONCAT(SUBSTR(sunset_time, -5, 2), SUBSTR(sunset_time, -2, 2)) AS UNSIGNED) - CAST(CONCAT(SUBSTR(sunrise_time, -5, 2), SUBSTR(sunrise_time, -2, 2)) AS UNSIGNED);
END //
DELIMITER ;

