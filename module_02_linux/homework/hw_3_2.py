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
    #  При изменении содержимого объекта из глобальной области видимости
    #  не нужно объявлять её глобальной. global нужно только в случае, когда вы
    #  вы меняете саму переменную. Например для my_list.append() global не нужен.
    #  А для my_list = [] без global не обойтись.
    #  В этой функции не меняется переменная storage и global не нужен
    if date in storage.keys():
        storage[date] += number
    else:
        storage[date] = number
    return f"Успешно"


@app.route("/calculate/<int:year>")
def calculate_year(year: int):
    #  При изменении содержимого объекта из глобальной области видимости
    #  не нужно объявлять её глобальной. global нужно только в случае, когда вы
    #  вы меняете саму переменную. Например для my_list.append() global не нужен.
    #  А для my_list = [] без global не обойтись.
    #  В этой функции не меняется переменная storage и global не нужен.
    result = 0
    for key, value in storage.items():
        if str(key).startswith(str(year)):
            result += value
    print(storage)
    return str(result)


@app.route("/calculate/<int:year>/<int:month>")
def calculate_month(year: int, month: int):
    # При изменении содержимого объекта из глобальной области видимости
    #  не нужно объявлять её глобальной. global нужно только в случае, когда вы
    #  вы меняете саму переменную. Например для my_list.append() global не нужен.
    #  А для my_list = [] без global не обойтись.
    #  В этой функции не меняется переменная storage и global не нужен.
    #  Метод работает неверно в случаях когда месяц состоит из одной цифры.
    #  Адрес вида /calculate/2020/05 даёт целочисленные аргументы функции
    #  2020 и 5. В результате формируется ключ поиска 20205, а записи в словаре
    #  имеют вид 202005XX
    result = 0
    all_month = ["01", "02", "03", "04", "05", "06", "07", "08", "09", "10", "11", "12"]
    date = str(year) + all_month[month - 1]
    for key, value in storage.items():
        if str(key).startswith(date):
            result += value
    return str(result)


if __name__ == "__main__":
    app.run(debug=True)
