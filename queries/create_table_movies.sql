CREATE TABLE IF NOT EXISTS
    movies (
         id INTEGER PRIMARY KEY AUTOINCREMENT
        ,title TEXT NOT NULL
        ,release_timestamp REAL NOT NULL
        ,UNIQUE(title, release_timestamp)
    );