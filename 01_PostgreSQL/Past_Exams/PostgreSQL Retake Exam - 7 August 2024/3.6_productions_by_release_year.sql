SELECT
    p.id,
    p.title,
    pi.duration,
    ROUND(pi.budget, 1) AS budget,
    TO_CHAR(pi.release_date:: DATE, 'MM-YY') AS release_date
FROM
    productions AS p
JOIN
    productions_info AS pi
ON
    p.production_info_id = pi.id
WHERE
    (EXTRACT(YEAR FROM pi.release_date) = 2023
         OR
     EXTRACT(YEAR FROM pi.release_date) = 2024)
AND
    pi.budget > 1500000
ORDER BY
    budget,
    pi.duration DESC,
    p.id
LIMIT 3;
