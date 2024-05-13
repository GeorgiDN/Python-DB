UPDATE
	employees
SET
	salary = salary + 1500,
	job_title = CONCAT('Senior', ' ', job_title)
WHERE 
	hire_date BETWEEN '1998-01-01' AND '2000-01-05';


	
	
-- UPDATE employees
-- SET salary = salary + 1500,
-- job_title = CONCAT ('Senior', ' ', job_title)
-- WHERE hire_date BETWEEN 'January 1, 1998' AND 'January 5, 2000';




-------------------------------------
-- CHECK CELL that contains senior
-- SELECT 
--     first_name,
--     job_title,
--     salary
-- FROM employees
-- WHERE job_title LIKE '%Senior%';
