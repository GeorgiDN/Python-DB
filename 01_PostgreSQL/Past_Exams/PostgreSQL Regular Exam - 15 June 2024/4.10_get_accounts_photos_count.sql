DROP FUNCTION IF EXISTS  udf_accounts_photos_count;
CREATE  FUNCTION udf_accounts_photos_count(
    IN account_username VARCHAR(30),
    OUT num_photos INT
) AS
$$
BEGIN
    SELECT
        COUNT(ap.photo_id)
    INTO
        num_photos
    FROM
        accounts AS a
    JOIN
        accounts_photos AS ap
    ON
        a.id = ap.account_id
    WHERE
        a.username LIKE account_username;
END;
$$
LANGUAGE plpgsql;

-- SELECT udf_accounts_photos_count('ssantryd') AS photos_count;


-- CREATE OR REPLACE FUNCTION udf_accounts_photos_count(
--     IN account_username VARCHAR(30),
--     OUT num_photos INT
-- ) AS
-- $$
-- BEGIN
--     SELECT COUNT(p.id)
--     FROM accounts AS a
--     JOIN accounts_photos AS ap
--     ON a.id = ap.account_id
--     JOIN photos AS p
--     ON ap.photo_id = p.id
--     WHERE a.username = account_username
--     INTO num_photos;
-- END;
-- $$
-- LANGUAGE plpgsql;
