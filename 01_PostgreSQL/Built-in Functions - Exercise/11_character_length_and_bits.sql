SELECT 
	CONCAT_WS(' ', m.mountain_range, p.peak_name) AS "mountain_information",
    CHAR_LENGTH(CONCAT_WS(' ', m.mountain_range, p.peak_name)) AS "characters_length",
    BIT_LENGTH(CONCAT_WS(' ', m.mountain_range, p.peak_name)) AS "bits_of_a_string"
FROM 
	mountains AS m,
	peaks AS P
WHERE
	m."id" = p.mountain_id;



-- SELECT concat_ws(' ', m.mountain_range, p.peak_name)             AS "mountain_information",
--        CHAR_LENGTH(concat_ws(' ', m.mountain_range, p.peak_name))     AS "characters_length",
--        bit_length(concat_ws(' ', m.mountain_range, p.peak_name)) AS "bits_of_a_string"
-- FROM mountains m
--          JOIN peaks p on m.id = p.mountain_id;
