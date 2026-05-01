import sqlite3
from movies_data import all_movies #все фильмы были перенесены с отдельного файла,где списком были все данные,которые переносятся тут в бд
conn = sqlite3.connect("film.db")
cursor = conn.cursor()
cursor.execute('''CREATE TABLE IF NOT EXISTS movies(id INTEGER PRIMARY KEY AUTOINCREMENT,genre TEXT,country TEXT,title TETX)''')
for genre in all_movies:
    for country in all_movies[genre]:
        for title in all_movies[genre][country]:
            cursor.execute("INSERT INTO movies(genre,country,title) VALUES (?,?,?)",(genre,country,title)) #забирает все данные по порядку с помощью for
conn.commit()