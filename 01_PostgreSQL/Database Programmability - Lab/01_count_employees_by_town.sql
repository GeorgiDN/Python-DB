CREATE OR REPLACE FUNCTION fn_count_employees_by_town(
    IN town_name VARCHAR(20),
    OUT count_employees INT
) AS
$$
BEGIN
      SELECT COUNT(e.employee_id)
      INTO count_employees
        FROM towns as t
        JOIN addresses as a
        USING (town_id)
        JOIN employees AS e
        USING (address_id)
        WHERE t.name = town_name;
END;
$$
LANGUAGE plpgsql;

-- SELECT fn_count_employees_by_town('Sofia');




--------------------------------------------------------------------------------------
-- CREATE OR REPLACE FUNCTION fn_count_employees_by_town(
--     IN town_name VARCHAR(20),
--     OUT count_employees INT
-- ) AS
-- $$
-- BEGIN
--       SELECT COUNT(e.employee_id)
--       INTO count_employees
--         FROM towns as t
--         JOIN addresses as a
--         ON t.town_id = a.town_id
--         JOIN employees AS e
--         ON a.address_id = e.address_id
--         WHERE t.name = town_name;
-- END;
-- $$
-- LANGUAGE plpgsql;

-- SELECT fn_count_employees_by_town('Sofia');




-------------------------------------------------------------------------------
-- CREATE OR REPLACE FUNCTION fn_count_employees_by_town(town_name VARCHAR)
-- RETURNS INT
-- AS
-- $$
-- BEGIN
-- 	RETURN (SELECT COUNT(*)
-- 		FROM
-- 			employees
-- 		JOIN 
-- 			addresses USING(address_id)
-- 		JOIN 
-- 			towns USING(town_id)
-- 		WHERE
-- 			towns.name = town_name);
-- 	END
-- $$
-- LANGUAGE plpgsql;

-- SELECT fn_count_employees_by_town('Sofia') AS count;


