"""
С помощью команды ps можно посмотреть список процессов, запущенных текущим пользователем.
Особенно эта команда выразительна с флагами
    $ ps aux
Запустите эту команду, output сохраните в файл, например вот так
$ ps aux >> output_file.txt
В этом файле вы найдёте информацию обо всех процессах, запущенных в системе.
В частности там есть информация о потребляемой процессами памяти - это столбец RSS .
Напишите в функцию python, которая будет на вход принимать путь до файла с output
и на выход возвращать суммарный объём потребляемой памяти в человеко-читаемом формате.
Это означает, что ответ надо будет перевести в байты, килобайты, мегабайты и тд.

Для перевода можете воспользоваться функцией _sizeof_fmt
"""


def _sizeof_fmt(num, suffix="B"):
    #  В колонке RSS результат возвращается в килобайтах.
    #  В текущей реализации результат будет в 1024 раза меньше
    #  чем должен быть. Для исправления проще всего убрать первый
    #  элемент списка в следующей строке.
    for unit in ["Ki", "Mi", "Gi", "Ti", "Pi", "Ei", "Zi"]:
        if abs(num) < 1024.0:
            return "%3.1f%s%s" % (num, unit, suffix)
        num /= 1024.0
    return "%.1f%s%s" % (num, "Yi", suffix)


def get_summary_rss(ps_output_file_path: str) -> str:
    result = 0
    with open(ps_output_file_path) as ouput_file:
        for line in ouput_file.readlines():
            line_list = line.split()
            try:
                if int(line_list[5]) > 0:
                    result += int(line_list[5])
                    line_list.clear()
            except (TypeError, ValueError):
                line_list.clear()
    return _sizeof_fmt(result)


if __name__ == "__main__":
    #  Старайтесь использовать в заданиях относительные пути.
    #  Если output_file.txt находится рядом с файлом задания,
    #  то достаточно пути "output_file.txt"
    print(
        get_summary_rss("output_file.txt"))

# Зачёт!

