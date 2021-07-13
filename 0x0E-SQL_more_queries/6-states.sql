-- a script that creates the database hbtn_0d_usa
--  and the table states (in the database hbtn_0d_usa
-- states description: id INT unique, auto generated,
-- can t be null and is a primary keycan
-- name VARCHAR(256) cant be null

CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
CREATE TABLE IF NOT EXISTS hbtn_0d_usa.states(id INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
name VARCHAR(256) NOT NULL); 
