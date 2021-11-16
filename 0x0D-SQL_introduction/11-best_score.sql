-- lists all recoreds of second table hbtn_0c_0 database
-- records ordered by score top first
SELECT score, name FROM second_table WHERE score >= 10 ORDER BY score DESC;
