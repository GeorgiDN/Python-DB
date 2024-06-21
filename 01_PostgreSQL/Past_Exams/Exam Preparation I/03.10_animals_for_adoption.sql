SELECT
    a.name,
    EXTRACT(YEAR FROM a.birthdate) AS "birth_year",
    at.animal_type
FROM
    animals AS a
LEFT JOIN
    animal_types AS at
ON
    a.animal_type_id = at.id
LEFT JOIN
    owners AS o
ON
    a.owner_id = o.id
WHERE
    at.animal_type NOT LIKE 'Birds'
AND
    a.owner_id IS NULL
AND
    a.birthdate > DATE '2022-01-01' - INTERVAL '5 years'
ORDER BY
    a.name;



-- SELECT 
-- 	a.name AS animal,
--     EXTRACT(YEAR FROM a.birthdate) AS "birth_year",
--     at.animal_type
-- FROM 
-- 	animals AS a
-- JOIN 
-- 	animal_types AS at 
-- ON 
-- 	at.id = a.animal_type_id
-- WHERE 
-- 	at.animal_type <> 'Birds' 
-- 	AND
-- 	owner_id IS NULL
-- 	AND
-- 	EXTRACT(YEAR FROM AGE('01/01/2022', a.birthdate)) < 5
-- ORDER BY 
-- 	a.name;
