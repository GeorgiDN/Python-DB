SELECT REPLACE(title, 'The', '***') AS title
FROM books
WHERE starts_with(title, 'The')
ORDER BY id;