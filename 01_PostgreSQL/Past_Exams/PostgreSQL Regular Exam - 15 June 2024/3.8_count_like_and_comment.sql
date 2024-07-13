WITH likes_count AS (
    SELECT
        photo_id,
        COUNT(id) AS likes_count
    FROM
        likes
    GROUP BY
        photo_id
),
comments_count AS (
    SELECT
        photo_id,
        COUNT(id) AS comments_count
    FROM
        comments
    GROUP BY
        photo_id
)
SELECT
    p.id AS photo_id,
    COALESCE(lc.likes_count, 0) AS likes_count,
    COALESCE(cc.comments_count, 0) AS comments_count
FROM
    photos AS p
LEFT JOIN
    likes_count AS lc
ON
    p.id = lc.photo_id
LEFT JOIN
    comments_count AS cc
ON
    p.id = cc.photo_id
ORDER BY
    likes_count DESC,
    comments_count DESC,
    p.id;




-- SELECT p.id                          AS photo_id,
--        COALESCE(l.likes_count, 0)    AS likes_count,
--        COALESCE(c.comments_count, 0) AS comments_count
-- FROM photos AS p
--          LEFT JOIN (SELECT photo_id,
--                            COUNT(*) AS likes_count
--                     FROM likes
--                     GROUP BY photo_id) l ON p.id = l.photo_id
--          LEFT JOIN (SELECT photo_id,
--                            COUNT(*) AS comments_count
--                     FROM comments
--                     GROUP BY photo_id) c ON p.id = c.photo_id
-- ORDER BY likes_count DESC,
--          comments_count DESC,
--          photo_id;
		 
		 



-- SELECT p.id                          AS photo_id,
--        COALESCE(l.likes_count, 0)    AS likes_count,
--        COALESCE(c.comments_count, 0) AS comments_count
-- FROM photos AS p
--          LEFT JOIN (SELECT photo_id,
--                            COUNT(*) AS likes_count
--                     FROM likes
--                     GROUP BY photo_id) AS l
--             ON p.id = l.photo_id

--          LEFT JOIN (SELECT photo_id,
--                            COUNT(*) AS comments_count
--                     FROM comments
--                     GROUP BY photo_id) AS c
--              ON p.id = c.photo_id
-- ORDER BY likes_count DESC,
--          comments_count DESC,
--          photo_id;
	 
		 
