import os
import datetime
import psycopg2

from dotenv import load_dotenv

load_dotenv()

CREATE_MOVIES_TABLE = open(".//queries//create_table_movies.sql", 'r').read()
CREATE_USERS_TABLE = open(".//queries//create_table_users.sql", 'r').read()
CREATE_WATCHED_TABLE = open(".//queries//create_table_watched.sql", 'r').read()
INSERT_MOVIE = open(".//queries//insert_movie.sql", 'r').read()
INSERT_USER = open(".//queries//insert_user.sql", 'r').read()
SELECT_ALL_MOVIES = open(".//queries//select_all_movies.sql", 'r').read()
SELECT_UPCOMING_MOVIES = open(".//queries//select_upcoming_movies.sql", 'r').read()
SELECT_WATCHED_MOVIES = open(".//queries//select_watched_movies.sql", 'r').read()
INSERT_WATCHED_MOVIE = open(".//queries//insert_watched_movie.sql", 'r').read()
SET_WATCHED_MOVIE = open(".//queries//set_watched_movie.sql", 'r').read()
SEARCH_MOVIES = open(".//queries//search_movies.sql", 'r').read()
CREATE_RELEASE_INDEX = open(".//queries//create_release_index.sql", 'r').read()

conn = psycopg2.connect(os.environ["DATABASE_URL"])


def create_table():
    with conn:
        with conn.cursor() as curs:
            curs.execute(
                CREATE_MOVIES_TABLE
            )
            curs.execute(
                CREATE_USERS_TABLE
            )
            curs.execute(
                CREATE_WATCHED_TABLE
            )
            curs.execute(
                CREATE_RELEASE_INDEX
            )


def add_user(username):
    try:
        with conn:
            with conn.cursor() as curs:
                curs.execute(INSERT_USER, (username,))
    except Exception:
        print("UNIQUE constraint failed: users.username")
        pass


def add_movie(title, release_timestamp):
    with conn:
        with conn.cursor() as curs:
            curs.execute(
                INSERT_MOVIE, (title, release_timestamp)
            )


def get_movies(upcoming=False):
    with conn:
        with conn.cursor() as curs:
            if upcoming:
                today_timestamp = datetime.datetime.today().timestamp()
                curs.execute(
                    SELECT_UPCOMING_MOVIES, (today_timestamp,)
                )
            else:
                curs.execute(
                    SELECT_ALL_MOVIES
                )

            return curs.fetchall()


def search_movies(search_term):
    with conn:
        with conn.cursor() as curs:
            curs.execute(SEARCH_MOVIES, (f"%{search_term}%",))

            return curs.fetchall()


def watch_movie(username, movie_id):
    try:
        with conn:
            with conn.cursor() as curs:
                curs.execute(
                    INSERT_WATCHED_MOVIE, (username, movie_id)
                )
    except Exception:
        print("UNIQUE constraint failed: users.username")
        pass


def get_watched_movies(username):
    with conn:
        with conn.cursor() as curs:
            curs.execute(
                SELECT_WATCHED_MOVIES, (username,)
            )

            return curs.fetchall()
