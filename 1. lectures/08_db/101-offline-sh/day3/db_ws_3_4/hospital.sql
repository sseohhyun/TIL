CREATE DATABASE hospital;

USE hospital;

CREATE TABLE patient(
  patient_id INT PRIMARY KEY,
  first_name VARCHAR(50),
  last_name VARCHAR(50),
  birth_date DATE,
  phone_number VARCHAR(15)
);

INSERT INTO patient
VALUES
(1, 'John', 'Doe', '1990-01-01', '123-456-7890'),
(2, 'Jane', 'Smith', '1985-02-02', '098-765-4321'),
(3, 'Alice', 'White', '1970-03-15', '111-222-3333');

CREATE TABLE doctor(
  doctor_id INT PRIMARY KEY,
  first_name VARCHAR(50),
  last_name VARCHAR(50),
  specialty VARCHAR(100)
;)

INSERT INTO doctor
VALUES
(1, 'Alice', 'Brown', 'Cardiology'),
(2, 'Bob', 'Johnson', 'Neurology'),
(3, 'Charlie', 'Davis', 'Dermatology');

CREATE TABLE visits(
  visit_id INT PRIMARY KEY,
  patient_id INT,
  Foreign Key (patient_id) REFERENCES patient(patient_id),
  doctor_id INT,
  Foreign Key (doctor_id) REFERENCES doctor(doctor_id),
  visit_date DATE
);

INSERT INTO visits
VALUES
(1, 1, 1, '2024-01-01'),
(2, 2, 2, '2024-02-01'),
(3, 1, 2, '2024-03-01'),
(4, 3, 3, '2024-04-01'),
(5, 1, 2, '2024-05-01'),
(6, 2, 3, '2024-06-01'),
(7, 3, 1, '2024-07-01');

-- 각 환자의 이름, 전화번호, 모든 방문 날짜, 각 방문별 담당 의사의 이름, 그리고 전문 분야를 조회하시오.
SELECT 
  p.first_name, p.last_name, p.phone_number,
  v.visit_date,
  d.first_name AS doctor_first_name, d.last_name AS doctor_last_name, d.specialty
FROM visits v
INNER JOIN patient p
 ON p.patient_id = v.patient_id
INNER JOIN doctor d
 ON d.doctor_id = v.doctor_id
ORDER BY p.patient_id ASC, v.visit_date ASC;

-- 지난 1년 동안(2024년 한 해) 방문한 환자들 중에서 의사별로 방문 횟수를 조회하시오.
SELECT 
  d.first_name, d.last_name, d.specialty, COUNT(*) AS visit_count
FROM doctor d
INNER JOIN visits v
  ON v.doctor_id = d.doctor_id
GROUP BY d.doctor_id;

-- ID가 2인 의사에게 방문한 환자 목록을 조회하되, 방문 횟수가 두 번 이상인 환자만 조회하시오.
SELECT 
  p.first_name, p.last_name, p.phone_number, COUNT(*) AS visit_count
FROM patient p
INNER JOIN visits v
  ON v.patient_id = p.patient_id
WHERE v.doctor_id = 2
GROUP BY v.patient_id
HAVING COUNT(*) >= 2;