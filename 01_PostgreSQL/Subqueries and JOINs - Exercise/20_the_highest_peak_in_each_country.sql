WITH data_table AS (SELECT
    cn.country_name
    ,COALESCE(pe.peak_name, '(no highest peak)') AS highest_peak_name
    ,COALESCE(pe.elevation, 0) AS highest_peak_elevation
    ,COALESCE(mn.mountain_range, '(no mountain)') AS mountain
    ,ROW_NUMBER() OVER (PARTITION BY cn.country_name ORDER BY pe.elevation DESC) AS peak_rank

        FROM countries AS cn
		LEFT JOIN mountains_countries AS mc USING (country_code)
		LEFT JOIN peaks AS pe USING (mountain_id)
        LEFT JOIN mountains AS mn ON mn."id" = pe.mountain_id)


SELECT
    country_name
    ,highest_peak_name
    ,highest_peak_elevation
    ,mountain

FROM data_table
WHERE peak_rank = 1
ORDER BY country_name ASC ,highest_peak_elevation DESC;