"""
Напишите GET flask endpoint с url /uptime,
    который в ответ на запрос будет возвращать как долго текущая машина не перезагружалась
        (в виде строки f"Current uptime is '{UPTIME}'"
            где UPTIME - uptime системы. Это можно сделать с помощью команды uptime
            (https://www.opennet.ru/man.shtml?topic=uptime&category=1&russian=4)
        )

Напомним, что вызвать программу из python можно с помощью модуля subprocess:
    # >>> import shlex, subprocess
    # >>> command_str = f"uptime"
    # >>> command = shlex.split(command_str)
    # >>> result = subprocess.run(command, capture_output=True)
"""
#from celery.bin.result import result
from flask import Flask, request

import shlex

import subprocess


app = Flask(__name__)


@app.route("/uptime")
def uptime():
    command_str = f"uptime"
    command = shlex.split(command_str)
    result = subprocess.run(command, capture_output=True)
    #  Лучше разделить строку результата по запятой и
    #  взять первую часть.
    response = result.stdout.decode().split(",")
    #  В return эндполинта возвращает объект типа CompletedProcess.
    #  Нужно получить строку из result.stdout, вырезать из неё фрагмент
    #  с аптаймом и вернуть пользователю полученный результат
    return f"Current uptime is {response[0]}"


if __name__ == "__main__":
    app.run(debug=True)
