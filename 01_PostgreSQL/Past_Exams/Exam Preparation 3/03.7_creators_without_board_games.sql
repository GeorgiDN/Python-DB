SELECT
    cr.id,
    CONCAT(cr.first_name, ' ', cr.last_name) AS creator_name,
    cr.email
FROM
    creators AS cr
LEFT JOIN
    creators_board_games AS crbg
ON
    cr.id = crbg.creator_id
WHERE
    crbg.creator_id IS NULL
ORDER BY
    creator_name;



-- SELECT
--     c.id,
--     CONCAT(c.first_name, ' ', c.last_name) AS creator_name,
--     c.email
-- FROM
--     creators AS c
-- LEFT JOIN
--     creators_board_games AS cbg
-- ON
--     c.id = cbg.creator_id
-- LEFT JOIN
--     board_games AS bg
-- ON
--     cbg.board_game_id = bg.id
-- WHERE
--     cbg.creator_id IS NULL
-- ORDER BY
--     creator_name;


