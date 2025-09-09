USE restaurant_db;

-- menus 테이블에서 'Salmon Nigiri' 항목을 삭제하시오.
DELETE FROM menus
WHERE item_name = "Salmon Nigiri";
-- SELECT *
-- FROM menus;

-- restaurants 테이블에서 'Pasta Paradise' 레스토랑을 삭제하시오. 
-- (이 레스토랑과 관련된 menus 테이블의 항목도 삭제해야 한다.)

-- 자식테이블부터 삭제하고
DELETE FROM menus
WHERE restaurant_id = (
  SELECT id FROM restaurants WHERE name = "Pasta Paradise"
);

--부모테이블을 삭제해야 함
DELETE FROM restaurants
WHERE name = "Pasta Paradise";
-- SELECT *
-- FROM restaurants;
-- SELECT *
-- FROM menus;

