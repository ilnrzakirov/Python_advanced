import datetime
import random
from flask import Flask

app = Flask(__name__)


@app.route('/hello_word')
def test_function():
   return "Привет Мир!"


@app.route('/cars')
def test_function():
   return "Chevrolet, Renault, Ford, Lada"


@app.route('/cats')
def test_function():
   cats = ["Корниш рекс", "Русская голубая", "Шотландская вислоухая", "Мэйн-кун", "Манчкин"]
   return random.choice(cats)


@app.route('/get_time/now')
def test_function():
   return "Точное время {}".format(datetime.datetime.now())


@app.route('/get_time/future')
def test_function():
   return "Точное время через час будет {}".format(datetime.datetime.now() + datetime.timedelta(hours=1))


@app.route('/get_random_word')
def test_function():
   with open("war_and_peace.txt", "r", encoding="UTF-8") as war_and_peace:
      lines = []
      for line in war_and_peace.readlines():
         lines.append(line.split())
   return random.choice(lines)

@app.route('/counter')
def counter():
   class Counter:
      def __init__(self):
         self.counter = 0

      def new_visit(self):
         self.counter += 1
         return self.counter

   counter = Counter()
   print("Текущая страница открывалась: {} раз".format(counter.new_visit()))


