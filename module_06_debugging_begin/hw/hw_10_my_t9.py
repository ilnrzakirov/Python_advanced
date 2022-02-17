"""
Представьте что мы решаем задачу следующего вида.
У нас есть кнопочный телефон (например, знаменитая Нокиа 3310) и мы хотим,
чтобы пользователь мог проще отправлять SMS.

Мы реализуем свой собственный клавиатурный помощник.
Каждой цифре телефона соответствует набор букв:
2 - a ,b, c
3 - d, e, f
4 - g, h, i
5 - j, k, l
6 - m, n, o
7 - p, q, r, s
8 - t, u, v
9 - w, x, y, z

Пользователь нажимает на клавиши, например,  22736368
    после чего на экране печатается basement

Напишите функцию-помощник my_t9, которая на вход принимает цифровую
строку и возвращает list из слов английского языка,
которые можно получить из этой цифровой строки.

В качестве словаря английского языка можете использовать
содержимое файла /usr/share/dict/words

Ваше решение должно работать с алгоритмической сложностью O(N),
где N -- длина цифровой строки.
"""
from typing import List
import itertools

def my_t9(input_numbers: str) -> List[str]:
    dict = {2: ('a', 'b', 'c'), 3: ('d', 'e', 'f'), 4: ('g', 'h', 'i'), 5: ('j', 'k', 'l'), 6: ('m', 'n', 'o'),
            7: ('p', 'q', 'r', 's'), 8: ('t', 'u', 'v'), 9: ('w', 'x', 'y', 'z')}

    res = []
    tmp = []
    s = ""
    for item in input_numbers:
        tmp.append(dict[int(item)])
    combinations = list(itertools.product(*tmp))
    for item in combinations:
        for char in item:
            s += char
        with open("/usr/share/dict/words", "r") as file:
            for word in file.readlines():
                if s == word.strip('\n'):
                    res.append(s)
                    break
        s = ""
    return res


my_t9("22736")