# Sparkify Database ETL using PostgreSQL and Python 3

## Overview
In this project, a new company, *Sparkify*, wants to create a database of all the songs and artists played by the users on their platform. The data is contained in two directories with files in JSON format: songs and logs. This is not easily accessible, and therefore it was decided to create an ETL (Extract, Transform, Load) pipeline and store the data in a star schema database. The database software chosen was PostgreSQL. Python was chosen as the language to extract the data from the JSON files and import it into the database. Additionally, Python is used to create the database and its associated tables. 

## Project Requirements
Using the song and log datasets, create a star schema optimized for queries on song play analysis. This includes the following tables:
Fact Table

   * songplays - records in log data associated with song plays i.e. records with page NextSong
        songplay_id, start_time, userId, level, song_id, artist_id, sessionId, location, userAgent

Dimension Tables

   * users - users in the app
        userId, firstName, lastName, gender, level
   * songs - songs in music database
        song_id, title, artist_id, year, duration
   * artists - artists in music database
        artist_id, artist_name, artist_location, artist_latitude, artist_longitude
   * time - timestamps of records in songplays broken down into specific units
        start_time, hour, day, week, month, year, weekday
        
## How to run the project
- In the console, enter the command 'run create_tables.py' to run the create_tables.py script.
- In the console, enter the command 'run etl.py' and run the script to read and process all of the files from song_data and log_data and load them into the tables.
- Run all cells in etl.ipynb to observe how the ETL process was developed for each table.
- Close the etl.ipynb by restarting the kernel, or by running conn.close() from inside the notebook.

