-- creates second_table and add multiple rows
CREATE TABLE IF NOT EXISTS second_table
(`id` INT, `name` VARCHAR(256), `score` INT);
INSERT INTO first_table (id, name, score) VALUES (1, "John", 10);
INSERT INTO first_table (id, name, score) VALUES (2, "Alex", 3);
INSERT INTO first_table (id, name, score) VALUES (3, "Bob", 14);
INSERT INTO first_table (id, name, score) VALUES (4, "George", 8);