SELECT 
	REPLACE (mountain_range, 'a', '@') as replace_a,
	REPLACE (mountain_range, 'A', '$') as replace_A
FROM
	mountains;
