/*
    Data Type Revisioning using PostgreSQL
*/


ALTER TABLE
    magnitudes
ALTER COLUMN
    geolocation
TYPE
    VARCHAR(255);

ALTER TABLE
    magnitudes
ALTER COLUMN
    "Estimate ('000) 2018"
TYPE
    NUMERIC(9, 2)
USING
    "Estimate ('000) 2018"::NUMERIC(9, 2);

ALTER TABLE
    magnitudes
ALTER COLUMN
    "Estimate ('000) 2021"
TYPE
    NUMERIC(9, 2)
USING
    "Estimate ('000) 2021"::NUMERIC(9, 2);

ALTER TABLE
    magnitudes
ALTER COLUMN
    "Estimate ('000) 2023"
TYPE
    NUMERIC(9, 2)
USING
    "Estimate ('000) 2023"::NUMERIC(9, 2);

ALTER TABLE
    magnitudes
ALTER COLUMN
    "Coefficient of Variation 2018"
TYPE
    NUMERIC(9, 2)
USING
    "Coefficient of Variation 2018"::NUMERIC(9, 2);

ALTER TABLE
    magnitudes
ALTER COLUMN
    "Coefficient of Variation 2021"
TYPE
    NUMERIC(9, 2)
USING
    "Coefficient of Variation 2021"::NUMERIC(9, 2);

ALTER TABLE
    magnitudes
ALTER COLUMN
    "Coefficient of Variation 2023"
TYPE
    NUMERIC(9, 2)
USING
    "Coefficient of Variation 2023"::NUMERIC(9, 2);

ALTER TABLE
    magnitudes
ALTER COLUMN
    "Standard Error 2018"
TYPE
    NUMERIC(9, 2)
USING
    "Standard Error 2018"::NUMERIC(9, 2);
	
ALTER TABLE
    magnitudes
ALTER COLUMN
    "Standard Error 2021"
TYPE
    NUMERIC(9, 2)
USING
    "Standard Error 2021"::NUMERIC(9, 2);

ALTER TABLE
    magnitudes
ALTER COLUMN
    "Standard Error 2023"
TYPE
    NUMERIC(9, 2)
USING
    "Standard Error 2023"::NUMERIC(9, 2);

ALTER TABLE
    magnitudes
ALTER COLUMN
    "95% Confidence Interval (Lower Limit) 2018"
TYPE
    NUMERIC(9, 2)
USING
    "95% Confidence Interval (Lower Limit) 2018"::NUMERIC(9, 2);

ALTER TABLE
    magnitudes
ALTER COLUMN
    "95% Confidence Interval (Lower Limit) 2021"
TYPE
    NUMERIC(9, 2)
USING
    "95% Confidence Interval (Lower Limit) 2021"::NUMERIC(9, 2);

ALTER TABLE
    magnitudes
ALTER COLUMN
    "95% Confidence Interval (Lower Limit) 2023"
TYPE
    NUMERIC(9, 2)
USING
    "95% Confidence Interval (Lower Limit) 2023"::NUMERIC(9, 2);

ALTER TABLE
    magnitudes
ALTER COLUMN
    "95% Confidence Interval (Upper Limit) 2018"
TYPE
    NUMERIC(9, 2)
USING
    "95% Confidence Interval (Upper Limit) 2018"::NUMERIC(9, 2);

ALTER TABLE
    magnitudes
ALTER COLUMN
    "95% Confidence Interval (Upper Limit) 2021"
TYPE
    NUMERIC(9, 2)
USING
    "95% Confidence Interval (Upper Limit) 2021"::NUMERIC(9, 2);

ALTER TABLE
    magnitudes
ALTER COLUMN
    "95% Confidence Interval (Upper Limit) 2023"
TYPE
    NUMERIC(9, 2)
USING
    "95% Confidence Interval (Upper Limit) 2023"::NUMERIC(9, 2);
