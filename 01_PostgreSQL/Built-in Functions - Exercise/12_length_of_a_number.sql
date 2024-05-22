SELECT 
	population,
	LENGTH(population::VARCHAR) AS length
From countries;



-- SELECT 
-- 	population,
-- 	LENGTH(CAST(population AS VARCHAR)) AS "length"
-- FROM countries;