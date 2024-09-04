
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

# ? to select all from a table to view what that table contains
# SELECT * FROM [table_name];

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