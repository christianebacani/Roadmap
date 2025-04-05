/*
	Data Imputation using PostgreSQL
*/


UPDATE
	magnitudes
SET
	"Estimate ('000) 2018" = '0.00'
WHERE
	"Estimate ('000) 2018" = '..';

UPDATE
	magnitudes
SET
	"Estimate ('000) 2021" = '0.00'
WHERE
	"Estimate ('000) 2021" = '..';

UPDATE
	magnitudes
SET
	"Coefficient of Variation 2018" = '0.00'
WHERE
	"Coefficient of Variation 2018" = '..';

UPDATE
	magnitudes
SET
	"Coefficient of Variation 2021" = '0.00'
WHERE
	"Coefficient of Variation 2021" = '..';

UPDATE
	magnitudes
SET
	"Standard Error 2018" = '0.00'
WHERE
	"Standard Error 2018" = '..';

UPDATE
	magnitudes
SET
	"Standard Error 2021" = '0.00'
WHERE
	"Standard Error 2021" = '..';

UPDATE
	magnitudes
SET
	"95% Confidence Interval (Lower Limit) 2018" = '0.00'
WHERE
	"95% Confidence Interval (Lower Limit) 2018" = '..';

UPDATE
	magnitudes
SET
	"95% Confidence Interval (Lower Limit) 2021" = '0.00'
WHERE
	"95% Confidence Interval (Lower Limit) 2021" = '..';

UPDATE
	magnitudes
SET
	"95% Confidence Interval (Upper Limit) 2018" = '0.00'
WHERE
	"95% Confidence Interval (Upper Limit) 2018" = '..';

UPDATE
	magnitudes
SET
	"95% Confidence Interval (Upper Limit) 2021" = '0.00'
WHERE
	"95% Confidence Interval (Upper Limit) 2021" = '..';



	

