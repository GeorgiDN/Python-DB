SELECT 
	COUNT(*) AS countries_without_rivers
FROM 
	countries c
LEFT JOIN 
	countries_rivers cr 
USING 
	(country_code)   -- where the name is the same in both columns
WHERE 
	cr.country_code IS NULL;
	



-- SELECT 
-- 	COUNT(*) AS countries_without_rivers
-- FROM 
-- 	countries c
-- LEFT JOIN 
-- 	countries_rivers cr 
-- ON 
-- 	cr.country_code = c.country_code
-- WHERE 
-- 	cr.country_code IS NULL;
