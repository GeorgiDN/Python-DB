DROP TABLE IF EXISTS search_results;
CREATE TABLE search_results
(
    id             SERIAL PRIMARY KEY,
    name           VARCHAR(50),
    release_year   INT,
    rating         FLOAT,
    category_name  VARCHAR(50),
    publisher_name VARCHAR(50),
    min_players    VARCHAR(50),
    max_players    VARCHAR(50)
);

CREATE OR REPLACE PROCEDURE usp_search_by_category(
    category VARCHAR(50)
)
AS
$$
BEGIN
    TRUNCATE TABLE search_results;
    INSERT INTO search_results(name,
                               release_year,
                               rating,
                               category_name,
                               publisher_name,
                               min_players,
                               max_players)
    SELECT bg.name,
           bg.release_year,
           bg.rating,
           cat.name,
           pb.name,
           CONCAT(pr.min_players, ' people'),
           CONCAT(pr.max_players, ' people')
    FROM board_games AS bg
             JOIN categories AS cat
                  ON bg.category_id = cat.id
             JOIN publishers AS pb
                  ON bg.publisher_id = pb.id
             JOIN players_ranges AS pr
                  ON bg.players_range_id = pr.id
    WHERE category LIKE cat.name
    ORDER BY pb.name, bg.release_year DESC;
END;
$$
    LANGUAGE plpgsql;


-- CALL usp_search_by_category('Wargames');
--
-- SELECT * FROM search_results;




------------------------------------------------------------------------------------
-- DROP TABLE IF EXISTS search_results;
-- CREATE TABLE search_results (
--     id SERIAL PRIMARY KEY,
--     name VARCHAR(50),
--     release_year INT,
--     rating FLOAT,
--     category_name VARCHAR(50),
--     publisher_name VARCHAR(50),
--     min_players VARCHAR(50),
--     max_players VARCHAR(50)
-- );
-- CREATE OR REPLACE PROCEDURE usp_search_by_category(
--     category VARCHAR(50))
-- AS
-- $$
-- BEGIN
--     TRUNCATE TABLE search_results;
--     INSERT INTO search_results(name,
--                                release_year,
--                                rating,
--                                category_name,
--                                publisher_name,
--                                min_players,
--                                max_players)
--     SELECT
--         bg.name AS "name",
--         bg.release_year,
--         bg.rating,
--         c.name,
--         p.name,
--         CONCAT(pr.min_players, ' ', 'people') AS "min_players",
--         CONCAT(pr.max_players, ' ', 'people') AS "max_players"
--     FROM board_games AS bg
--     JOIN categories AS c
--         ON bg.category_id = c.id
--     JOIN publishers AS p
--         ON bg.publisher_id = p.id
--     JOIN players_ranges AS pr
--         ON bg.players_range_id = pr.id
--     WHERE category = c.name
--     ORDER BY
--         p.name,
--         bg.release_year DESC;
-- END;
-- $$
-- LANGUAGE plpgsql;

-- -- CALL usp_search_by_category('Wargames');
-- -- 
-- -- SELECT * FROM search_results;
