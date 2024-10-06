UPDATE productions_info
SET duration = CASE
                   WHEN id < 15 THEN duration + 15
                   WHEN id >= 20 THEN duration + 20
                   ELSE duration
                END
WHERE synopsis IS NULL
