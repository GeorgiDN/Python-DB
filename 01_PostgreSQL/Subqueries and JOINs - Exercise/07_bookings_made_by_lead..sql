SELECT
    b.apartment_id,
    b.booked_for,
    c.first_name,
    c.country
FROM
    bookings AS b
JOIN
    customers AS c
USING
    (customer_id)
WHERE
    c.job_type LIKE '%Lead%'
;




-- SELECT 
-- 	b.apartment_id,
-- 	b.booked_for,
-- 	c.first_name,
-- 	c.country
-- FROM 
-- 	customers AS c
--     JOIN bookings b USING (customer_id)
-- WHERE c.job_type = 'Lead';
