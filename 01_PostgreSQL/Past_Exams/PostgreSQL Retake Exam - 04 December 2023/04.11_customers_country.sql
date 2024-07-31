CREATE PROCEDURE sp_customer_country_name(
    IN customer_full_name VARCHAR (50),
    OUT country_name VARCHAR (50)
) AS
$$
BEGIN
    SELECT
        cou.name
    INTO
        country_name
    FROM
        countries AS cou
    JOIN
        customers AS cus
    ON
        cou.id = cus.country_id
    WHERE
        CONCAT(cus.first_name, ' ', cus.last_name) LIKE customer_full_name;
END;
$$
LANGUAGE plpgsql;


-- CALL sp_customer_country_name('Betty Wallace', '');
-- CALL sp_customer_country_name('Rachel Bishop', '');
-- CALL sp_customer_country_name('Jerry Andrews', '');


----------------------------------------------------------------------------
-- CREATE OR REPLACE PROCEDURE sp_customer_country_name(
--     IN customer_full_name VARCHAR (50),
--     OUT country VARCHAR (50)
-- ) AS
-- $$
-- BEGIN
--     SELECT c.name
--     INTO country
--     FROM countries AS c
--     JOIN customers AS cus
--     ON c.id = cus.country_id
--     WHERE CONCAT(cus.first_name, ' ', cus.last_name) = customer_full_name;
-- END;
-- $$
-- LANGUAGE plpgsql;


----------------------------------------------------------------------------
-- CREATE OR REPLACE PROCEDURE sp_customer_country_name(
--     IN customer_full_name VARCHAR(50),
--     OUT country_name VARCHAR(50)
-- )
-- AS
-- $$
-- BEGIN
--     SELECT coun.name
--     INTO country_name
--     FROM countries AS coun
--              JOIN customers AS cus
--                   ON coun.id = cus.country_id
--     WHERE customer_full_name = CONCAT(cus.first_name, ' ', cus.last_name);
-- END;
-- $$
--     LANGUAGE plpgsql;

-- -- CALL sp_customer_country_name('Betty Wallace', '');
-- -- CALL sp_customer_country_name('Rachel Bishop', '');
-- -- CALL sp_customer_country_name('Jerry Andrews', '');

