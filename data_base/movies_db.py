import os
import sqlite3
from sqlite3 import Error

def create_connection(db_file):
    conn = None
    try:
        conn = sqlite3.connect(db_file)
    except sqlite3.Error as e:
        print(e)
    return conn

def execute_sql(conn, sql):
   try:
       c = conn.cursor()
       c.execute(sql)
   except Error as e:
       print(e)

def add_genre(conn, genre):
    sql = 'INSERT INTO genres(name) VALUES(?)'
    cur = conn.cursor()
    cur.execute(sql, (genre,))
    conn.commit()
    return cur.lastrowid

def add_movie(conn, title, genre_id, release_date):
    sql = 'INSERT INTO movies(title, genre_id, release_date) VALUES(?, ?, ?)'
    cur = conn.cursor()
    cur.execute(sql, (title, genre_id, release_date))
    conn.commit()
    return cur.lastrowid

def select_all(conn, table):
    cur = conn.cursor()
    cur.execute(f'SELECT * FROM {table}')
    rows = cur.fetchall()
    return rows

def select_where(conn, table, **query):
   cur = conn.cursor()
   qs = []
   values = ()
   for k, v in query.items():
       qs.append(f"{k}=?")
       values += (v,)
   q = " AND ".join(qs)
   cur.execute(f"SELECT * FROM {table} WHERE {q}", values)
   rows = cur.fetchall()
   return rows

def update(conn, table, id, **kwargs):
   parameters = [f"{k} = ?" for k in kwargs]
   parameters = ", ".join(parameters)
   values = tuple(v for v in kwargs.values())
   values += (id, )

   sql = f''' UPDATE {table}
             SET {parameters}
             WHERE id = ?'''
   try:
       cur = conn.cursor()
       cur.execute(sql, values)
       conn.commit()
   except sqlite3.OperationalError as e:
       print(e)

def delete_where(conn, table, **kwargs):
   qs = []
   values = tuple()
   for k, v in kwargs.items():
       qs.append(f"{k}=?")
       values += (v,)
   q = " AND ".join(qs)

   sql = f'DELETE FROM {table} WHERE {q}'
   cur = conn.cursor()
   cur.execute(sql, values)
   conn.commit()

create_genre_table_sql = '''
    -- genres table
    CREATE TABLE IF NOT EXISTS genres (
        id integer PRIMARY KEY,
        name text NOT NULL
    );
'''

create_movies_sql = '''
    -- movies table
    CREATE TABLE IF NOT EXISTS movies (
        id integer PRIMARY KEY,
        title text NOT NULL,
        genre_id integer NOT NULL,
        release_date text NOT NULL,
        FOREIGN KEY (genre_id) REFERENCES genres(id)
   );
   '''

db_file = 'movies.db'

# For demo purposes always create a data base from scratch.
if os.path.exists(db_file):
    os.remove(db_file)

conn = create_connection(db_file)

if conn is not None:
    execute_sql(conn, create_genre_table_sql)
    execute_sql(conn, create_movies_sql)

    animation_id = add_genre(conn, 'Animation')
    action_id = add_genre(conn, 'Action')
    horror_id = add_genre(conn, 'Horror')
    drama_id = add_genre(conn, 'Drama')
    scifi_id = add_genre(conn, 'Science Fiction')

    movie_id = add_movie(conn, 'Puss in Boots: The Last Wish', animation_id, '12/21/2022')
    movie_id = add_movie(conn, 'Black Panther: Wakanda Forever', action_id, '11/11/2022')
    movie_id = add_movie(conn, 'Knock at the Cabin', horror_id, '02/03/2023')
    movie_id = add_movie(conn, 'Die Hart', action_id, '02/24/2023')
    movie_id = add_movie(conn, 'Shark Side of the Moon', action_id, '08/12/2022')
    movie_id = add_movie(conn, 'Plane', action_id, '01/13/2023')
    movie_id = add_movie(conn, 'Prizefighter: The Life of Jem Belcher', drama_id, '07/22/2022')
    movie_id = add_movie(conn, 'The Whale', drama_id, '12/09/2022')
    movie_id = add_movie(conn, 'Creed III', drama_id, '03/03/2023')
    movie_id = add_movie(conn, 'Avatar: The Way of Water', scifi_id, '16/12/2022') # Ouch! Wrong date.
    update(conn, 'movies', movie_id, release_date = '12/16/2022') # Fix it.
    update(conn, 'movies', movie_id, genre = animation_id) # Handle error.

    delete_where(conn, 'movies', genre_id = action_id) # I don't like action movies. Delete them permanently
    delete_where(conn, 'genres', id = action_id) # ... and the action genre itself as well. :)

    all_genres = select_all(conn, 'genres')
    print ('GENRES:')
    print(all_genres)
    print()
    
    all_movies = select_all(conn, 'movies')
    print('MOVIES:')
    print(all_movies)
    print()

    drama_movies = select_where(conn, 'movies', genre_id = drama_id)
    print('DRAMA MOVIES:')
    print(drama_movies)

    conn.close()
