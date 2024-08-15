SELECT
    c.name,
    COUNT(p.country_id) AS productions_count,
    COALESCE(AVG(pi.budget), 0) AS avg_budget
FROM
    countries AS c
JOIN
    productions AS p
ON
    c.id = p.country_id
JOIN
    productions_info AS pi
ON
    p.production_info_id = pi.id
GROUP BY
    c.name
HAVING
    COUNT(p.country_id) > 0
ORDER BY
    productions_count DESC,
    c.name;
