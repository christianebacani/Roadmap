/*
    Lesson: Snowflake Data Types and Data Type Conversions
*/


// Game Characters Table
CREATE OR REPLACE TABLE
    game_characters (
    game_character_id INTEGER PRIMARY KEY,
    game_character_name VARCHAR(255),
    released_datetime TIMESTAMP_LTZ // 'TIMESTAMP_LTZ' is the exclusive data type of Snowflake for timestamp. Format: 'YYYY-MM-DD HH:MM:SS.fff -timezone'
    );

// Game Character First Skill Informations Table
CREATE OR REPLACE TABLE
    character_first_skill_infos (
    game_character_id INTEGER,
    first_skill_name VARCHAR(255),
    first_skill_description TEXT,
    first_skill_damage NUMBER(8, 3), // 'NUMBER' Data Type is the same as 'NUMERIC' Data type in PostgreSQL
    first_skill_cooldown INTEGER,
    first_skill_mana_cost INTEGER,
    FOREIGN KEY(game_character_id) REFERENCES game_characters(game_character_id)
    );

// Game Character Second Skill Informations Table
CREATE OR REPLACE TABLE
    character_second_skill_infos (
    game_character_id INTEGER,
    second_skill_name VARCHAR(255),
    second_skill_description TEXT,
    second_skill_damage NUMBER(8, 3),
    second_skill_cooldown INTEGER,
    second_skill_mana_cost INTEGER,
    FOREIGN KEY(game_character_id) REFERENCES game_characters(game_character_id)
    );

// Game Character Third Skill Informations Table
CREATE OR REPLACE TABLE
    character_third_skill_infos (
    game_character_id INTEGER,
    third_skill_name VARCHAR(255),
    third_skill_description TEXT,
    third_skill_damage NUMBER(8, 3),
    third_skill_cooldown INTEGER,
    third_skill_mana_cost INTEGER,
    FOREIGN KEY(game_character_id) REFERENCES game_characters(game_character_id)
    );

// Game Character Ultimate Skill Informations Table
CREATE OR REPLACE TABLE
    character_ultimate_skill_infos (
    game_character_id INTEGER,
    ultimate_skill_name VARCHAR(255),
    ultimate_skill_description TEXT,
    ultimate_skill_damage NUMBER(8, 3),
    ultimate_skill_cooldown INTEGER,
    ultimate_skill_mana_cost INTEGER,
    FOREIGN KEY(game_character_id) REFERENCES game_characters(game_character_id)
    );


// Insert data to the tables
INSERT INTO
    game_characters (
    game_character_id,
    game_character_name,
    released_datetime
    )
VALUES (1, 'Vayne', '2011-05-10 21:51:44.444');

INSERT INTO
    character_first_skill_infos (
    game_character_id,
    first_skill_name,
    first_skill_description,
    first_skill_damage,
    first_skill_cooldown,
    first_skill_mana_cost
    )
VALUES (1, 'Tumble', 'Vayne tumbles, maneuvering to carefully place her next shot. Her next attack deals bonus damage.', 77.200, 3, 30);

INSERT INTO
    character_second_skill_infos (
    game_character_id,
    second_skill_name,
    second_skill_description,
    second_skill_damage,
    second_skill_cooldown,
    second_skill_mana_cost
    )
VALUES (1, 'Silver Bolts', 'Vayne tips her bolts with a rare metal, toxic to evil things. The third consecutive attack or ability against the same target deals a percentage of the target\'s max health as bonus true damage.', 108.400, 0, 0);

INSERT INTO
    character_third_skill_infos (
    game_character_id,
    third_skill_name,
    third_skill_description,
    third_skill_damage,
    third_skill_cooldown,
    third_skill_mana_cost
    )
VALUES (1, 'Condemn', 'Vayne draws a heavy crossbow from her back, and fires a huge bolt at her target, knocking them back and dealing damage. If they collide with terrain, they are impaled, dealing bonus damage and stunning them.', 173.000, 16, 90);

INSERT INTO
    character_ultimate_skill_infos (
    game_character_id,
    ultimate_skill_name,
    ultimate_skill_description,
    ultimate_skill_damage,
    ultimate_skill_cooldown,
    ultimate_skill_mana_cost
    )
VALUES (1, 'Final Hour', 'Readying herself for an epic confrontation, Vayne gains increased Attack Damage, Invisibility during Tumble, reduced Tumble cooldown, and more bonus Move Speed from Night Hunter', 231.000, 85, 80);


// CAST() and '::' double-colon for data type conversion
SELECT
    game_character_id,
    CAST(game_character_id AS VARCHAR) AS game_character_id_varchar, // CAST() Function to convert data type from a certain column
    game_character_id::VARCHAR AS game_character_id_varchar, // Using double-colon is the same from CAST() Function
    first_skill_name,
    first_skill_description,
    first_skill_damage,
    first_skill_cooldown,
    first_skill_mana_cost
FROM
    character_first_skill_infos;

// Conversion function
SELECT
    game_character_id,
    TO_VARCHAR(game_character_id) AS game_character_id_varchar, // Using TO_VARCHAR() Function to convert expression to 'VARCHAR' Data Type
    game_character_name,
    released_datetime,
    TO_DATE(released_datetime) AS released_date // Using TO_DATE() Function to convert expression to 'DATE' Data Type
FROM
    game_characters;