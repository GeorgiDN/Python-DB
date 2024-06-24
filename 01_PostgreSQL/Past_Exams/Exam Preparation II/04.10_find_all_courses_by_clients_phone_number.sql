CREATE OR REPLACE FUNCTION fn_courses_by_client(
    IN phone_num VARCHAR(20),
    OUT number_courses INT
)
AS
$$
BEGIN
    SELECT COUNT(cou.client_id)
    FROM clients AS cl
    JOIN courses AS cou
    ON cl.id = cou.client_id
    WHERE cl.phone_number = phone_num
    INTO number_courses;
END;
$$
LANGUAGE plpgsql;


-- SELECT fn_courses_by_client('(803) 6386812')
-- SELECT fn_courses_by_client('(831) 1391236');
-- SELECT fn_courses_by_client('(704) 2502909');






-- CREATE OR REPLACE FUNCTION fn_courses_by_client(
--     phone_num VARCHAR(20)
-- ) RETURNS INT
-- AS
-- $$
-- BEGIN
--     RETURN
--         (SELECT
--         	COUNT(car_id)
--         FROM
-- 			clients AS cl
-- 		JOIN
-- 			courses AS cou
-- 		ON
-- 			cl.id = cou.client_id
-- 		WHERE
-- 		    cl.phone_number = phone_num
-- 		);
-- END;
-- $$
-- LANGUAGE plpgsql;

-- SELECT fn_courses_by_client('(803) 6386812');
