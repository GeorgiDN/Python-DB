SELECT
    CONCAT(a.id, ' ', a.username) AS id_username,
    a.email AS email
FROM
    accounts AS a
JOIN
    accounts_photos AS ap
ON
    a.id = ap.account_id
WHERE
    ap.photo_id = ap.account_id
ORDER BY
    a.id;


-- SELECT
--     CONCAT(a.id, ' ', a.username) AS id_username,
--     a.email
-- FROM
--     accounts AS a
-- JOIN
--     accounts_photos AS ap
-- ON
--     a.id = ap.account_id
-- JOIN
--     photos AS p
-- ON
--     ap.photo_id = p.id
-- WHERE
--     a.id = ap.photo_id
-- ORDER BY
--     a.id;
