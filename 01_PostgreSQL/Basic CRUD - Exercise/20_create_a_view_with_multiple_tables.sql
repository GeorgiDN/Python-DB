CREATE VIEW view_addresses AS
SELECT CONCAT(
	e.first_name, ' ', e.last_name) AS full_name,
	department_id,
	CONCAT(a.number, ' ', a.street) as address
FROM 
	employees e
JOIN 
	addresses a ON a.id = e.address_id
ORDER BY "address"

