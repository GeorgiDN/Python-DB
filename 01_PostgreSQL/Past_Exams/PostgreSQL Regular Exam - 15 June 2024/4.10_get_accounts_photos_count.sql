CREATE OR REPLACE FUNCTION udf_accounts_photos_count(
    IN account_username VARCHAR(30),
    OUT num_photos INT
) AS
$$
BEGIN
    SELECT COUNT(p.id)
    FROM accounts AS a
    JOIN accounts_photos AS ap
    ON a.id = ap.account_id
    JOIN photos AS p
    ON ap.photo_id = p.id
    WHERE a.username = account_username
    INTO num_photos;
END;
$$
LANGUAGE plpgsql;

-- SELECT udf_accounts_photos_count('ssantryd') AS photos_count;
