SELECT
    m.*
FROM
    movies AS m
INNER JOIN watched as w ON
    m.id = w.movie_id
INNER JOIN users as u ON
    w.user_username = u.username
WHERE
    u.username = %s
;