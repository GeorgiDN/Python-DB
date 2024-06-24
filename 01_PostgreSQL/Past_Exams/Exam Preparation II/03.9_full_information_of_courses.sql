SELECT
    a.name AS address,
    CASE
        WHEN EXTRACT(HOUR FROM cou.start) BETWEEN 6 AND 20 THEN 'Day'
        ELSE 'Night'
        END AS day_time,
    cou.bill,
    cl.full_name,
    ca.make,
    ca.model,
    cat.name AS category_name
FROM
    addresses AS a
JOIN
    courses AS cou
ON
    a.id = cou.from_address_id
JOIN
    clients AS cl
ON
    cou.client_id = cl.id
JOIN
    cars AS ca
ON
    cou.car_id = ca.id
JOIN
    categories AS cat
ON
    ca.category_id = cat.id
ORDER BY
    cou.id;

