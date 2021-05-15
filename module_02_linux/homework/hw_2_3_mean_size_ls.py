"""
Напишите функцию, которая будет по output команды ls возвращать средний размер файла в папке.
В качестве аргумента функции должен выступать путь до файла с output команды ls
"""
import os


def get_mean_size(ls_output_path: str) -> str:
    size = os.path.getsize(ls_output_path)
    return f"{round(size / 1024, 2)} Kib"


if __name__ == "__main__":
    print(get_mean_size("output_file.txt"))
