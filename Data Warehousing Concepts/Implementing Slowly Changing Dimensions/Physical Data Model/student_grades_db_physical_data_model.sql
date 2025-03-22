/*
	Implementing SCDs (Slowly Changing Dimensions)
	with Snowflake Schema for student_grades database
*/

-- Type 0: Prevents update to the value from the dimension table
-- Type 1: Overwrites the existing value from the row of dimension table
-- Type 2: Add new row with updated values. Leaving the previous value from the previous row of the dimension table
-- Type 3: Adding the previous value to a column
-- Type 4: Stores the entire history snapshot from a separate dimension table

----------------------------------------------------------------------------------------------


-- Grade remarks dimension table (SCD Type 3)
CREATE TABLE
	dim_grade_remarks (
	remark_id INTEGER PRIMARY KEY,
	remark VARCHAR(20),
	previous_remark VARCHAR(20)
	);


-- Professors dimension table (SCD Type 2)
CREATE TABLE
	dim_professors (
	professor_id INTEGER PRIMARY KEY,
	professor VARCHAR(255),
	graduated_at VARCHAR(255), -- University that they graduated
	graduated_year INTEGER,
	degree VARCHAR(255)
	);


-- Instructors dimension table (SCD Type 1)
CREATE TABLE
	dim_instructors (
	instructor_id INTEGER PRIMARY KEY,
	instructor VARCHAR(255),
	graduated_at VARCHAR(255), -- University that they graduated
	graduated_year INTEGER,
	degree VARCHAR(255)
	);


-- Subjects dimension table (SCD Type 2)
CREATE TABLE
	dim_subjects (
	subject_id INTEGER PRIMARY KEY,
	subject VARCHAR(255)
	);


-- Departments dimension table (SCD Type 3)
CREATE TABLE
	dim_departments(
	department_id INTEGER PRIMARY KEY,
	department VARCHAR(255),
	previous_department VARCHAR(255)
	);


-- Courses dimension table (SCD Type 3)
CREATE TABLE
	dim_courses (
	course_id INTEGER PRIMARY KEY,
	department_id INTEGER, -- Foreign key, referencing dim_departments table
	course VARCHAR(255),
	previous_course VARCHAR(255),
	CONSTRAINT fk_dim_departments FOREIGN KEY(department_id) REFERENCES dim_departments(department_id)
	);


-- Universities dimension table (SCD Type 3)
CREATE TABLE
	dim_universities (
	university_id INTEGER PRIMARY KEY,
	university VARCHAR(255),
	president VARCHAR(255),
	previous_president VARCHAR(255),
	founded_date DATE
	);


-- Campuses dimension table (SCD Type 3)
CREATE TABLE
	dim_campuses (
	campus_id INTEGER PRIMARY KEY,
	university_id INTEGER, -- Foreign key, referencing dim_universities table
	campus VARCHAR(255),
	director VARCHAR(255),
	previous_director VARCHAR(255),
	location TEXT,
	founded_date DATE,
	CONSTRAINT fk_dim_universities FOREIGN KEY(university_id) REFERENCES dim_universities(university_id)
	);


-- Semesters dimension table (SCD Type 1)
CREATE TABLE
	dim_semesters (
	semester_id INTEGER PRIMARY KEY,
	semester VARCHAR(50)
	);


-- Academic school years dimension table (SCD Type 2)
CREATE TABLE
	dim_academic_school_years (
	academic_school_year_id INTEGER PRIMARY KEY,
	academic_school_year VARCHAR(50)
	);


-- College years dimension table (SCD Type 1)
CREATE TABLE
	dim_college_years (
	college_year_id INTEGER PRIMARY KEY,
	college_year VARCHAR(30)
	);
	

-- Provinces dimension table (SCD Type 3)
CREATE TABLE
	dim_provinces (
	province_id INTEGER PRIMARY KEY,
	province VARCHAR(255),
	governor VARCHAR(255),	
	previous_governor VARCHAR(255),
	founded_date DATE
	);


-- Cities dimension table (SCD Type 3)
CREATE TABLE
	dim_cities (
	city_id INTEGER PRIMARY KEY,
	province_id INTEGER, -- Foreign key, referencing dim_provinces table
	city VARCHAR(255),
	mayor VARCHAR(255),
	previous_mayor VARCHAR(255),
	zipcode INTEGER,
	founded_date DATE,
	CONSTRAINT fk_dim_provinces FOREIGN KEY(province_id) REFERENCES dim_provinces(province_id)
	);


-- Municipalities dimension table (SCD Type 3)
CREATE TABLE
	dim_municipalities (
	municipality_id INTEGER PRIMARY KEY,
	province_id INTEGER, -- Foreign key, referencing dim_municipalies table
	municipality VARCHAR(255),
	mayor VARCHAR(255),
	previous_mayor VARCHAR(255),
	zipcode INTEGER,
	founded_date DATE,
	CONSTRAINT fk_dim_provinces FOREIGN KEY(province_id) REFERENCES dim_provinces(province_id)
	);


-- Baranggays dimension table (SCD Type 3)
CREATE TABLE
	dim_baranggays (
	baranggay_id INTEGER PRIMARY KEY,
	city_id INTEGER, -- Foreign key, referencing dim_cities table
	municipality_id INTEGER, -- Foreign key, referencing dim_municipalities tabl
	baranggay VARCHAR(255),
	captain VARCHAR(255),
	previous_captain VARCHAR(255),
	founded_date DATE,
	CONSTRAINT fk_dim_cities FOREIGN KEY(city_id) REFERENCES dim_cities(city_id),
	CONSTRAINT fk_dim_municipalities FOREIGN KEY(municipality_id) REFERENCES dim_municipalities(municipality_id)
	);


-- Student addresses dimension table (SCD Type 1)
CREATE TABLE
	dim_student_addresses (
	student_address_id INTEGER PRIMARY KEY,
	baranggay_id INTEGER, -- Foreign key, referencing dim_baranggays table
	street_name VARCHAR(255),
	house_number INTEGER,
	CONSTRAINT fk_dim_baranggays FOREIGN KEY(baranggay_id) REFERENCES dim_baranggays(baranggay_id)
	);



-- Student genders dimension table (SCD Type 1)
CREATE TABLE
	dim_student_genders (
	gender CHAR(1) PRIMARY KEY,
	gender_name VARCHAR(10)
	);


-- Occupation categories dimension table (SCD Type 1)
CREATE TABLE
	dim_occupation_categories (
	occupation_category_id INTEGER PRIMARY KEY,
	occupation_category VARCHAR(255)
	);


-- Occupations dimension table (SCD Type 3)
CREATE TABLE
	dim_occupations (
	occupation_id INTEGER PRIMARY KEY,
	occupation_category_id INTEGER, -- Foreign key, referencing dim_occupation_categories table
	occupation VARCHAR(255),
	previous_occupation VARCHAR(255),
	CONSTRAINT fk_dim_occupation_categories FOREIGN KEY(occupation_category_id) REFERENCES dim_occupation_categories(occupation_category_id)
	);


-- Student guardians dimension table (SCD Type 1)
CREATE TABLE
	dim_student_guardians (
	student_guardian_id INTEGER PRIMARY KEY,
	occupation_id INTEGER, -- Foreign key, referencing dim_occupations table
	relationship_to_student VARCHAR(255),
	first_name VARCHAR(255),
	middle_name VARCHAR(255),
	last_name VARCHAR(255),
	contact_number INTEGER,
	address TEXT,
	CONSTRAINT fk_dim_occupations FOREIGN KEY(occupation_id) REFERENCES dim_occupations(occupation_id)
	);


-- Enum type for dim_students table
CREATE TYPE
	status AS ENUM('Currently Enrolled', 'Semestral Break', 'Vacation', 'Withdrawal', 'Discontinued');

-- Students dimension table (SCD Type 1)
CREATE TABLE
	dim_students (
	student_id INTEGER PRIMARY KEY,
	student_guardian_id INTEGER, -- Foreign key, referencing dim_student_guardians table
	first_name VARCHAR(255),
	middle_name VARCHAR(255),
	last_name VARCHAR(255),
	is_transfereee BOOLEAN,
	academic_status status,
	is_working_student BOOLEAN,
	graduation_date DATE,
	CONSTRAINT fk_dim_student_guardians FOREIGN KEY(student_guardian_id) REFERENCES dim_student_guardians(student_guardian_id)
	);


-- Student semestral grades fact table
CREATE TABLE
	fact_student_semestral_grades (
	student_id INTEGER, -- Foreign key, referencing dim_students table
	gender CHAR(1), -- Foreign key, referencing dim_student_genders table
	student_address_id INTEGER, -- Foreing key, referencing dim_student_addresses table
	college_year_id INTEGER, -- Foreign key, referencing dim_college_years table
	academic_school_year_id INTEGER, -- Foreign key, referencing dim_academic_school_years table
	semester_id INTEGER, -- Foreign key, referencing dim_semesters table
	campus_id INTEGER, -- Foreign key, referencing dim_campuses table
	course_id INTEGER, -- Foreign key, referencing dim_courses table
	subject_id INTEGER, -- Foreign key, referencing dim_subjects table
	instructor_id INTEGER, -- Foreign key, referencing dim_instructors table
	professor_id INTEGER, -- Foreign key, referencing dim_professors table
	remark_id INTEGER, -- Foreign key, referencing dim_grade_remarks table
	semester_grade NUMERIC,
	subject_total_units NUMERIC,
	CONSTRAINT fk_dim_students FOREIGN KEY(student_id) REFERENCES dim_students(student_id),
	CONSTRAINT fk_dim_student_genders FOREIGN KEY(gender) REFERENCES dim_student_genders(gender),
	CONSTRAINT fk_dim_student_addresses FOREIGN KEY(student_address_id) REFERENCES dim_student_addresses(student_address_id),
	CONSTRAINT fk_dim_college_years FOREIGN KEY(college_year_id) REFERENCES dim_college_years(college_year_id),
	CONSTRAINT fk_dim_academic_school_years FOREIGN KEY(academic_school_year_id) REFERENCES dim_academic_school_years(academic_school_year_id),
	CONSTRAINT fk_dim_semesters FOREIGN KEY(semester_id) REFERENCES dim_semesters(semester_id),
	CONSTRAINT fk_dim_campuses FOREIGN KEY(campus_id) REFERENCES dim_campuses(campus_id),
	CONSTRAINT fk_dim_courses FOREIGN KEY(course_id) REFERENCES dim_courses(course_id),
	CONSTRAINT fk_dim_subjects FOREIGN KEY(subject_id) REFERENCES dim_subjects(subject_id),
	CONSTRAINT fk_dim_instructors FOREIGN KEY(instructor_id) REFERENCES dim_instructors(instructor_id),
	CONSTRAINT fk_dim_professors FOREIGN KEY(professor_id) REFERENCES dim_professors(professor_id),
	CONSTRAINT fk_dim_grade_remarks FOREIGN KEY(remark_id) REFERENCES dim_grade_remarks(remark_id)
	);


	