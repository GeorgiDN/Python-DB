SELECT title,
	ROUND(cost, 3) AS modified_price
FROM books
ORDER BY id;