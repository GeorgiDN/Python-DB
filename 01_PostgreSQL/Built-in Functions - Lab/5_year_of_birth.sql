SELECT 
	first_name,
	last_name,
	TO_CHAR(born, 'YYYY') as year
FROM authors;


-- SELECT 
-- 	first_name,
-- 	last_name,
-- 	EXTRACT(YEAR FROM born) AS year
-- FROM 
-- 	authors;