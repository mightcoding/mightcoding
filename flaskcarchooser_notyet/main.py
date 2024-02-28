#Импорт
from flask import Flask, render_template


app = Flask(__name__)

def car_image(page, lights):
    #Переменные для энергозатратности приборов
    if page == 1: 
        if lights == 1:
            return "../static/img/subaru.png"
        elif lights == 2:
            return "../static/img/audi.png"
        elif lights == 3:
            return "../static/img/911.png"
    if page == 1: 
        if lights == 1:
            return "../static/img/subaru.png"
        elif lights == 2:
            return "../static/img/audi.png"
        elif lights == 3:
            return "../static/img/911.png"



#Первая страница
@app.route('/')
def index():
    return render_template('index.html')

#Вторая страница
@app.route('/<page>')
def lights(page):
    return render_template(
                            'lights.html', 
                            page=page
                           )

#Третья страница
@app.route('/<page>/<lights>')
def electronics(page, lights):
    return render_template(
                            'end.html',
                            image = car_image(int(page),
                                              int(lights)),
                            page = page, 
                            lights = lights                           
                           )


app.run(debug=True)
