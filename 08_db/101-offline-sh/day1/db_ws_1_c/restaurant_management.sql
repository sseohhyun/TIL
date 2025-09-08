USE restaurant_db

-- 'restaurants' 테이블의 이름을 'restaurant_info'로 변경하시오.
ALTER TABLE restaurants
RENAME TO restaurant_info;

-- 'menus' 테이블의 이름을 'menu_items'로 변경하시오.
ALTER TABLE menus
RENAME TO menu_items;

-- 'restaurant_info' 테이블의 'location' 컬럼의 이름을 'address'으로 변경하시오.
ALTER TABLE restaurant_info
RENAME COLUMN location To address;

-- 'menu_items' 테이블에 'available' (BOOLEAN) 컬럼을 추가하고, 기본값을 TRUE로 설정하시오.
ALTER TABLE menu_items
ADD COLUMN available BOOLEAN DEFAULT TRUE;

-- 'menu_items' 테이블을 삭제하시오.
DROP TABLE menu_items;