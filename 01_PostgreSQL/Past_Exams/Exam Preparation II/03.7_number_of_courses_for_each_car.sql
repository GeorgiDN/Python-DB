SELECT
    c.id AS "car_id",
    c.make,
    c.mileage,
    COUNT(cou.car_id) AS count_of_courses,
    ROUND(AVG(cou.bill), 2) AS average_bill
FROM
    cars AS c
LEFT JOIN
    courses AS cou
ON
    c.id = cou.car_id
GROUP BY
    c.id,
    c.make,
    c.mileage
HAVING COUNT(cou.car_id) <> 2
ORDER BY
    count_of_courses DESC,
    c.id;







-- SELECT
--     c.id AS car_id,
--     c.make,
--     c.mileage,
--     COUNT(co.car_id) AS count_of_coureses,
--     ROUND(AVG(co.bill)::NUMERIC, 2) AS average_bill
-- FROM
--     cars AS c
-- LEFT JOIN
--     courses AS co
-- ON
--     c.id = co.car_id
-- GROUP BY
--     c.id,
--     c.make,
--     c.mileage
-- HAVING
--     COUNT(co.id) != 2
-- ORDER BY
--     count_of_coureses DESC,
--     car_id;
