/*
	Format Revisioning using PostgreSQL
*/


UPDATE
	magnitudes
SET
	geolocation = REPLACE(geolocation, '.', '');

UPDATE
	magnitudes
SET
	geolocation = REPLACE(geolocation, 'r1', '')
WHERE
	geolocation LIKE '%r1%';

UPDATE
	magnitudes
SET
	geolocation = REPLACE(geolocation, 'r2', '')
WHERE
	geolocation LIKE '%r2%';

UPDATE
	magnitudes
SET
	geolocation = REPLACE(geolocation, '1/', '')
WHERE
	geolocation LIKE '%1/%';

UPDATE
	magnitudes
SET
	geolocation = REPLACE(geolocation, '1/,', '')
WHERE
	geolocation LIKE '%1/,%';

UPDATE
	magnitudes
SET
	geolocation = REPLACE(geolocation, '2/', '')
WHERE
	geolocation LIKE '%2/%';

UPDATE
	magnitudes
SET
	geolocation = REPLACE(geolocation, '2/,', '')
WHERE
	geolocation LIKE '%2/,%';

UPDATE
	magnitudes
SET
	geolocation = REPLACE(geolocation, '3/', '')
WHERE
	geolocation LIKE '%3/%';

UPDATE
	magnitudes
SET
	geolocation = REPLACE(geolocation, '3/,', '')
WHERE
	geolocation LIKE '%3/,%';

UPDATE
	magnitudes
SET
	geolocation = REPLACE(geolocation, '4/', '')
WHERE
	geolocation LIKE '%4/%';

UPDATE
	magnitudes
SET
	geolocation = REPLACE(geolocation, ',   5', '')
WHERE
	geolocation LIKE '%,   5/%';


UPDATE
	magnitudes
SET
	geolocation = REPLACE(geolocation, 'a/', '')
WHERE
	geolocation LIKE '%a/%';

UPDATE
	magnitudes
SET
	geolocation = REPLACE(geolocation, 'a/,', '')
WHERE
	geolocation LIKE '%a/,%';

UPDATE
	magnitudes
SET
	geolocation = REPLACE(geolocation, 'b/', '')
WHERE
	geolocation LIKE '%b/%';


UPDATE
	magnitudes
SET
	geolocation = REPLACE(geolocation, 'b/,', '')
WHERE
	geolocation LIKE '%b/,%';

UPDATE
	magnitudes
SET
	geolocation = REPLACE(geolocation, 'c/', '')
WHERE
	geolocation LIKE '%c/%';


UPDATE
	magnitudes
SET
	geolocation = REPLACE(geolocation, '/', '')
WHERE
	geolocation LIKE '%/%';

UPDATE
	magnitudes
SET
	geolocation = REPLACE(geolocation, ',', '')
WHERE
	geolocation LIKE '%,%';

UPDATE
	magnitudes
SET
	geolocation = TRIM(geolocation);










