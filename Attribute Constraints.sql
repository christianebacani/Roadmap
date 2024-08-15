-- Database Name
USE practicedb;

-- Serial Data Type, Binary Data Tye, and Cast/Convert Function for Attribute Constraints

-- Drop Table
DROP TABLE IF EXISTS employee_attendances;


-- Table Creation
CREATE TABLE employee_attendances(record_id SERIAL,
									employee_id INT,
									serial_number INT(9),
									employee_name VARCHAR(50), 
                                    `weekday` ENUM('Mon', 'Tue', 'Wed', 'Thu', 'Fri'),
                                    time_in TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                                    break_time TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                                    time_out TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                                    PRIMARY KEY (record_id, employee_id));
		

-- Attribute Inserting
INSERT INTO employee_attendances(record_id, employee_id, serial_number, employee_name, `weekday`) 
VALUES (1, 1, 13, 'Bacani, Christiane', 5), (2, 1, 13, 'Bacani, Christiane', 1), (3, 2, 14, 'Flores, Rica Mae', 1), (4, 1, 13, 'Bacani, Christiane', 2);


-- Querying using Convert/Cast to convert int to binary
SELECT
	record_id,
	employee_id,
    serial_number,
    CONVERT(serial_number, BINARY) AS serial_code,
    employee_name,
    `weekday`,
    time_in,
    break_time,
    time_out
FROM employee_attendances;



