SELECT
	id AS "id",
	CONCAT_WS(' ',
		first_name,
		middle_name,
		last_name
	 ) AS "Full Name",
	 hire_date
FROM employees
ORDER BY hire_date
OFFSET 9;




-- SELECT id,
-- 	CONCAT(first_name, ' ', middle_name, ' ', last_name) AS "full_name",
-- 	hire_date
-- FROM employees
-- ORDER BY hire_date
-- OFFSET 9;
