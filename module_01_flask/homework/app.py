import datetime
import random
from flask import Flask

app = Flask(__name__)


@app.route('/hello_word')
def hello_word():
    return "Привет Мир!"


@app.route('/cars')
def cars():
    return "Chevrolet, Renault, Ford, Lada"


@app.route('/cats')
def cats():
    cats_list = ["Корниш рекс", "Русская голубая", "Шотландская вислоухая", "Мэйн-кун", "Манчкин"]
    return random.choice(cats_list)


@app.route('/get_time/now')
def get_time_now():
    return "Точное время {}".format(datetime.datetime.now())


@app.route('/get_time/future')
def get_time_future():
    return "Точное время через час будет {}".format(datetime.datetime.now() + datetime.timedelta(hours=1))


@app.route('/get_random_word')
def get_random_word():
    global lines
    if len(lines) == 0:
        with open("war_and_peace.txt", "r", encoding="UTF-8") as war_and_peace:
            for line in war_and_peace.readlines():
                for item in line.split():
                    lines.append(item)
    return random.choice(lines)


lines = []


@app.route('/counter')
def counter():
    global count
    count += 1
    return "Текущая страница открывалась: {} раз".format(count)


count = 0
