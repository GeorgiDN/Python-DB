CREATE TABLE IF NOT EXISTS gift_recipients (
    id SERIAL PRIMARY KEY,
    name VARCHAR(50),
    country_id INT,
    gift_sent BOOLEAN DEFAULT FALSE
);

INSERT INTO gift_recipients(name, country_id, gift_sent)
(SELECT
    CONCAT(c.first_name, ' ', c.last_name),
    c.country_id,
    CASE WHEN c.country_id IN (7, 8, 14, 17, 26) THEN TRUE
    ELSE FALSE
    END
FROM
    customers AS c
);




-- CREATE TABLE IF NOT EXISTS gift_recipients (
--   id SERIAL PRIMARY KEY,
--   name VARCHAR(100) NOT NULL,
--   country_id INT NOT NULL,
--   gift_sent BOOLEAN DEFAULT FALSE
-- );


-- INSERT INTO gift_recipients (
-- 	name, country_id, gift_sent
-- )
-- SELECT
--   CONCAT(first_name, ' ', last_name) AS name,
--   country_id AS country_id,
--   CASE
--     WHEN country_id IN (7, 8, 14, 17, 26) THEN TRUE
--     ELSE FALSE
--   END AS gift_sent
-- FROM customers;
