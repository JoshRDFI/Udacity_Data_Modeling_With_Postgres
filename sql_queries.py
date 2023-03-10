# DROP TABLES

songplay_table_drop = "DROP TABLE IF EXISTS songplays"
user_table_drop = "DROP TABLE IF EXISTS users"
song_table_drop = "DROP TABLE IF EXISTS songs"
artist_table_drop = "DROP TABLE IF EXISTS artists"
time_table_drop = "DROP TABLE IF EXISTS time"

# CREATE TABLES

user_table_create = ("""
CREATE TABLE IF NOT EXISTS users (
    userId int PRIMARY KEY,
    firstName varchar NOT NULL,
    lastName varchar NOT NULL,
    gender char(1),
    level varchar NOT NULL
);
""")

artist_table_create = ("""
CREATE TABLE IF NOT EXISTS artists (
    artist_id varchar PRIMARY KEY,
    artist_name varchar NOT NULL,
    artist_location varchar,
    artist_latitude double precision,
    artist_longitude double precision
);
""")

song_table_create = ("""
CREATE TABLE IF NOT EXISTS songs (
    song_id varchar PRIMARY KEY,
    title varchar NOT NULL,
    artist_id varchar NOT NULL,
    year int NOT NULL,
    duration numeric NOT NULL
);
""")

songplay_table_create = ("""
CREATE TABLE IF NOT EXISTS songplays (
    songplay_id serial PRIMARY KEY,
    start_time timestamp NOT NULL,
    userId int NOT NULL REFERENCES users (userId),
    level varchar,
    song_id varchar REFERENCES songs (song_id),
    artist_id varchar REFERENCES artists (artist_id),
    session_id int NOT NULL,
    location varchar,
    user_agent varchar
);
""")

time_table_create = ("""
CREATE TABLE IF NOT EXISTS time (
    start_time timestamp PRIMARY KEY NOT NULL,
    hour int NOT NULL,
    day int NOT NULL,
    week int NOT NULL,
    month int NOT NULL,
    year int NOT NULL,
    weekday int NOT NULL
);
""")

# INSERT RECORDS

user_table_insert = ("""
INSERT INTO users (
    userId, 
    firstName, 
    lastName, 
    gender, 
    level)
VALUES (%s, %s, %s, %s, %s)
ON CONFLICT (userId)
DO UPDATE
    SET level = users.level
""")

artist_table_insert = ("""
INSERT INTO artists (
    artist_id, 
    artist_name, 
    artist_location, 
    artist_latitude, 
    artist_longitude)
VALUES (%s, %s, %s, %s, %s)
 ON CONFLICT (artist_id)
 DO NOTHING
""")

song_table_insert = ("""
INSERT INTO songs (
    song_id, 
    title, 
    artist_id, 
    year, 
    duration)
VALUES (%s, %s, %s, %s, %s)
ON CONFLICT (song_id)
DO NOTHING
""")

songplay_table_insert = ("""
INSERT INTO songplays (
    songplay_id, 
    start_time, 
    userId, 
    level, 
    song_id, 
    artist_id, 
    session_id, 
    location, 
    user_agent)
VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
ON CONFLICT (songplay_id)
DO NOTHING
""")

time_table_insert = ("""
INSERT INTO time (
    start_time, 
    hour, 
    day, 
    week, 
    month, 
    year, 
    weekday)
VALUES (%s, %s, %s, %s, %s, %s, %s)
ON CONFLICT (start_time)
DO NOTHING
""")

# FIND SONGS

song_select = ("""
SELECT song_id, songs.artist_id 
FROM songs 
JOIN artists ON artists.artist_id = songs.artist_id
WHERE title = %s
AND artist_name = %s
AND duration = %s;
""")

# QUERY LISTS

create_table_queries = [user_table_create, artist_table_create, song_table_create, songplay_table_create, time_table_create]
drop_table_queries = [user_table_drop, artist_table_drop, song_table_drop, songplay_table_drop, time_table_drop]