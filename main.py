import random
from movies_data import all_movies
while True:
  genre=input("Здравствуйте! Какой  жанр фильма вы хотите посмотреть?").lower()
  country=input("Выберите страну из предложенных:Россия,США,Франция,Германия,.Прошу заметить, что фильмы представлены на платформе Кинопоиск, поиск фильмов ведется оттуда.")
  if genre in all_movies and country in all_movies[genre]:
    film=random.choice(all_movies[genre][country])
    print(f"Приятного просмотра!:{film}")
  else:
    print("Извините! Я не знаю такого жанра/фильма, попробуйте ввести действительный жанр и название страны с заглавной буквой")
  question=input("Хотите выбрать еще один фильм?").strip()
  if question == "нет":
    print("Хорошо! Обращайтесь за помощью!")
    break