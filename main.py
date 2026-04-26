import requests 
mood=input("Какое у вас настроение?")
if mood in["грустно", "печально","уныло", "мрачно", "тоскливо", "нерадостно"]:
  print("Советую вам посмотреть комедию")
  film_choice1=input("Помочь вам выбрать подходящий фильм?")
  if film_choice1 == "да":
    key="667d4f7a-8588-4444-a536-1e66c759089f"
    url1="https://kinopoiskapiunofficial.tech"
    result = requests.get(url,headers={"X-API-KEY": key})
    data = result.json()
