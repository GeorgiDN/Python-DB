SELECT
    CONCAT(cr.first_name, ' ', cr.last_name) as full_name,
    cr.email,
    MAX(bg.rating) AS rating
FROM
    creators AS cr
JOIN
    creators_board_games AS crbg
ON
    cr.id = crbg.creator_id
JOIN
    board_games AS bg
ON
    crbg.board_game_id = bg.id
WHERE
    cr.email LIKE '%.com'
GROUP BY
    cr.first_name, cr.last_name, cr.email
ORDER BY
    full_name;




-- SELECT
--     CONCAT(c.first_name, ' ', c.last_name) AS full_name,
--     c.email,
--     MAX(bg.rating) AS rating
-- FROM
--     creators AS c
-- JOIN
--     creators_board_games AS crbg
-- ON
--     c.id = crbg.creator_id
-- JOIN
--     board_games AS bg
-- ON
--     bg.id = crbg.board_game_id
-- WHERE
--     c.email LIKE '%.com'
-- GROUP BY
--     c.id
-- ORDER BY
--     full_name;




-- WITH highest_ratings AS (
--     SELECT
--         c.id AS creator_id,
--         MAX(bg.rating) AS max_rating
--     FROM
--         creators AS c
--     JOIN
--         creators_board_games AS crbg
--     ON
--         c.id = crbg.creator_id
--     JOIN
--         board_games AS bg
--     ON
--         bg.id = crbg.board_game_id
--     WHERE
--         c.email LIKE '%.com'
--     GROUP BY
--         c.id
-- )
-- SELECT
--     CONCAT(c.first_name, ' ', c.last_name) AS full_name,
--     c.email,
--     hr.max_rating AS rating
-- FROM
--     highest_ratings AS hr
-- JOIN
--     creators AS c
-- ON
--     hr.creator_id = c.id
-- ORDER BY
--     full_name;