/*
	4 Steps of Kimball approach to implementing data models
*/

-- Step 1: Choose a process
-- Voting system

-- Step 2: Identify the grain level of the facts table
-- Transaction per voters (total number of votes per party lists of a voter)

-- Step 3: Identify the dimensions table
-- dim_voters, dim_voter_addresses, dim_voter_baranggays, dim_voter_cities, dim_voter_municipalities,
-- dim_voter_provinces, dim_voter_regions, dim_voter_occupations, dim_voter_occupation_categories,
-- dim_politicians, dim_party_lists, dim_genders, dim_voted_dates, dim_voted_months, dim_voted_years,
-- dim_voted_locations, and dim_election_officers

-- Step 4: Identify the numerics of the facts table
-- total_votes_for_party_lists numeric facts


------------------------------------------------------------------------------------------------


-- Election officers dimension table
CREATE TABLE IF NOT EXISTS
	dim_election_officers (
	election_officer_id INTEGER PRIMARY KEY,
	voter_occupation_id INTEGER, -- Can be used to established relationship to dim_voter_occupations table (many-to-one relationship)
	election_position VARCHAR(255),
	first_name VARCHAR(255),
	middle_name VARCHAR(255),
	last_name VARCHAR(255)
	);


-- Voted locations dimension table
CREATE TABLE IF NOT EXISTS
	dim_voted_locations (
	voted_location_id INTEGER PRIMARY KEY,
	location TEXT
	);


-- Voted dates dimension table
CREATE TABLE IF NOT EXISTS
	dim_voted_dates (
	voted_date_id INTEGER PRIMARY KEY,
	voted_year INTEGER,
	voted_month INTEGER,
	voted_day INTEGER
	);


-- Genders dimension table
CREATE TABLE IF NOT EXISTS
	dim_genders (
	gender CHAR(1) PRIMARY KEY,
	gender_name VARCHAR(10)
	);


-- Party-lists dimension table
CREATE TABLE IF NOT EXISTS
	dim_party_lists (
	party_list_id INTEGER PRIMARY KEY,
	party_list VARCHAR(255),	
	party_list_chairperson VARCHAR(255),
	party_list_vice_chairperson VARCHAR(255),
	party_list_secretary_general VARCHAR(255),
	party_list_treasurer VARCHAR(255),
	party_list_auditor VARCHAR(255),
	party_list_sectoral_heads TEXT,
	party_list_public_relation_officers TEXT,
	party_list_legal_counsels TEXT,
	party_list_nominees TEXT,
	party_list_general_members TEXT
	);


-- Politicians dimension table
CREATE TABLE IF NOT EXISTS
	dim_politicians (
	politician_id INTEGER PRIMARY KEY,
	voter_occupation_id INTEGER, -- Can be used to established relationship to dim_voters_occupation table (one-to-one relationship)
	party_list_id INTEGER, -- Foreign key, referencing dim_party_lists table
	gender CHAR(1), -- Foreign key, referencing dim_genders table
	first_name VARCHAR(255),
	middle_name VARCHAR(255),
	last_name VARCHAR(255),
	birthdate DATE,
	birthplace TEXT,
	CONSTRAINT fk_dim_party_lists FOREIGN KEY(party_list_id) REFERENCES dim_party_lists(party_list_id),
	CONSTRAINT fk_dim_genders FOREIGN KEY(gender) REFERENCES dim_genders(gender)
	);


-- Voter occupation categories dimension table
CREATE TABLE
	dim_voter_occupation_categories (
	voter_occupation_category_id INTEGER PRIMARY KEY,
	voter_occupation_category VARCHAR(255)
	);


-- Voter occupations dimension table
CREATE TABLE IF NOT EXISTS
	dim_voter_occupations (
	voter_occupation_id INTEGER PRIMARY KEY,
	voter_occupation_category_id INTEGER, -- Foreign key, referencing dim_voter_occupation_categories table
	occupation VARCHAR(255),
	CONSTRAINT fk_dim_voter_occupation_categories FOREIGN KEY(voter_occupation_category_id) REFERENCES dim_voter_occupation_categories(voter_occupation_category_id)
	);


-- Voter regions dimension table
CREATE TABLE IF NOT EXISTS
	dim_voter_regions (
	voter_region_id INTEGER PRIMARY KEY,
	region_name VARCHAR(255),
	founded_date DATE,
	regional_directors TEXT,
	assistant_regional_directors TEXT,
	regional_development_council_chairperon VARCHAR(255),
	regional_development_council_co_chairperson VARCHAR(255),
	provincial_governors TEXT,
	city_mayors TEXT,
	municipal_mayors TEXT,
	private_sector_representatives TEXT,
	chief_minister VARCHAR(255),
	deputy_chief_ministers TEXT,
	members_of_the_regional_parliament TEXT,
	regional_ministers TEXT,
	regional_disaser_risk_reduction_and_management_officers TEXT,
	regional_planning_officers TEXT,
	regional_health_officers TEXT,
	regional_tourism_officers TEXT,
	regional_environment_officers TEXT
	);


-- Voter provinces dimension table
CREATE TABLE IF NOT EXISTS
	dim_voter_provinces (
	voter_province_id INTEGER PRIMARY KEY,
	voter_region_id INTEGER, -- Foreign key, referencing dim_voter_regions table
	province_name VARCHAR(255),
	founded_date DATE,
	governor VARCHAR(255),
	vice_governor VARCHAR(255),
	province_board_members TEXT,
	presidents_of_provincial_liga_ng_mga_baranggay TEXT,
	presidents_of_the_sangguniang_kabataan TEXT,
	indigenous_people_representatives TEXT,
	secretaries_to_the_sangguniang_panlalawigan TEXT,
	provincial_treasurers VARCHAR(255),
	provincial_accessors VARCHAR(255),
	provincial_accountants VARCHAR(255),
	provincial_planning_and_development_coordinators TEXT,
	provincial_engineers TEXT,
	provincial_health_officers TEXT,
	provincial_social_welface_officers TEXT,
	provincial_agriculturists TEXT,
	provincial_environment_and_natural_resources_officers TEXT,
	provincial_legal_officers TEXT,
	provincial_disaster_risk_reduction_and_management_officers TEXT,
	provincial_information_officers TEXT,
	provincial_tourism_officers TEXT,
	provincial_veterinarians TEXT,
	CONSTRAINT fk_dim_voter_regions FOREIGN KEY(voter_region_id) REFERENCES dim_voter_regions(voter_region_id)
	);


-- Voter municipalities table
CREATE TABLE IF NOT EXISTS
	dim_voter_municipalities (
	voter_municipality_id INTEGER PRIMARY KEY,
	voter_province_id INTEGER, -- Foreign key, referencing dim_voter_provinces table
	municipality_name VARCHAR(255),
	founded_date DATE,
	municipal_mayor VARCHAR(255),
	municipal_vice_mayor VARCHAR(255),
	municipal_councilors TEXT,
	municipal_secretary_to_sangguninang_bayan VARCHAR(255),
	municipal_treasurers TEXT,
	municipal_accessors TEXT,
	municipal_accountants TEXT,
	municipal_planning_and_development_coordinators TEXT,
	municipal_engineers TEXT,
	municipal_architects TEXT,
	municipal_health_officers TEXT,
	municipal_social_welfare_officers TEXT,
	municipal_agriculturists TEXT,
	municipal_environment_and_natural_resources_officers TEXT,
	CONSTRAINT fk_dim_voter_provinces FOREIGN KEY(voter_province_id) REFERENCES dim_voter_provinces(voter_province_id)
	);


-- Voter cities dimension table
CREATE TABLE IF NOT EXISTS
	dim_voter_cities (
	voter_city_id INTEGER PRIMARY KEY,
	voter_province_id INTEGER, -- Foreign key, referencing dim_voter_provinces table
	city_name VARCHAR(255),
	is_capital BOOLEAN,
	founded_date DATE,
	city_mayor VARCHAR(255),
	city_vice_mayor VARCHAR(255),
	city_councilors TEXT,
	city_administrators TEXT,
	city_treasurers TEXT,
	city_accessors TEXT,
	city_accountants TEXT,
	city_planning_and_development_officers TEXT,
	city_engineers TEXT,
	city_health_officers TEXT,
	city_social_welfare_and_development_officers TEXT,
	city_legal_officers TEXT,
	city_budget_officers TEXT,
	city_environment_and_natural_resources_officers TEXT,
	CONSTRAINT fk_dim_voter_provinces FOREIGN KEY(voter_province_id) REFERENCES dim_voter_provinces(voter_province_id)
	);


-- Voter baranggays dimension table
CREATE TABLE IF NOT EXISTS
	dim_voter_baranggays (
	voter_baranggay_id INTEGER PRIMARY KEY,
	voter_city_id INTEGER, -- Foreign key, referencing dim_voter_cities table
	voter_municipality_id INTEGER, -- Foreign key, referencing dim_voter_municipalities table
	baranggay_name VARCHAR(255),
	founded_date DATE,
	baranggay_captain VARCHAR(255),
	baranggay_councilors TEXT,
	baranggay_sangguniang_kabataan_chairperson VARCHAR(255),
	baranggay_secretary VARCHAR(255),
	baranggay_treasurer VARCHAR(255),
	baranggay_health_workers TEXT,
	baranggay_peace_and_order_officers TEXT,
	baranggay_nutrition_scholars TEXT,
	baranggay_day_care_workers TEXT,
	CONSTRAINT fk_dim_voter_cities FOREIGN KEY(voter_city_id) REFERENCES dim_voter_cities(voter_city_id),
	CONSTRAINT fk_dim_voter_municipalities FOREIGN KEY(voter_municipality_id) REFERENCES dim_voter_municipalities(voter_municipality_id)
	);


-- Voter addresses dimension table
CREATE TABLE IF NOT EXISTS
	dim_voter_addresses (
	voter_address_id INTEGER PRIMARY KEY,
	voter_baranggay_id INTEGER, -- Foreign key, referencing dim_voter_baranggays table
	zipcode INTEGER,
	street_name VARCHAR(255),
	house_number INTEGER,
	CONSTRAINT fk_dim_voter_baranggays FOREIGN KEY(voter_baranggay_id) REFERENCES dim_voter_baranggays(voter_baranggay_id)
	);


-- Voters dimension table
CREATE TABLE IF NOT EXISTS
	dim_voters (
	voter_id INTEGER PRIMARY KEY,
	voter_occupation_id INTEGER, -- Foreign key, referencing dim_voter_occupations table
	gender CHAR(1), -- Foreign key, referencing dim_genders table
	voter_address_id INTEGER, -- Foreign key, referencing dim_voter_addresses table
	full_name VARCHAR(255),
	middle_name VARCHAR(255),
	last_name VARCHAR(255),
	age INTEGER,
	birthdate DATE,
	birthplace TEXT,
	is_current_student BOOLEAN,
	CONSTRAINT fk_dim_voter_occupations FOREIGN KEY(voter_occupation_id) REFERENCES dim_voter_occupations(voter_occupation_id),
	CONSTRAINT fk_dim_genders FOREIGN KEY(gender) REFERENCES dim_genders(gender),
	CONSTRAINT fk_dim_voter_addresses FOREIGN KEY(voter_address_id) REFERENCES dim_voter_addresses(voter_address_id)
);


-- Total number of votes per party lists of a voter
CREATE TABLE IF NOT EXISTS
	fact_total_votes_per_voters (
	voter_id INTEGER, -- Foreign key, referencing dim_voters table
	voted_date_id INTEGER, -- Foreign key, referencing dim_voted_dates table
	voted_location_id INTEGER,-- Foreign key, referencing dim_voted_locations table
	election_officer_id INTEGER, -- Foreign key, referencing dim_election_officers table
	total_votes_for_pdp_laban_party_lists INTEGER,
	total_votes_for_nacionalista_party_lists INTEGER,
	total_votes_for_independent_party_lists INTEGER,
	CONSTRAINT fk_dim_voters FOREIGN KEY(voter_id) REFERENCES dim_voters(voter_id),
	CONSTRAINT fk_dim_voted_dates FOREIGN KEY(voted_date_id) REFERENCES dim_voted_dates(voted_date_id),
	CONSTRAINT fk_dim_voted_locations FOREIGN KEY(voted_location_id) REFERENCES dim_voted_locations(voted_location_id),
	CONSTRAINT fk_dim_election_officers FOREIGN KEY(election_officer_id) REFERENCES dim_election_officers(election_officer_id)
);




