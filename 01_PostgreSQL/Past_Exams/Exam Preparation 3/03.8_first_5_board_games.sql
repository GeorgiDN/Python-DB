SELECT
    bg.name,
    bg.rating,
    c.name
FROM
    board_games AS bg
JOIN
    categories AS c
ON
    bg.category_id = c.id
JOIN
    players_ranges AS pr
ON
    bg.players_range_id = pr.id
WHERE
    (bg.rating > 7 AND bg.name ILIKE '%a%')
OR
    (bg.rating > 7.50 AND (pr.min_players >= 2 AND pr.max_players <= 5))
ORDER BY
    bg.name,
    bg.rating DESC
LIMIT 5;






-- SELECT
--     bg.name,
--     bg.rating,
--     cat.name
-- FROM
--     board_games AS bg
-- JOIN
--     categories AS cat
-- ON
--     bg.category_id = cat.id
-- JOIN
--     players_ranges AS pr
-- ON
--     bg.players_range_id = pr.id
-- WHERE
--     (bg.rating > 7 AND bg.name ILIKE '%a%')
-- OR
--     (bg.rating > 7.50
-- AND
--      ((pr.min_players BETWEEN 2 AND 5)
--           AND
--      (pr.max_players BETWEEN 2 AND 5)))
-- ORDER BY
--     bg.name,
--     bg.rating DESC
-- LIMIT 5;
