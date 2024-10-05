CREATE DATABASE IF NOT EXISTS web_ssis;

USE web_ssis;

CREATE TABLE IF NOT EXISTS college (
	code VARCHAR(5) PRIMARY KEY,
	name VARCHAR(100) NOT NULL
);

CREATE TABLE IF NOT EXISTS program (
	code VARCHAR(20) PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    college VARCHAR(5) NOT NULL,
    FOREIGN KEY program(college) REFERENCES college(code) ON DELETE CASCADE
);

CREATE TABLE IF NOT EXISTS student (
	id_number VARCHAR(9) PRIMARY KEY,
    
    last_name VARCHAR(50) NOT NULL,
    first_name VARCHAR(100) NOT NULL,
    middle_name VARCHAR(50),
    
    program VARCHAR(20),
	year_level INT NOT NULL,
    gender VARCHAR(20),
    FOREIGN KEY student(program) REFERENCES program(code) ON DELETE SET NULL
);
