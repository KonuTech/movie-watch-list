import datetime
import sqlite3


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


connection = sqlite3.connect(".//db//data.db")


def create_table():
    with connection:
        connection.execute(
            CREATE_MOVIES_TABLE
        )
        connection.execute(
            CREATE_USERS_TABLE
        )
        connection.execute(
            CREATE_WATCHED_TABLE
        )
        connection.execute(
            CREATE_RELEASE_INDEX
        )


def add_user(username):
    try:
        with connection:
            connection.execute(INSERT_USER, (username,))
    except:
        print("UNIQUE constraint failed: users.username")
        pass


def add_movie(title, release_timestamp):
    with connection:
        connection.execute(
            INSERT_MOVIE, (title, release_timestamp)
        )


def get_movies(upcoming=False):
    with sqlite3.connect(".//db//data.db") as connection:
        cursor = connection.cursor()
        if upcoming:
            today_timestamp = datetime.datetime.today().timestamp()
            cursor.execute(
                SELECT_UPCOMING_MOVIES, (today_timestamp,)
            )
        else:
            cursor.execute(
                SELECT_ALL_MOVIES
            )

        return cursor.fetchall()


def search_movies(search_term):
    with connection:
        cursor = connection.cursor()
        cursor.execute(SEARCH_MOVIES, (f"%{search_term}%",))

        return cursor.fetchall()


def watch_movie(username, movie_id):
    try:
        with connection:
            connection.execute(
                INSERT_WATCHED_MOVIE, (username, movie_id)
            )
    except:
        print("UNIQUE constraint failed: users.username")
        pass


def get_watched_movies(username):
    with connection:
        cursor = connection.cursor()
        cursor.execute(
            SELECT_WATCHED_MOVIES, (username, )
        )

        return cursor.fetchall()
