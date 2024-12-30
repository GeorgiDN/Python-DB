CREATE OR REPLACE FUNCTION udf_category_productions_count(
    IN category_name VARCHAR(50),
    OUT result VARCHAR(50)
) AS
$$
BEGIN
    SELECT
        CONCAT('Found', ' ', COUNT(cp.production_id), ' ',  'productions.')
    FROM
        categories AS c
    JOIN
        categories_productions AS cp
    ON
        c.id = cp.category_id
    WHERE
        c.name LIKE category_name
    INTO
        result;
END;
$$
LANGUAGE plpgsql;

-- SELECT udf_category_productions_count('Nonexistent') AS message_text;
-- SELECT udf_category_productions_count('History') AS message_text;
