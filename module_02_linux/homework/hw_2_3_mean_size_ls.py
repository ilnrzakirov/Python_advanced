"""
Напишите функцию, которая будет по output команды ls возвращать средний размер файла в папке.
В качестве аргумента функции должен выступать путь до файла с output команды ls
"""


def get_mean_size(ls_output_path: str) -> str:
    result = 0
    with open(ls_output_path, "r") as file:
        for line in file:
            lines = line.split()
            if len(lines) > 2:
                result += int(lines[4])

    # TODO Нужно выводить не суммарное значение, а среднее.
    return str(result)


if __name__ == "__main__":
    #  В этом задании нужно работать с файлом,
    #  содержащим вывод команды ls -l.
    #  В output_file.txt результаты вывода
    #  команды ps.
    print(get_mean_size("output.txt"))
