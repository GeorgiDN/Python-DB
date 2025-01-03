DROP PROCEDURE IF EXISTS udp_awarded_production;
CREATE OR REPLACE PROCEDURE udp_awarded_production(
    production_title VARCHAR(70)
) AS
$$
BEGIN
    UPDATE actors
    SET awards = awards + 1
    WHERE id IN (
        SELECT
            pa.actor_id
        FROM
            productions_actors AS pa
        JOIN
            productions AS p
        ON
            pa.production_id = p.id
        WHERE
            production_title LIKE p.title);
END;
$$
LANGUAGE plpgsql;

-- -- CALL udp_awarded_production('Tea For Two');
