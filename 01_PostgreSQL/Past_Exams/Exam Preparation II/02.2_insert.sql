INSERT INTO clients
    (full_name,
     phone_number)
SELECT
    CONCAT(d.first_name, ' ', d.last_name), '(088) 9999' || (d.id * 2)
FROM
    drivers as d
WHERE
    d.id BETWEEN 10 AND 20;


