CREATE DATABASE hospital_db
  DEFAULT CHARACTER SET = 'utf8mb4';

USE hospital_db;

CREATE TABLE patients(
  patient_id INT PRIMARY KEY AUTO_INCREMENT,
  name VARCHAR(100) NOT NULL,
  birthdate DATE NOT NULL,
  phone_number VARCHAR(20),
  email VARCHAR(50) UNIQUE,
  address VARCHAR(200)
);

ALTER TABLE patientss
ADD COLUMN gender VARCHAR(10),
MODIFY COLUMN phone_number VARCHAR(20)

TRUNCATE TABLE patients;
