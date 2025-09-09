USE restaurant_db;

-- restaurants 테이블에서 모든 레스토랑의 이름과 위치를 조회하시오.
SELECT name, location
FROM restaurants;

-- menus 테이블에서 가격이 6.00 이상인 모든 항목을 조회하시오.
SELECT item_name, price
FROM menus
WHERE price >= 6;