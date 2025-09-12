-- 'john_doe' 지원자의 모든 지원 내역과 지원한 직무의 위치를 조회하시오.
SELECT a.username, j.title, j.location, ap.application_date, ap.status
FROM applications ap
INNER JOIN applicants a
 ON ap.applicant_id = a.id
INNER JOIN jobs j
 ON ap.job_id = j.id
WHERE a.username = "john_doe";

-- 모든 'Accepted' 상태의 지원 내역과 해당 지원자의 이메일, 전화번호를 조회하시오.
SELECT a.username, a.email, a.phone, j.title, ap.application_date
FROM applications ap
INNER JOIN applicants a
 ON ap.applicant_id = a.id
INNER JOIN jobs j
 ON ap.job_id = j.id
WHERE ap.status = "Accepted";

-- 'Software Engineer' 직무에 지원한 지원자 수와 그 직무의 부서명을 조회하시오.
SELECT j.title, j.department, COUNT(*) AS applicant_count
FROM applications ap
INNER JOIN applicants a
 ON ap.applicant_id = a.id
INNER JOIN jobs j
 ON ap.job_id = j.id
WHERE j.title = "Software Engineer"
GROUP BY j.title, j.department;

-- 각 부서별로 'Pending' 상태의 지원 건수를 조회하시오.
SELECT j.department, COUNT(*) AS pending_count
FROM applications ap
INNER JOIN applicants a
 ON ap.applicant_id = a.id
INNER JOIN jobs j
 ON ap.job_id = j.id
WHERE ap.status = "Pending"
GROUP BY j.department; 