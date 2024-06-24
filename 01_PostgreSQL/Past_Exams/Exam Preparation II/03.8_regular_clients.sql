SELECT
    c.full_name,
    COUNT(cou.car_id) AS count_of_cars,
    SUM(bill) AS total_sum
FROM
    clients AS c
JOIN
    courses AS cou
ON
    c.id = cou.client_id
WHERE
    c.full_name LIKE '_a%'
GROUP BY
    c.full_name
HAVING
    COUNT(cou.car_id) > 1
ORDER BY
    c.full_name;




-- SELECT
--     cl.full_name,
--     COUNT(car_id) AS count_of_cars,
--     SUM(COALESCE (cou.bill, 0)) AS total_sum
-- FROM
--     clients AS cl
-- JOIN
--     courses AS cou 
-- 	ON
-- 	cou.client_id = cl.id
-- WHERE
--     SUBSTRING(cl.full_name, 2, 1) = 'a'
-- GROUP BY
--     cl.full_name
-- HAVING
--     COUNT(cl.id) > 1
-- ORDER BY
--     cl.full_name;