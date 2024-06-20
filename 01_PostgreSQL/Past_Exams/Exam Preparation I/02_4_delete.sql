-- 1
DELETE
FROM volunteers
WHERE department_id IN
      (SELECT id
       FROM volunteers_departments
       WHERE department_name LIKE 'Education program assistant');

DELETE FROM volunteers_departments
       WHERE department_name LIKE 'Education program assistant';



--2
-- DELETE FROM volunteers
-- WHERE department_id = 2;

-- DELETE FROM volunteers_departments
-- WHERE "id" = 2
-- RETURNING *;



-- 3
-- DELETE FROM volunteers_departments
-- WHERE department_name = 'Education program assistant';
