-- This script lists tv shows and their genres
SELECT tv_shows.title, tv_show_genres.genre_id FROM tv_shows
LEFT OUTER JOIN tv_show_genres ON tv_shows.id = tv_show_genres.show_id
WHERE tv_show_genres.genre_id IS NULL
ORDER BY title, genre_id ASC;
