"""
Напишите  hello-world endpoint , который возвращал бы строку "Привет, <имя>. Хорошей пятницы!".
Вместо хорошей пятницы, endpoint должен уметь желать хорошего дня недели в целом, на русском языке.
Текущий день недели можно узнать вот так:
>>> import datetime
>>> print(datetime.datetime.today().weekday())
"""

import datetime

from flask import Flask

app = Flask(__name__)


@app.route("/hello-world/<username>")
def hello_world(username) -> str:
    today = datetime.datetime.today().weekday()
    # TODO Вместо серии повторяющихся проверок по одной переменной
    #  оптимальнее будет сделать словарь, в котором номер дня недели
    #  будет ключом, а текст сообщений сохранён в значениях.
    if today == 0:
        day = "понедельника"
        string = "Хорошего"
    elif today == 1:
        day = "вторника"
        string = "Хорошего"
    elif today == 2:
        day = "среды"
        string = "Хорошей"
    elif today == 3:
        day = "четверга"
        string = "Хорошего"
    elif today == 4:
        day = "пятницы"
        string = "Хорошей"
    elif today == 5:
        day = "суботы"
        string = "Хорошей"
    elif today == 6:
        day = "воскресенья"
        string = "Хорошего"
    return f"Привет {username}. {string} {day} "


if __name__ == "__main__":
    app.run(debug=True)
