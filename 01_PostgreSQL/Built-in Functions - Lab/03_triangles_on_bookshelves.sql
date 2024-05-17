SELECT 
	id,
	(height * side) / 2 AS area
FROM 
	triangles
ORDER
	BY id;