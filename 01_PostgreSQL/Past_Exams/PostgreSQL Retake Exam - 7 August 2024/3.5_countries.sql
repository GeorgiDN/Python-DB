SELECT
    id,
    name,
    continent,
    currency
FROM
    countries
WHERE
    continent = 'South America'
AND
    (currency LIKE 'P%' OR currency LIKE 'U%')
ORDER BY
    currency DESC,
    id;
