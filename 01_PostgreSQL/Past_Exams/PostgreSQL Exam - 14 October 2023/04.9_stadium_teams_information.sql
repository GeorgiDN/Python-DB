DROP FUNCTION IF EXISTS fn_stadium_team_name;
CREATE  OR REPLACE FUNCTION fn_stadium_team_name(
    IN stadium_name VARCHAR(30)
) RETURNS TABLE(details VARCHAR(40))
AS
$$
BEGIN
    RETURN QUERY
    SELECT t.name
    FROM teams AS t
    JOIN stadiums AS s
    ON s.id = t.stadium_id
    WHERE s.name = stadium_name
    ORDER BY t.name;
END;
$$
LANGUAGE plpgsql;

-- SELECT fn_stadium_team_name('BlogXS')
-- SELECT fn_stadium_team_name('Quaxo')
-- SELECT fn_stadium_team_name('Jaxworks')
