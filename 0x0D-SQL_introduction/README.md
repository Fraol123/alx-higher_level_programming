# SQL - Introduction

- Database
	A database is an organised collection of related 
  	data from which you can easily retrieve and use data.

- Relational Database
  	     Tables are structured related to each other
  	     Each specific type of domain data is strored
  	     it's own table

- SQL
	stands for Structured Query Language

- MYSQL
	MySQL is an open source DBMS which is built, 
  	supported and distributed by MySQL(ORACLE). 

- how to create database in MYSQL
      MySQL implements a database as a directory that 
      contains all files which correspond to tables in the database.

-  To create a new database in MySQL, you use the 
      ```
      CREATE DATABASE statement with the following syntax:

      CREATE DATABASE [IF NOT EXISTS] database_name
      [CHARACTER SET charset_name]
      [COLLATE collation_name]
      ```
- DDl stands for Data Definition language and DML
      Data Manipulation language

- create or alter table
  	 ```
	 ALTER TABLE table_name

	 ADD column_name datatype; 
	 ```

- selecting data from a table
  	    ```
	    SELECT column1, column2, ...
	    FROM table_name; 

	    or 

	    SELECT* FROME name
	    ```

- Subquaries
	A Subquery or Inner query or a Nested query is 
  	a query within another SQL query and embedded 
  	within the WHERE clause.