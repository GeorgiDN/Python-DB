SELECT
    username,
    gender,
    age
FROM accounts
WHERE age >= 18 AND char_length(username) > 9
ORDER BY age DESC, username
