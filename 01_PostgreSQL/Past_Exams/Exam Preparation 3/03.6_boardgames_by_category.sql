SELECT
    bg.id,
    bg.name,
    bg.release_year,
    cat.name AS category_name
FROM
    board_games AS bg
JOIN
    categories AS cat
ON
    cat.id = bg.category_id
WHERE
    cat.name IN ('Strategy Games', 'Wargames')
ORDER BY
    release_year DESC;
