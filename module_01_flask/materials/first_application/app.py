import datetime
from flask import Flask

app = Flask(__name__)

@app.route('/hello')
def test_function():
   return 'Это тестовая страничка, ответ сгенерирован в %s' % \
                     datetime.datetime.now().utcnow()

@app.route('/test')
def hello():
   return 'Привет мир'