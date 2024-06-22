DELETE FROM clients
WHERE 
    LENGTH(full_name) > 3
AND 
    id NOT IN (SELECT client_id FROM courses);
	
	
	
-- DELETE FROM clients
-- WHERE LENGTH(full_name) > 3
-- AND NOT EXISTS (
--     SELECT 1
--     FROM courses
--     WHERE courses.client_id = clients.id
-- );