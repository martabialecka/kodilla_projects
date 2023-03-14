import sqlite3
from sqlite3 import Error

def create_connection(movies_file):
    conn = None
    try:
        conn = sqlite3.connect(movies_file)
        return conn
    except sqlite3.Error as e:
        print(e)
    return conn

def execute_sql(conn, sql):
   try:
       c = conn.cursor()
       c.execute(sql)
   except Error as e:
       print(e)

def add_movie(conn, movie):
    sql = '''INSERT INTO movies(title, genre, production_date)
            VALUES(?,?,?)'''
    cur = conn.cursor()
    cur.execute(sql,movie)
    conn.commit()
    return cur.lastrowid

def add_actor(conn, actor):
    sql = '''INSERT INTO actors (movies_id, name, surname, age)
            VALUES(?,?,?,?)'''
    cur = conn.cursor()
    cur.execute(sql, actor)
    conn.commit()
    return cur.lastrowid

def select_all(conn, table):
   cur = conn.cursor()
   cur.execute(f"SELECT * FROM {table}")
   rows = cur.fetchall()

   return rows

if __name__ == "__main__":
    create_movies_sql = """
   -- movies table
   CREATE TABLE IF NOT EXISTS movies (
      id integer PRIMARY KEY,
      title text NOT NULL,
      genre text,
      production_date text
   );
   """
create_actors_sql = """
   -- zadanie table
   CREATE TABLE IF NOT EXISTS actors (
      id integer PRIMARY KEY,
      movies_id integer NOT NULL,
      name VARCHAR(250) NOT NULL,
      surname TEXT,
      age NOT NULL,
      FOREIGN KEY (movies_id) REFERENCES movies (id)
   );
   """

conn = create_connection("movies.db")
if conn is not None:
    execute_sql(conn, create_movies_sql)
    execute_sql(conn, create_actors_sql)

movie = ("Inception", "SF", "2010")

movie_id = add_movie(conn, movie)

movie = ("Forrest Gump", "Drama", "1994")

movie_id = add_movie(conn, movie)

actor = (
        movie_id,
        "Leonardo",
        "DiCaprio",
        "48",
    )

actor_id = add_actor(conn, actor)

actor = (
        movie_id,
        "Joseph",
        "Gordon",
        "42",
    )

actor_id = add_actor(conn, actor)

print(movie_id, actor_id)
conn.commit()
conn.close()
