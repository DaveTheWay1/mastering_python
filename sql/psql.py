
# * enter in termial to start: psql
# upon succful entry youll see:
# psql (14.11 (Homebrew))
# Type "help" for help.

# davidramirez=# 

# * Creating a Database and a Table
# ? Let’s create a database named music and a bands table:
# CREATE DATABASE music; -- Don't forget the semicolon!

# ? To list all databases that already exist: 
# use the \list meta-command or its shortcut \l

# ? to create a database:
# CREATE DATABASE databasename;

#  ! if the databse already exists and you wish to delete: 
# DROP DATABASE [database_name];

# ? to connect to a database:
#  \c [database_name]     no ";" needed for this command line
# . ** if you only do \c without the database name you will connect to the first existing database

# ? how to see the current database that you are using?
# SELECT current_database();
# no need to switch out to go to another, simply repeat the step with the new database name

# ? to list all tables and sequences:
# \d

# ? to list all tables only
# \dt

# ? -- Ex: Define a table's schema. In other words, an example of create a table.
# CREATE TABLE bands (
#   id serial PRIMARY KEY,  -- serial is auto-incrementing integer
#   name varchar NOT NULL,
#   genre varchar
# );

# ? to see details of a specific table:
#  \d table_name

# OR

# ? to select all from a table to view what that table contains
# SELECT * FROM [table_name];

# THE DIFFERENCE IS select * will show you the fields and \d table_name will show datatype fields

# * Basic Querying and Inserting Data

# ? how to show everything found within a table
# first be insde the database that table belonds to
# SELECT * FROM [table_name]; -- The * represents all fields

# ? how to insert a value into a single field
# ! For text, use single quotes, not double

# INSERT INTO [database_name] ([field_name]) VALUES ([value]);  
# . ** the [] are to not be included. only directly what is being asked inside them
# ex: INSERT INTO bands (name) VALUES ('The Smiths');

# ? how to insert a value into more than one field
# INSERT INTO database_name (field_name_0, field_name_1 ) VALUES (value_for_field_0, value_for_field_1);
# ex: INSERT INTO bands (name, genre) VALUES ('Rush', 'prog rock');

# * output for the command lines above:
#  id |    name    |   genre   
# ----+------------+-----------
#   1 | The Smiths | 
#   2 | Rush       | prog rock
# (2 rows)

# * Creating a Table for a Related Data Entity

# exmaple of relating tables:
# Let’s say we have the following data relationship: Band ---< Musician

# A Band has many Musicians, and
# a Musician belongs to a Band

# ! Whenever you have a one:many relationship like above, 
# the rows in the table for the many-side must include a column 
# that references which row in the table on the one-side it belongs to.

# in the exmaple above, musicians being the many side should contain a relating factor to the Band being the one side of the relationship.
# the primary key of the one side should be added as foreign to to the many side

# * creating the relating table exmaple:
# CREATE TABLE musicians (
#   id serial PRIMARY KEY,
#   name varchar NOT NULL,
#   quote text,
#   band_id integer NOT NULL REFERENCES bands (id)
# );

# * ^ The REFERENCES constraint is what makes a column a FK.

# ? ex: what would happen if we submit something invalid as the FK
# let’s attempt to add a musician with a bogus foreign key:

# INSERT INTO musicians (name, band_id) VALUES ('Geddy Lee', 999);
# --- The above command will fail because there's no matching PK in the bands table
# output: 
# ERROR:  insert or update on table "musicians" violates foreign key constraint "musicians_band_id_fkey"
# DETAIL:  Key (band_id)=(999) is not present in table "bands".

# ! As mentioned previously, instead of referencing a number that does not exist causing an error, 
# ! reference a key that does exist 

# ? ex: 
# -- Assuming 'The Smiths' has an id of 1
# INSERT INTO musicians (name, band_id) VALUES ('Geddy Lee', 1);

# ? to then view the added values if added correctly:
# SELECT * FROM musicians;  -- There's Geddy!
# output:
#  id |   name    | quote | band_id 
# ----+-----------+-------+---------
#   2 | Geddy Lee |       |       1
# (1 row)

# ? INSERTing a TEXT with an apostrophe HOW
# -- Use two single quotes to embed an apostrophe
# EX: 

# INSERT INTO musicians (name, quote, band_id)
# VALUES (
# 'Neil Peart',
# 'If you''ve got a problem, take it out on a drum',
# 2);

# ** 👀 It’s possible to insert multiple rows by providing comma separated value lists:
# ...VALUES ('Geddy Lee', 2), ('Neil Peart', 2);

# * Querying Data using a JOIN Clause
# The JOIN clause is used with a SELECT to query for data from more than one table.

# ? Let’s query for all of the bands with their musicians:
# -- table right of JOIN has the FKs
# SELECT * FROM bands JOIN musicians ON bands.id = musicians.band_id;

# .** output: 
#  id |    name    |   genre   | id |    name    |                     quote                      | band_id 
# ----+------------+-----------+----+------------+------------------------------------------------+---------
#   1 | The Smiths |           |  2 | Geddy Lee  |                                                |       1
#   2 | Rush       | prog rock |  3 | Neil Peart | If you've got a problem, take it out on a drum |       2
# (2 rows)

# ! Note that no records are returned for bands without any musicians. 
# This is called an # * INNER JOIN, which is the default.

# ? LEFT JOIN
# If we want to return all bands, regardless of whether or not there’s any matches for musicians
# EX:
# SELECT * FROM bands LEFT JOIN musicians on bands.id = musicians.bands_id;

# * Querying Data using a WHERE Clause
# The WHERE clause allows selecting records that meet a condition or conditions:
# ex:
# SELECT *
# FROM bands b
# LEFT JOIN musicians m ON b.id = m.band_id
# WHERE b.name = 'Rush' AND m.name LIKE 'G%';

# * the LIKE operator uses:
# % to match any number of characters (wildcard)
# _ to match any single character

# * Updating Data
# ex: 
# UPDATE musicians SET quote = 'I love to write, it''s my first love.' WHERE name = 'Geddy Lee';

# * Deleting Data
# Be careful with this command because if you don’t use a WHERE clause, 
# you can accidentally delete all of the data from a table:

# SELECT * FROM bands;
# DELETE FROM bands WHERE name LIKE '%Smiths';
# SELECT * FROM bands;

# SQL - Summary
# As much fun as it is to write SQL, most developers don’t have many opportunities to do so because 
# they typically software known as an Object Relational Mapper (ORM) to automatically write SQL and 
# communicate with the database server.

# ? What happens if you get an error like in the below? 
# music=# DELETE FROM bands WHERE name LIKE '%Smiths%';
# ERROR:  update or delete on table "bands" violates foreign key 
# constraint "musicians_band_id_fkey" on table "musicians"
# DETAIL:  Key (id)=(1) is still referenced from table "musicians".

# * WHEN YOU TRY TO DELETE WHEN THERE IS AN ACTIVE FOREIGN KEY CONSTRAINT
# you have 2 options:
# you either delete the the row from the other table causing the restraint 
# OR
# We can update the 

# * EXAMPLE
# SELECT * FROM musicians LEFT JOIN bands on musicians.band_id = bands.id; 
#  id |    name    |                     quote                      | band_id | id |    name    |   genre   
# ----+------------+------------------------------------------------+---------+----+------------+-----------
#   3 | Neil Peart | If you've got a problem, take it out on a drum |       2 |  2 | Rush       | prog rock
#   6 | Mow        | I got the Meowies                              |       2 |  2 | Rush       | prog rock
#   2 | Geddy Lee  | I love to write, it's my first love.           |       1 |  1 | The Smiths | 
# (3 rows)

# DELETE FROM musicians WHERE name LIKE '%Geddy%';
# DELETE 1

# SELECT * FROM musicians;
#  id |    name    |                     quote                      | band_id 
# ----+------------+------------------------------------------------+---------
#   3 | Neil Peart | If you've got a problem, take it out on a drum |       2
#   6 | Mow        | I got the Meowies                              |       2
# (2 rows)

# SELECT * FROM bands LEFT JOIN musicians ON bands.id = musicians.band_id;
#  id |    name    |   genre   | id |    name    |                     quote                      | band_id 
# ----+------------+-----------+----+------------+------------------------------------------------+---------
#   2 | Rush       | prog rock |  3 | Neil Peart | If you've got a problem, take it out on a drum |       2
#   2 | Rush       | prog rock |  6 | Mow        | I got the Meowies                              |       2
#   1 | The Smiths |           |    |            |                                                |        
# (3 rows)

# DELETE FROM bands WHERE name LIKE '%Smiths%';
# DELETE 1
# music=# SELECT * FROM bands;
#  id | name |   genre   
# ----+------+-----------
#   2 | Rush | prog rock
# (1 row)


# !!!!! CASCADE, WE AVOID IT BECAUSE IT IS CONSIDERED BAD PRACTICE!!!!!!
# why? bc you always want to have full control of your data and know what exactly you are deleting


# (1) A relational database contains a _________ for each data entity/resource that an application has.
# table
# (2) True or False: In a relational database, all of the data in a particular column in a table must be of the same data type.
# True
# (3) A single instance of a data entity, e.g., Band, is represented by a ______ in a table.
# row
# (4) _____ is the "programming" language used by relational databases.
# Structured Query Language (SQL)