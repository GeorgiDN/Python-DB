UPDATE 
	countries
SET 
	country_name = 'Burma'
WHERE
	country_name = 'Myanmar';
	
INSERT INTO
	monasteries (monastery_name, country_code)
VALUES
	('Hanga Abbey', (SELECT country_code FROM countries WHERE country_name = 'Tanzania')),
	('Myin-Tin-Daik', (SELECT country_code FROM countries WHERE country_name = 'Myanmar'));

SELECT
	con.continent_name,
	c.country_name,
	count(m.id) AS monasteries_count
FROM 
	continents AS con
LEFT JOIN 
	countries AS c
ON 
	c.continent_code = con.continent_code
LEFT JOIN 
	monasteries AS m 
ON m.country_code = c.country_code
WHERE 
	NOT c.three_rivers
GROUP BY
	c.country_name,
	continent_name
ORDER BY
	monasteries_count DESC, country_name;
	