SELECT 
	department_id,
    count(*) AS employee_count
FROM 
	employees
GROUP BY 
	department_id
ORDER BY 
	department_id;
	
	
	
-- SELECT 
-- 	department_id,
-- 	COUNT(department_id) AS "employee_count"
-- FROM
-- 	employees
-- GROUP BY 
-- 	department_id
-- ORDER BY department_id;