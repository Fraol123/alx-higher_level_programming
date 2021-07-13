-- lists all genres from hbtn_0d_tvshows and displays the number of shows linked to each
-- Each record should display: tv_geners.name - number of shows
-- Don't display a genere that doesn't have any shows linked
-- Results must be sorted in descending order by the number of shows linked 
-- You can use only SELECT statement
-- The database name will be passed as an argument of the mysql command

SELECT tv_genres.name AS genre, COUNT(*) AS number_shows
FROM tv_genres
INNER JOIN tv_show_genres
ON tv_genres.id=tv_show_genres.genre_id
GROUP BY tv_show_genres.genre_id
ORDER BY number_shows DESC;
