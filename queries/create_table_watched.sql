-- Table: public.watched

-- DROP TABLE IF EXISTS public.watched;

CREATE TABLE IF NOT EXISTS public.watched
(
    user_username text COLLATE pg_catalog."default" NOT NULL,
    movie_id integer NOT NULL,
    CONSTRAINT watched_pkey PRIMARY KEY (user_username, movie_id),
    CONSTRAINT watched_movie_id_fkey FOREIGN KEY (movie_id)
        REFERENCES public.movies (id) MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION,
    CONSTRAINT watched_user_username_fkey FOREIGN KEY (user_username)
        REFERENCES public.users (username) MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION
)
WITH (
    OIDS = FALSE
)
TABLESPACE pg_default;

ALTER TABLE IF EXISTS public.watched
    OWNER to onzwlhkt;


-- CREATE TABLE IF NOT EXISTS watched (
--      user_username TEXT NOT NULL
--     ,movie_id INTEGER NOT NULL
--     ,PRIMARY KEY (user_username, movie_id)
--     ,FOREIGN KEY (user_username) REFERENCES users(username)
--     ,FOREIGN KEY (movie_id) REFERENCES movies(id)
--     );
