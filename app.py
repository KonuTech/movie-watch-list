import datetime
import database


menu = """
Please select one of the following options:
1) Add User to the App
2) Add new movie
3) View all movies
4) View upcoming movies
5) Search for a movie
6) Watch a movie
7) View watched movies
8) Exit

Your selection:\n
"""
welcome = "Welcome to the watchlist app!"


def prompt_add_movie():
    title = input("Movie title: ")
    release_date = input("Release date (dd-mm-YYYY): ")
    parsed_date = datetime.datetime.strptime(release_date, "%d-%m-%Y")
    timestamp = parsed_date.timestamp()
    database.add_movie(title, timestamp)


def print_movie_list(heading, movies):
    print(f"-- {heading} movies --")
    for _id, title, release_date in movies:
        movie_date = datetime.datetime.fromtimestamp(release_date)
        human_date = movie_date.strftime("%b %d %Y")
        print(f"{_id}: {title} (on {human_date})")
    print("----\n")


def prompt_watch_movie():
    username = input("Username: ")
    movie_id = input("Movie ID: ")
    database.watch_movie(username, movie_id)


def prompt_show_watched_movies():
    username = input("Username: ")
    movies = database.get_watched_movies(username)
    if movies:
        print_movie_list(f"Watched: ", movies)
    else:
        print("That user has watched no movies yet!")


def prompt_search_movies():
    search_term = input("Enter the partial movie title: ")
    movies = database.search_movies(search_term)
    if movies:
        print_movie_list("Movies found", movies)
    else:
        print("Found no movies for that search term!")


def prompt_add_user():
    username = input("Username: ")
    database.add_user(username)


print(welcome)
database.create_table()


while (user_input := input(menu)) != "8":
    if user_input == "1":
        prompt_add_user()
    elif user_input == "2":
        prompt_add_movie()
    elif user_input == "3":
        upcoming_movies = database.get_movies()
        print_movie_list("All", upcoming_movies)
    elif user_input == "4":
        upcoming_movies = database.get_movies(True)
        print_movie_list("Upcoming", upcoming_movies)
    elif user_input == "5":
        prompt_search_movies()
    elif user_input == "6":
        prompt_watch_movie()
    elif user_input == "7":
        prompt_show_watched_movies()
    else:
        print("Invalid input, please try again!")
