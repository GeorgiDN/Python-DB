SELECT
    a.name,
    a.country,
    b.booked_at::DATE
FROM
    apartments AS a
LEFT JOIN
    bookings AS b
USING
    (booking_id)
LIMIT 10
;


-- SELECT 
-- 	a.name,
-- 	a.country,
-- 	b.booked_at::DATE
-- FROM 
-- 	apartments AS a
-- LEFT JOIN 
-- 	bookings AS b
-- ON b.booking_id = a.booking_id
-- LIMIT 10;




-- SELECT
--     a.name,
--     a.country,
--     b.booked_at::DATE
-- FROM
--     bookings AS b
-- RIGHT JOIN
--     apartments AS a
-- USING
--     (booking_id)
-- LIMIT 10
-- ;
