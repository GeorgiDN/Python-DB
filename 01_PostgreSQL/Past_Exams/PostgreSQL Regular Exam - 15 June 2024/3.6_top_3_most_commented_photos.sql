SELECT
    p.id AS photo_id,
    capture_date,
    description,
    COUNT(c.id) AS comments_count
FROM
    photos AS p
JOIN
    comments AS c
ON
    p.id = c.photo_id
WHERE
    description IS NOT NULL
GROUP BY
    p.id,
    capture_date,
    description
ORDER BY
    comments_count DESC,
    photo_id
LIMIT 3;


