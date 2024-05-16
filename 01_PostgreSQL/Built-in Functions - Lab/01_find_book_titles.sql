SELECT title
FROM books
WHERE starts_with(title, 'The')
ORDER BY id;



-- WHERE title LIKE 'The %'


-- WHERE LEFT(title, 1, 3) = 'The'


-- WHERE substr(title, 1, 3) = 'The'
