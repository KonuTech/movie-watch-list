-- Table: public.movies

-- DROP TABLE IF EXISTS public.movies;

CREATE TABLE IF NOT EXISTS public.movies
(
    --id integer NOT NULL DEFAULT nextval('movies_id_seq'::regclass),
    id SERIAL,
    title text COLLATE pg_catalog."default" NOT NULL,
    release_timestamp real NOT NULL,
    CONSTRAINT movies_pkey PRIMARY KEY (id),
    CONSTRAINT movies_title_release_timestamp_key UNIQUE (title, release_timestamp)
)
WITH (
    OIDS = FALSE
)
TABLESPACE pg_default;

ALTER TABLE IF EXISTS public.movies
    OWNER to onzwlhkt;
-- Index: idx_movies_release

-- DROP INDEX IF EXISTS public.idx_movies_release;

CREATE INDEX IF NOT EXISTS idx_movies_release
    ON public.movies USING btree
    (release_timestamp ASC NULLS LAST)
    TABLESPACE pg_default;


-- CREATE TABLE IF NOT EXISTS
--     movies (
--          id SERIAL PRIMARY KEY
--         ,title TEXT NOT NULL
--         ,release_timestamp REAL NOT NULL
--         ,UNIQUE(title, release_timestamp)
--     );
