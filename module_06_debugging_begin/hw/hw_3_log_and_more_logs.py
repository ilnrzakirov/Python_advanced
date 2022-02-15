"""
Логов бывает очень много. А иногда - ооооооооочень много.
Из-за этого люди часто пишут логи не в человекочитаемом,
    а в машиночитаемом формате, чтобы машиной их было обрабатывать быстрее.

Напишите функцию

def log(level: str, message: str) -> None:
    pass


которая будет писать лог  в файл skillbox_json_messages.log в следующем формате:
{"time": "<время>", "level": "<level>", "message": "<message>"}

сообщения должны быть отделены друг от друга символами переноса строки.
Обратите внимание: наше залогированное сообщение должно быть валидной json строкой.

Как это сделать? Возможно метод json.dumps поможет вам?
"""

import datetime
import json
import time


def log(level: str, message: str) -> None:
    log = dict()
    d = datetime.datetime.now().time()
    time = str(d)
    log['time'] = time
    log['level'] = level
    log['mesage'] = message
    res = json.dumps(log)
    with open("skillbox_json_messages.log", "a") as file:
        file.write(f"{res}\n")


log("debug", "start")