SELECT 
	e.employee_id,
	CONCAT(e.first_name, ' ', e.last_name) AS full_name,
	d.department_id,
	d.name AS deparment_name
FROM 
	employees AS e JOIN	
		departments AS d
			ON e.employee_id = d.manager_id
ORDER BY employee_id
LIMIT 5;