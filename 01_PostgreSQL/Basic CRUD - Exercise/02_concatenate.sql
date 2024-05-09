SELECT
	CONCAT(name, ' ', state) as "Cities Information",
	area as "area_km2"
FROM 
	cities
ORDER BY
    id;
	