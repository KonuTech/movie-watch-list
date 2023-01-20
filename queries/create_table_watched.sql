CREATE TABLE IF NOT EXISTS watched (
     user_username TEXT NOT NULL
    ,movie_id INTEGER NOT NULL
    ,PRIMARY KEY (user_username, movie_id)
    ,FOREIGN KEY (user_username) REFERENCES users(username)
    ,FOREIGN KEY (movie_id) REFERENCES movies(id)
    );