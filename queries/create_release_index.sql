CREATE INDEX IF NOT EXISTS
    idx_movies_release ON movies (
        release_timestamp
    );