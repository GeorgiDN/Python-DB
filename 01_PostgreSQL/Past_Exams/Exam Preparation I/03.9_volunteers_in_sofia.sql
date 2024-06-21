SELECT
    v.name AS volunteers,
    v.phone_number,
	SUBSTRING(
		v.address, POSITION('Sofia' IN v.address) + 7
) AS address
FROM
    volunteers as v
JOIN
    volunteers_departments AS vd
ON
    v.department_id = vd.id
WHERE
    vd.department_name LIKE 'Education program assistant'
AND
    v.address LIKE '%Sofia%'
ORDER BY
    v.name;




-- SELECT 
-- 	v.name,
-- 	v.phone_number,
-- 	SUBSTRING(
-- 		v.address, POSITION('Sofia' IN v.address) + 7
-- ) AS address
-- FROM 
-- 	volunteers AS v
-- JOIN
-- 	volunteers_departments AS vd
-- ON 
-- 	vd.id = v.department_id
-- WHERE 
-- 	vd.department_name = 'Education program assistant' 
-- AND 
-- 	v.address LIKE '%Sofia%'
-- ORDER BY v.name;
