UPDATE coaches
SET salary = salary * coach_level
WHERE first_name LIKE 'C%'
AND EXISTS (
    SELECT 1 
    FROM players_coaches 
    WHERE players_coaches.coach_id = coaches.id
);




-- UPDATE coaches
-- SET salary = salary * coach_level
-- WHERE first_name LIKE 'C%'
--   AND id IN (SELECT DISTINCT coach_id
--              FROM players_coaches
--              WHERE coach_id IS NOT NULL);
