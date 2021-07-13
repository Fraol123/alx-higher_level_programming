-- a script that creates the database hbtn_0d_usa and the table
--  cities (in the database hbtn_0d_usa)
--  cities description: 
--            id INT unique, auto generated, 
--            cant be null and is a primary key
--            state_id INT, cant be null and must be a FOREIGN KEY 
--            that references to id of the states tablecan
--            name VARCHAR(256) cant be nullcan

CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
CREATE TABLE IF NOT EXISTS hbtn_0d_usa.cities(id INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
state_id INT NOT NULL,
name VARCHAR(256) NOT NULL,
FOREIGN KEY(state_id) REFERENCES hbtn_0d_usa.states(id)); 
