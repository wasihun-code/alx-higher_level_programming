-- Lists all the tables of a database
-- database name will be passed as argument of mysql command
SET @DB='$1';
SELECT * FROM '@Db';
