"""
Давайте напишем свое приложение для учета финансов.
Оно должно уметь запоминать, сколько денег мы потратили за день,
    а также показывать затраты за отдельный месяц и за целый год.

Модифицируйте  приведенный ниже код так, чтобы у нас получилось 3 endpoint:
/add/<date>/<int:number> - endpoint, который сохраняет информацию о совершённой за какой-то день трате денег (в рублях, предполагаем что без копеек)
/calculate/<int:year> -- возвращает суммарные траты за указанный год
/calculate/<int:year>/<int:month> -- возвращает суммарную трату за указанный месяц

Гарантируется, что дата для /add/ endpoint передаётся в формате
YYYYMMDD , где YYYY -- год, MM -- месяц (число от 1 до 12), DD -- число (от 01 до 31)
Гарантируется, что переданная дата -- корректная (никаких 31 февраля)
"""
from flask import Flask

app = Flask(__name__)

storage = {}


@app.route("/add/<date>/<int:number>")
def add(date: str, number: int):
    global storage
    if date in storage.keys():
        storage[date] += number
    else:
        storage[date] = number
    return f"Успешно"


@app.route("/calculate/<int:year>")
def calculate_year(year: int):
    global storage
    result = 0
    for key, value in storage.items():
        if str(key).startswith(str(year)):
            result += value
    print(storage)
    return str(result)



@app.route("/calculate/<int:year>/<int:month>")
def calculate_month(year: int, month: int):
    global storage
    result = 0
    date = str(year) + str(month)
    for key, value in storage.items():
        if str(key).startswith(date):
            result += value
    return str(result)


if __name__ == "__main__":
    app.run(debug=True)
