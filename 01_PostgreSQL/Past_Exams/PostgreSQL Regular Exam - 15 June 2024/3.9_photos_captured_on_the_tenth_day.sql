SELECT
    CONCAT(LEFT(p.description, 10), '...') AS summary,
    TO_CHAR(p.capture_date, 'DD.MM HH24:MI' ) AS date
FROM
    photos AS p
WHERE
    EXTRACT('DAY' FROM capture_date) = 10
ORDER BY
    capture_date DESC
;


-- SELECT
--     CONCAT(SUBSTRING(description, 1, 10), '...') AS summary,
--     TO_CHAR(capture_date, 'DD.MM HH24:MI') AS "date"
-- FROM
--     photos AS p
-- WHERE
--     EXTRACT(DAY FROM capture_date) = 10
-- ORDER BY
--     capture_date DESC
