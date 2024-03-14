-- Retrieve all genres from the database hbtn_0d_tvshows along with the count
-- of shows associated with each genre.
-- Exclude genres that do not have any associated shows.
-- Arrange the records in descending order based on the count of associated shows.

SELECT tv_genres.name AS genre,
	COUNT(*) AS number_of_shows
	FROM tv_genres
	INNER JOIN tv_show_genres
	ON tv_genres.id = tv_show_genres.genre_id
GROUP BY tv_genres.name
ORDER BY number_of_shows DESC;
