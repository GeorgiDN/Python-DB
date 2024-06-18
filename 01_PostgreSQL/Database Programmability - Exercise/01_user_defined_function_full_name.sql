CREATE OR REPLACE FUNCTION fn_full_name(
    IN first_name VARCHAR,
    IN last_name VARCHAR,
    OUT full_name VARCHAR
) AS
$$
BEGIN
    full_name := INITCAP(first_name || ' ' || last_name);
END
$$
LANGUAGE plpgsql;


-- SELECT fn_full_name('fred', 'sanford');
-- SELECT fn_full_name('', 'SIMPSONS');
-- SELECT fn_full_name('JOHN', '');
-- SELECT fn_full_name(NULL, NULL);



------------------------------------------------------------------------------------------
-- CREATE OR REPLACE FUNCTION fn_full_name(
--     IN first_name VARCHAR,
--     IN last_name VARCHAR,
--     OUT full_name VARCHAR
-- ) AS
-- $$
-- BEGIN
--     full_name := INITCAP(first_name) || ' ' || initcap(last_name);
-- END
-- $$
--     LANGUAGE plpgsql;

-- SELECT fn_full_name('fred', 'sanford')




--------------------------------------------------------------------------------------
-- CREATE OR REPLACE FUNCTION fn_full_name(
--     IN first_name VARCHAR (50),
--     IN last_name VARCHAR (50)
-- ) RETURNS VARCHAR (50)
-- AS
-- $$
--     DECLARE the_full_name VARCHAR (50);
-- BEGIN
--     IF first_name IS NULL AND last_name IS NULL THEN
--         the_full_name := NULL;
--     ELSIF first_name IS NULL AND last_name IS NOT NULL THEN
--         the_full_name := INITCAP(last_name);
--     ELSIF first_name IS NOT NULL AND last_name IS NULL THEN
--         the_full_name := INITCAP(first_name);
--     ELSE the_full_name := INITCAP(first_name || ' ' || last_name);
--     END IF;
--     RETURN the_full_name;
-- END;
-- $$
-- LANGUAGE plpgsql;






-----------------------------------------------------------------------------------
-- CREATE OR REPLACE FUNCTION fn_full_name (first_name VARCHAR, last_name VARCHAR)
-- RETURNS VARCHAR AS
-- $$
-- BEGIN
--     -- Check if both first_name and last_name are null
--     IF first_name IS NULL AND last_name IS NULL THEN
--         RETURN NULL;
--     -- Check if first_name is null
--     ELSIF first_name IS NULL THEN
--         RETURN UPPER(last_name);
--     -- Check if last_name is null
--     ELSIF last_name IS NULL THEN
--         RETURN UPPER(first_name);
--     ELSE
--         RETURN INITCAP(first_name || ' ' || last_name);
--     END IF;
-- END;
-- $$
-- LANGUAGE plpgsql;


-- SELECT fn_full_name('fred', 'sanford');

