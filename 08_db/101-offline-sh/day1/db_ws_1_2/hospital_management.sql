USE hospital_db;

CREATE TABLE hospital(
  hospital_id INT AUTO_INCREMENT PRIMARY KEY,
  name VARCHAR(150) NOT NULL,
  location VARCHAR(200) NOT NULL,
  established_date DATE,
  contact_number VARCHAR(20) UNIQUE,
  type VARCHAR(50) NOT NULL
)


ALTER TABLE hospital
ADD COLUMN capacity INT,
MODIFY COLUMN type VARCHAR(100),
RENAME COLUMN established_date TO founded_date;

DROP TABLE hospital;
DROP TABLE patients;