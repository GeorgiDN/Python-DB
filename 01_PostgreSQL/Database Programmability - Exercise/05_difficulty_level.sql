CREATE OR REPLACE FUNCTION fn_difficulty_level(
    level INT
) RETURNS VARCHAR (40)
AS
$$
    DECLARE level_of_difficulty VARCHAR(40);
BEGIN
    IF level <= 40 THEN level_of_difficulty := 'Normal Difficulty';
    ELSIF level BETWEEN 41 AND 60 THEN level_of_difficulty := 'Nightmare Difficulty';
    ELSIF level > 60 THEN level_of_difficulty := 'Hell Difficulty';
END IF;
    RETURN level_of_difficulty;
END;
$$
LANGUAGE plpgsql;


SELECT
	user_id,
	level,
	cash,
	fn_difficulty_level(level)
FROM
	users_games
ORDER BY
	user_id;





-- CREATE OR REPLACE FUNCTION fn_difficulty_level(
-- 	IN level INT,
-- 	OUT difficulty_level VARCHAR
-- )AS
-- $$
-- BEGIN
-- 	IF level <= 40 THEN 
-- 		difficulty_level := 'Normal Difficulty';
-- 	ELSIF level BETWEEN 41 AND 60 THEN
-- 		difficulty_level := 'Nightmare Difficulty';
-- 	ELSE 
-- 		difficulty_level := 'Hell Difficulty';
-- 	END IF;
-- END;
-- $$
-- LANGUAGE plpgsql;


-- SELECT 
-- 	user_id,
-- 	level,
-- 	cash,
-- 	fn_difficulty_level(level)
-- FROM 
-- 	users_games
-- ORDER BY 
-- 	user_id ASC;
	