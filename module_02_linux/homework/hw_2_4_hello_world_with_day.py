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
    #  Вместо серии повторяющихся проверок по одной переменной
    #  оптимальнее будет сделать словарь, в котором номер дня недели
    #  будет ключом, а текст сообщений сохранён в значениях.
    week = {0: "Хорошего понедельника", 1: "Хорошего вторника", 3: "Хорошей среды", 4: "Хорошего четверга",
            5: "Хорошей субботы", 6: "Хорошего воскресенья"}

    return f"Привет {username}. {week[today]} "


if __name__ == "__main__":
    app.run(debug=True)
