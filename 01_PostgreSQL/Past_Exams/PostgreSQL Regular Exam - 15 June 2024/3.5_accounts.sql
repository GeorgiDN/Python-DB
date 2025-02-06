SELECT
    username,
    gender,
    age
FROM
    accounts
WHERE
    (age >= 18)
AND
    CHAR_LENGTH(username) > 9
ORDER BY
    age DESC,
    username
;
