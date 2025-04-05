/*
	Field Name Revisioning using PostgreSQL
*/


ALTER TABLE
	magnitudes
RENAME COLUMN
	"Estimate ('000) 2018" TO
	estimate_num_of_poor_fam_2018;

ALTER TABLE
	magnitudes
RENAME COLUMN
	"Estimate ('000) 2021" TO
	estimate_num_of_poor_fam_2021;

ALTER TABLE
	magnitudes
RENAME COLUMN
	"Estimate ('000) 2023" TO
	estimate_num_of_poor_fam_2023;

ALTER TABLE
	magnitudes
RENAME COLUMN
	"Coefficient of Variation 2018" TO
	coefficient_of_variation_2018;

ALTER TABLE
	magnitudes
RENAME COLUMN
	"Coefficient of Variation 2021" TO
	coefficient_of_variation_2021;

ALTER TABLE
	magnitudes
RENAME COLUMN
	"Coefficient of Variation 2023" TO
	coefficient_of_variation_2023;

ALTER TABLE
	magnitudes
RENAME COLUMN
	"Standard Error 2018" TO
	standard_error_2018;

ALTER TABLE
	magnitudes
RENAME COLUMN
	"Standard Error 2021" TO
	standard_error_2021;

ALTER TABLE
	magnitudes
RENAME COLUMN
	"Standard Error 2023" TO
	standard_error_2023;

ALTER TABLE
	magnitudes
RENAME COLUMN
	"95% Confidence Interval (Lower Limit) 2018" TO
	confidence_interval_of_95_pct_lower_limit_at_2018;

ALTER TABLE
	magnitudes
RENAME COLUMN
	"95% Confidence Interval (Lower Limit) 2021" TO
	confidence_interval_of_95_pct_lower_limit_at_2021;

ALTER TABLE
	magnitudes
RENAME COLUMN
	"95% Confidence Interval (Lower Limit) 2023" TO
	confidence_interval_of_95_pct_lower_limit_at_2023;

ALTER TABLE
	magnitudes
RENAME COLUMN
	"95% Confidence Interval (Upper Limit) 2018" TO
	confidence_interval_of_95_pct_upper_limit_at_2018;

ALTER TABLE
	magnitudes
RENAME COLUMN
	"95% Confidence Interval (Upper Limit) 2021" TO
	confidence_interval_of_95_pct_upper_limit_at_2021;

ALTER TABLE
	magnitudes
RENAME COLUMN
	"95% Confidence Interval (Upper Limit) 2023" TO
	confidence_interval_of_95_pct_upper_limit_at_2023;