-- shows and genre!
-- select show.title, genre.name from joined tables
SELECT tv_shows.title, tv_genres.name FROM tv_shows
JOIN tv_show_genres ON tv_show_genres.show_id = tv_shows.id
JOIN tv_genres ON tv_show_genres.genre_id = tv_genres.id
ORDER BY title, name;
