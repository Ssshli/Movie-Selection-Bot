from flask import Flask, render_template, request  #подключаю движок сайта,шаблоны и работы с данными
import random
from movies_data import all_movies
app=Flask(__name__)                                #создание веб-приложения
@app.route('/', methods=['GET','POST'])                                    # @app обращение к приложению, .route говорю об адресе, а ('/')- сам адрес
def index():
    recommendation=None
    if request.method=='POST':
        genre=request.form.get('genre').lower().strip() 
        country=request.form.get('country').capitalize().strip()
        print(f"Ищу жанр:'{genre}' и страну:'{country}'")
        if genre in all_movies and country in all_movies[genre]:
            recommendation=random.choice(all_movies[genre][country])
        else:
            recommendation=("Извините! Данные отсутствуют,попробуйте снова")
    return render_template('index.html', result=recommendation)            
if __name__=='__main__':
    app.run(debug=True)