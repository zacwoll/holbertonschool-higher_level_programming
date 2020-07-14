-- This script gets the number of shows by genre
-- Select the name and number of shows
SELECT name AS genre, COUNT(show_id) AS number_of_shows FROM tv_genres
-- Join the genres table based on id
JOIN tv_show_genres ON genre_id = tv_genres.id
-- Group the genres together and sort by number of shows
GROUP BY genre ORDER BY number_of_shows DESC;
