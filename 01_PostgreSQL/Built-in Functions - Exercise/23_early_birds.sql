SELECT 
	user_id,
	AGE(starts_at, booked_at) AS "Eadrly Birds"
FROM
	bookings
WHERE 
	starts_at - booked_at >= '10 MONTHS';
	
	
	
-- SELECT user_id,
-- 	age(starts_at, booked_at) AS "Early Birds"
-- FROM bookings
-- WHERE starts_at - booked_at >= INTERVAL '10 MONTHS';