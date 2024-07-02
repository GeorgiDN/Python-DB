CREATE OR REPLACE FUNCTION fn_feedbacks_for_product(
    product_name VARCHAR(25)
)
    RETURNS TABLE
            (
                customer_id          INT,
                customer_name        VARCHAR(75),
                feedback_description VARCHAR(255),
                feedback_rate        NUMERIC(4, 2)
            )
AS
$$
BEGIN
    RETURN QUERY
        (SELECT c.id,
                c.first_name,
                f.description,
                f.rate
         FROM feedbacks AS f
                  JOIN customers AS c
                       ON f.customer_id = c.id
                  JOIN products AS p
                       ON f.product_id = p.id
         WHERE p.name = product_name
         ORDER BY f.customer_id);
END;
$$
    LANGUAGE plpgsql;


-- SELECT *
-- FROM fn_feedbacks_for_product('Banitsa');
--
-- SELECT *
-- FROM fn_feedbacks_for_product('ALCOHOL');

-- SELECT * FROM fn_feedbacks_for_product('Bread');





-- CREATE OR REPLACE FUNCTION fn_feedbacks_for_product(
--     product_name VARCHAR(25)
-- ) RETURNS TABLE (
--     customer_id INT,
--     customer_name VARCHAR(75),
--     feedback_description VARCHAR(255),
--     feedback_rate NUMERIC(4, 2)
-- )
-- AS
-- $$
-- BEGIN
--     RETURN QUERY
--     SELECT f.customer_id,
--            c.first_name,
--            f.description,
--            f.rate
--     FROM customers AS c
--     JOIN feedbacks AS f
--     ON c.id = f.customer_id
--     JOIN products AS p
--     ON f.product_id = p.id
--     WHERE product_name = p.name
--     ORDER BY f.customer_id
-- ;
-- END;
-- $$
-- LANGUAGE plpgsql;


-- -- SELECT * FROM fn_feedbacks_for_product('Banitsa');
-- -- SELECT * FROM fn_feedbacks_for_product('ALCOHOL');
-- -- SELECT * FROM fn_feedbacks_for_product('Bread');
