USE recruitment_db;

-- applicants 테이블의 username 열에 인덱스를 생성하시오.
-- jobs 테이블의 department 열에 인덱스를 생성하시오.
-- applications 테이블의 application_date 열에 인덱스를 생성하시오.
-- applications 테이블의 status 열에 인덱스를 생성하시오.
CREATE INDEX idx_applicants_username
on applicants (username);

ALTER TABLE jobs
ADD INDEX idx_jobs_department (department);

ALTER TABLE applications
ADD INDEX idx_applications_application_date (application_date);

ALTER TABLE applications
ADD INDEX idx_applications_status (status);

-- 아래 조건을 만족하는 SQL을 작성하시오.
-- 특정 지원자(john_doe)가 작성한 모든 지원 내역과 지원한 직무의 위치를 조회
SELECT 
  a.username,
  j.title,
  j.location,
  ap.application_date,
  ap.status
FROM applications ap
INNER JOIN applicants a
  ON a.id = ap.applicant_id
INNER JOIN jobs j
  ON j.id = ap.job_id
WHERE a.username = "john_doe";

-- 각 부서별로 'Pending' 상태의 지원 건수를 조회
SELECT j.department, COUNT(*) AS pending_count
FROM jobs j
INNER JOIN applications ap
 ON ap.job_id = j.id
WHERE ap.status = "Pending"
GROUP BY j.department;


-- 특정 일자 이후의 'Reviewed' 상태 지원 내역과 지원자의 이메일, 전화번호, 지원한 직무의 위치를 조회
SELECT 
  a.username,
  a.email,
  a.phone,
  j.title,
  j.location,
  ap.application_date,
  ap.status
FROM applications ap
INNER JOIN applicants a
  ON a.id = ap.applicant_id
INNER JOIN jobs j
  ON j.id = ap.job_id
WHERE ap.application_date >= "2023-08-02" AND
  ap.status = "Reviewed";

-- 모든 지원자들의 지원 내역과 해당 직무 정보를 포함하는 뷰 생성
CREATE VIEW applicant_job_applications AS
SELECT 
  a.username,
  j.title AS job_title,
  j.department,
  j.location,
  ap.application_date,
  ap.status
FROM applications ap
INNER JOIN applicants a
  ON a.id = ap.applicant_id
INNER JOIN jobs j
  ON j.id = ap.job_id;

-- 특정 지원자가 작성한 모든 지원 내역을 뷰를 통해 조회
SELECT * FROM applicant_job_applications;