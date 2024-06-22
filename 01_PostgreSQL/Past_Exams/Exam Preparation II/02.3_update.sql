UPDATE cars
SET condition = 'C'
WHERE
    (mileage IS NULL
OR
    mileage >= 800000)
AND
    year <= 2010
AND
    make NOT LIKE 'Mercedes-Benz';


-- UPDATE cars
-- SET condition = 'C'
-- WHERE
--     (mileage > 800000 OR mileage IS NULL)
--     AND
--     year <= 2010
--     AND
--     make <> 'Mercedes-Benz';
