CREATE OR REPLACE PROCEDURE sp_players_team_name(
    IN player_name VARCHAR(50),
    OUT team_name VARCHAR(45)
)
LANGUAGE plpgsql
AS $$
BEGIN
    SELECT
        COALESCE(t.name, 'The player currently has no team')
    INTO
        team_name
    FROM
        players AS p
    LEFT JOIN
        teams AS t
        ON p.team_id = t.id
    WHERE
        CONCAT_WS(' ', p.first_name, p.last_name) = player_name;
END;
$$;


-- CALL sp_players_team_name('Thor Serrels', '');
-- CALL sp_players_team_name('Walther Olenchenko', '');
-- CALL sp_players_team_name('Isaak Duncombe', '');






-- CREATE OR REPLACE PROCEDURE sp_players_team_name(
--     IN player_name VARCHAR(50),
--     OUT team_name VARCHAR(45)
-- )
-- AS
-- $$
-- BEGIN
--     SELECT 
--         COALESCE(t.name, 'The player currently has no team')
--     INTO team_name
--     FROM players AS p
--     LEFT JOIN teams AS t ON p.team_id = t.id
--     WHERE CONCAT(p.first_name, ' ', p.last_name) = player_name;

--     IF team_name IS NULL THEN
--         team_name := 'The player currently has no team';
--     END IF;
-- END;
-- $$
-- LANGUAGE plpgsql;





-- CREATE OR REPLACE PROCEDURE sp_players_team_name(
--     IN player_name VARCHAR(50),
--     OUT team_name VARCHAR(45)
-- )
-- AS
-- $$
-- BEGIN
--     SELECT t.name
--     INTO team_name
--     FROM teams t
--              JOIN players p ON t.id = p.team_id
--     WHERE concat_ws(' ', p.first_name, p.last_name) = player_name;

--     IF NOT FOUND THEN
--         team_name := 'The player currently has no team';
--     END IF;
-- END;
-- $$
--     LANGUAGE plpgsql;


-- CALL sp_players_team_name('Thor Serrels', '');
-- CALL sp_players_team_name('Walther Olenchenko', '');
-- CALL sp_players_team_name('Isaak Duncombe', '');
