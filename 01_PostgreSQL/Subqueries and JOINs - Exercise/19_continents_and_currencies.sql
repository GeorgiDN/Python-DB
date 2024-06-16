CREATE VIEW 
	continent_currency_usage 
AS
SELECT 
	c.continent_code,
    c.currency_code,
    COUNT(*) AS currency_usage
FROM 
	countries c
GROUP BY 
	c.continent_code,
    c.currency_code
HAVING COUNT(*) > 1
   AND COUNT(*) =
       (SELECT COUNT(*) AS most_used_cur
        FROM countries c2
        WHERE c2.continent_code = c.continent_code
        GROUP BY c2.currency_code
        ORDER BY most_used_cur DESC
        LIMIT 1)
ORDER BY currency_usage DESC, c.continent_code;



-- CREATE VIEW continent_currency_usage AS
-- WITH count_data_table AS (
-- 		SELECT
-- 			continent_code
-- 			,currency_code
-- 			,COUNT(*) AS currency_usage
-- 		FROM countries
-- 		GROUP BY  continent_code,currency_code
-- 		HAVING COUNT(*) > 1),

-- ranked_data_table AS (
-- 		SELECT
-- 			continent_code
-- 			,currency_code
-- 			,currency_usage
-- 			,DENSE_RANK() OVER (PARTITION BY continent_code ORDER BY currency_usage DESC) AS ranked_table
-- 		FROM
-- 			count_data_table)

-- SELECT 
-- 	continent_code
-- 	,currency_code
-- 	,currency_usage
-- FROM
-- 	ranked_data_table
-- WHERE 
-- 	ranked_table = 1
-- ORDER BY
-- 	currency_usage DESC;
