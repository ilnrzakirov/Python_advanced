"""
Давайте немного вспомним Linux command line утилиты.

Напишите Flask GET endpoint, который на вход принимает флаги командной строки,
    а возвращает результат запуска команды PS с этими флагами.
    Чтобы красиво отформатировать результат вызова программы - заключите его в тэг <pre>:
        <pre>Put your text here</pre>

Endpoint должен быть по url = /ps и принимать входные значение через аргумент arg
Напомню, вызвать программу ps можно, например, вот так

    >>> import shlex, subprocess
    >>> command_str = f"uptime"
    >>> command = shlex.split(command_str)
    >>> result = subprocess.run(command, capture_output=True)
"""
from flask import Flask, request

import shlex

import subprocess


app = Flask(__name__)


@app.route("/ps", methods=["GET"])
def _ps():
    req = request.args.getlist("flag")
    flag = "".join(req)
    command_str = f"ps {flag}"
    command = shlex.split(command_str)
    result = subprocess.run(command, capture_output=True)
    if result.returncode == 0:
        return f"<pre>{result.stdout.decode()}</pre>"
    else:
        return f"Ошибка ввода: {result.stderr.decode()}"
    # TODO Здесь аргументы к ps передаёт пользователь и
    #  это может вызвать ошибки. Поэтому нужно проверять
    #  result.returncode и если программа завершилась
    #  без ошибок нужно вернуть result.stdout.
    #  В случае ошибки нужно вывести сообщение и вернуть
    #  подробности из result.stderr.





if __name__ == "__main__":
    app.run(debug=True)
