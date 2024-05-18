ALTER TABLE
	countries
ADD COLUMN 
	capital_code CHAR(2);
	
UPDATE 
	countries
-- SET capital_code = substring(capital FROM 1 FOR 2);
SET 
	capital_code = LEFT(capital, 2);