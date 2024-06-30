SELECT p.id,
       CONCAT(p.first_name, ' ', p.last_name) AS full_name,
       p.age,
       p.position,
       p.salary,
       sd.pace,
       sd.shooting
FROM players AS p
         JOIN skills_data AS sd
              ON p.skills_data_id = sd.id
WHERE sd.pace + sd.shooting > 130
  AND p.position LIKE 'A'
  AND p.team_id IS NULL;




-- SELECT
--     pl.id,
--     CONCAT(pl.first_name, ' ', pl.last_name) as full_name,
--     pl.age,
--     pl.position,
--     pl.salary,
--     sd.pace,
--     sd.shooting
-- FROM
--     players AS pl
-- JOIN
--     skills_data AS sd
-- ON
--     pl.skills_data_id = sd.id
-- WHERE
--     sd.pace + sd.shooting > 130
-- AND
--     pl.position = 'A'
-- AND
--     pl.team_id IS NULL;
