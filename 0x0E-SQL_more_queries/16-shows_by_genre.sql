-- This script lists all movies and their genre
SELECT title, name FROM tv_show_genres
JOIN tv_shows ON tv_shows.id = tv_show_genres.show_id
JOIN tv_genres ON tv_genres.id = tv_show_genres.genre_id
ORDER BY title, name;
