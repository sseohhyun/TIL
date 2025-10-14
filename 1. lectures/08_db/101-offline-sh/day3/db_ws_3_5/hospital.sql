USE hospital;

-- 이전 단계 문제에서 사용한 테이블과 데이터를 그대로 사용하시오.
-- 의사 테이블에서 'Neurology', 'Dermatology' 진료 과목(specialty)을 가진 의사의 목록을 조회하되, 
-- 각 의사가 진료한 환자 수가 2 이상인 경우에 해당하는 의사만 조회하시오. 이 때 Multi-column Subquery를 사용하여 작성하시오.
SELECT first_name, last_name, specialty
FROM doctor
WHERE specialty in ("Neurology", "Dermatology") AND
  doctor_id in (
    SELECT doctor_id
    FROM visits
    GROUP BY doctor_id
    HAVING COUNT(*) >= 2);


-- 각 환자의 이름, 전화번호, 모든 방문 날짜, 각 방문별 담당 의사의 이름, 그리고 전문 분야를 포함하는 View를 생성하시오.
CREATE VIEW patient_visit_details AS
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

-- 특정 의사에게 방문한 환자 목록을 조회하는 View를 생성하시오.
CREATE VIEW doctor_patient_list AS
SELECT
  d.first_name AS doctor_first_name, d.last_name AS doctor_last_name,
  p.first_name AS patient_first_name, p.last_name AS patient_last_name, p.phone_number
FROM visits v
INNER JOIN patient p
 ON p.patient_id = v.patient_id
INNER JOIN doctor d
 ON d.doctor_id = v.doctor_id
ORDER BY d.doctor_id ASC, p.patient_id ASC;


-- 생성한 View를 사용하여 각 환자의 이름, 전화번호, 모든 방문 날짜, 각 방문별 담당 의사의 이름, 그리고 전문 분야를 조회하시오.
SELECT * FROM patient_visit_details;

-- 생성한 View를 사용하여 Brown 의사에게 방문한 환자 목록을 조회하시오.
SELECT * FROM doctor_patient_list
WHERE doctor_last_name = "Brown";