SELECT
    id,
    name,
    continent,
    currency
FROM
    countries
WHERE
    continent LIKE 'South America'
AND
    (currency LIKE 'P%' or currency LIKE 'U%')
ORDER BY
    currency DESC,
    id;