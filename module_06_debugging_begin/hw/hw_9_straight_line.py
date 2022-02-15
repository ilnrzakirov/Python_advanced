"""
Давайте немного отойдём от логирования.
Программист должен знать не только computer science, но и математику.
Давайте вспомним школьный курс математики.

Итак, нам нужно реализовать функцию, которая принимает на вход
list из координат точек (каждая из них - tuple с x и y).

Напишите функцию, которая определяет, лежат ли все эти точки на одной прямой или не лежат
"""
from typing import List, Tuple


def check_is_straight_line(coordinates: List[Tuple[float, float]]) -> bool:
    x = coordinates[0][0]
    y = coordinates[0][1]
    x_1 = coordinates[1][0]
    y_1 = coordinates[1][1]
    for item in coordinates[2 :]:
        x_2 = item[0]
        y_2 = item[1]
        try:
            if not ((x_2 - x_1) / (x_1 - x)) == ((y_2 - y_1) / (y_1 - y)):
                return False
        except ZeroDivisionError:
            x = coordinates[0][0]
            y = coordinates[0][1]
            for item in coordinates[1:]:
                if x == item[0]:
                    return True
            for item in coordinates[1:]:
                if y == item[1]:
                    return True
            return False
    return True

print(check_is_straight_line([(1, 1), (1, 2), (1, 3)]))
