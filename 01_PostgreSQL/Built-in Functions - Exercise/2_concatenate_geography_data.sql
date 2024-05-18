CREATE VIEW 
	view_continents_countries_currencies_details
AS
SELECT 
	CONCAT_WS(': ', con.continent_name, con.continent_code) AS "continent_details",
	CONCAT_WS(' - ', cou.country_name, cou. capital, cou.area_in_sq_km, 'km2') AS "country_information",
	CONCAT(cur.description, ' (', cur.currency_code, ')') AS "currencies"
FROM 
	continents AS con,
	countries AS cou,
	currencies AS cur
WHERE 
	con.continent_code = cou.continent_code
		AND
	cou.currency_code = cur.currency_code
ORDER BY
	"country_information" ASC,
	"currencies" ASC;



-- CREATE VIEW view_continents_countries_currencies_details AS
-- SELECT concat_ws(': ', c2.continent_name, c2.continent_code)               AS "continent_details",
--        concat_ws(' - ', c1.country_name, capital, c1.area_in_sq_km, 'km2') AS "country_information",
--        concat(c3.description, ' (', c3.currency_code, ')')                 AS "currencies"

-- FROM countries c1
--          JOIN continents c2 on c1.continent_code = c2.continent_code
--          JOIN currencies c3 on c3.currency_code = c1.currency_code
-- ORDER BY "country_information", "currencies";