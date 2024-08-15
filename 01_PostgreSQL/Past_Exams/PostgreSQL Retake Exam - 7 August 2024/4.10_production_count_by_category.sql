DROP FUNCTION IF EXISTS udf_category_productions_coun;
CREATE FUNCTION udf_category_productions_count(
    IN category_name VARCHAR(50),
    OUT curr_message varchar(50)
) AS
$$
BEGIN
    SELECT
        CONCAT('Found', ' ', COUNT(cp.category_id), ' ', 'productions.')
    FROM categories AS c
    LEFT JOIN categories_productions AS cp
    ON c.id = cp.category_id
    WHERE category_name LIKE c.name
    INTO curr_message;
END;
$$
LANGUAGE plpgsql;

-- SELECT udf_category_productions_count('Nonexistent') AS message_text;
-- SELECT udf_category_productions_count('History') AS message_text;
