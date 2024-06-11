SELECT 
	b.booking_id,
	CONCAT(c.first_name, ' ', c.last_name) AS customer_name
FROM 
	bookings AS b
	CROSS JOIN customers AS c
ORDER BY 
	customer_name;