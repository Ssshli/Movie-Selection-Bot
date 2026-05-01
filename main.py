
import sqlite3
conn = sqlite3.connect("film.db")     #создаю соединение с файлом бд
cursor = conn.cursor()     #создаю библиотекаря cursor
while True:       #Использую для работы цикла, чтобы после окончания вопроса был возврат
  g=input('Здравствуйте!Хотите посмотреть или добавить фильм?').lower()
  if g =='добавить':
    new_genre=input("Введите жанр").lower()
    new_country=input("Введите страну").capitalize()
    new_title=input("Введите название")
    cursor.execute("INSERT INTO movies(genre,country,title)VALUES(?,?,?)",(new_genre,new_country,new_title))  #рабочий cursor добавляет названия жанра,страны,названия в базу данных,после введенных данных
    print("Добавил,спасибо!")
    conn.commit() #все новые фильмы сохранятся в бд
  elif g=="посмотреть":
    genre=input("Какой жанр фильма хотите посмотреть?").lower()
    country=input("Выберите страну:Россия,США,Франция,Германия.Прошу с заглавной буквы. ")
    cursor.execute("SELECT title FROM movies WHERE genre=? and country=? ORDER BY RANDOM()",(genre,country)) #по сравнению с другой операцией, тут cursor ищет в бд данные
    film=cursor.fetchone()     #рандомом выбирается фильм из-за ORDER BY RANDOM()
    if film:
      print(f"Приятного просмотра! Советую: {film[0]}")
    else:
      print("Извините! Я ничего не нашел")
  else:
    print("Извините, не понимаю вас")
  while True:
    question=input("Хотите выбрать еще один фильм?").strip()
    if question == "нет":
      print("Хорошо! Обращайтесь за помощью!")
      exit()
    elif question == "да": #после ответа программа откатывается назад на 1 вопрос
      break
    else:
      print("Извините,я не понимаю")