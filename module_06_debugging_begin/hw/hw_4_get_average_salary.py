"""
Вы работаете программистом на предприятии.
К вам пришли из бухгалтерии и попросили посчитать среднюю зарплату по предприятию.
Вы посчитали, получилось слишком много, совсем не реалистично.
Вы подумали и проконсультировались со знакомым из отдела статистики.
Он посоветовал отбросить максимальную и минимальную зарплату.
Вы прикинули, получилось что-то похожее на правду.

Реализуйте функцию get_average_salary_corrected,
которая принимает на вход непустой массив заработных плат
(каждая -- число int) и возвращает среднюю з/п из этого массива
после отбрасывания минимальной и максимальной з/п.

Задачу нужно решить с алгоритмической сложностью O(N) , где N -- длина массива зарплат.

Покройте функцию логгированием.
"""
import logging
from typing import List

logger = logging.getLogger("salary")
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s %(message)s', datefmt='%H:%M:%S')


def get_average_salary_corrected(salaries: List[int]) -> float:
    res = 0
    if not isinstance(salaries, list):
        logger.debug("Ошибка вх данных")
        return 0
    max = salaries[0]
    min = salaries[0]
    if len(salaries) > 0:
        for salary in salaries:
            if not isinstance(salary, int):
                logger.debug("Подается не число")
                continue
            if salary <= 0:
                logger.debug("Число меньше либо равно нулю")
                continue
            if salary > max:
                max = salary
            elif salary < min:
                min = salary
            res += salary
    if res == 0:
        logger.debug("Дайте список реальных зарплат")
        return 0
    else:
        logger.debug("Список зарплат пуст")
    return ((res - min - max) / (len(salaries) - 2))


print(get_average_salary_corrected({0, 0, 0, 0, 0}))