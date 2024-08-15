SELECT
    CONCAT(a.first_name, ' ', a.last_name) AS full_name,
    CONCAT(
        LOWER(SUBSTRING(a.first_name, 1, 1)),
        LOWER(SUBSTRING(a.last_name, LENGTH(a.last_name) - 1, 2)),
        LENGTH(a.last_name),
        '@sm-cast.com'
    ) AS email,
    a.awards
FROM
    actors AS a
LEFT JOIN
    productions_actors AS pa
ON
    a.id = pa.actor_id
WHERE
    pa.actor_id IS NULL
ORDER BY
    a.awards DESC,
    a.id;
