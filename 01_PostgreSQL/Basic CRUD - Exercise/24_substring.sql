CREATE VIEW 
	view_initials AS
SELECT 
	LEFT(first_name, 2) AS initial,
	last_name
FROM 
	employees
ORDER BY 
	last_name;


-- SELECT * FROM public.view_initials