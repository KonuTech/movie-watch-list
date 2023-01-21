SELECT
    *
FROM
    movies
WHERE
    release_timestamp > %s
;