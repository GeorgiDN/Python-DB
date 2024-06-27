CREATE OR REPLACE FUNCTION fn_creator_with_board_games(
    IN first_name_of_creator VARCHAR(30),
    OUT number_of_board_games INT
)
AS
$$
BEGIN
    SELECT
        COUNT(crbg.creator_id)
        FROM creators AS cr
        JOIN creators_board_games AS crbg
        ON cr.id = crbg.creator_id
        WHERE cr.first_name LIKE first_name_of_creator
        INTO number_of_board_games;
END;
$$
LANGUAGE plpgsql;

-- SELECT fn_creator_with_board_games('Bruno')
-- SELECT fn_creator_with_board_games('Alexander')





-- CREATE OR REPLACE FUNCTION fn_creator_with_board_games(
--     IN first_name_creator VARCHAR (30),
--     OUT count_board_games INT
-- )
-- AS
-- $$
-- BEGIN
--     SELECT COUNT(bg.id)
--     INTO count_board_games
--     FROM creators AS c
--     JOIN creators_board_games AS crbg
--         ON c.id = crbg.creator_id
--     JOIN board_games AS bg
--         ON crbg.board_game_id = bg.id
--     WHERE c.first_name = first_name_creator;
-- END;
-- $$
-- LANGUAGE plpgsql;

-- -- SELECT fn_creator_with_board_games('Bruno');
-- -- SELECT fn_creator_with_board_games('Alexander');
