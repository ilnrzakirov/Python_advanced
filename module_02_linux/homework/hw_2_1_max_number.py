"""
Реализуйте endpoint, с url, начинающийся с  /max_number ,
в который можно будет передать список чисел, перечисленных через / .
Endpoint должен вернуть текст "Максимальное переданное число {number}",
где number, соответственно, максимальное переданное в endpoint число,
выделенное курсивом.
"""

from flask import Flask

app = Flask(__name__)


@app.route("/max_number/<path:numbers>")
def max_number(numbers):
    def str_to_int(string: str) -> int:
        return int(string)

    number_list = numbers.split("/")
    number_list.sort(key=str_to_int, reverse=True)
    print(number_list)

    return f"Максимальное число <i>{number_list[0]}</i>"


if __name__ == "__main__":
    app.run(debug=True)
