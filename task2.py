"""
2) Из ваших заданий в уроках 1-5 найти 2-3 скрипта, сделать замеры памяти,
оптимизировать, вновь выполнить замеры и ОПИСАТЬ СЛОВАМИ, что вы сделали и чего
удалось добиться

Описания нужно делать в виде docstrings
"""
from memory_profiler import profile


"""
1 скрипт - нахождение факториала
"""


# Рекурсия
@profile
def find_fact_recursion(num):
    """
        Функция для нахождения факториала числа через рекурсию
        :param num: число для расчета факториала
        :return: факториал числа
        """
    if num == 0:
        return 1
    return find_fact_recursion(num - 1) * num


# Цикл
@profile
def find_fact_cycle(num):
    """
        Функция для нахождения факториала числа при помощи цикла
        :param num: число для расчета факториала
        :return: факториал числа
    """
    factorial = 1
    while num > 1:
        factorial *= num
        num -= 1
    return factorial


# Генератор
def fact_gen(number):
    """
    Функция генератор для нахождения факториала числа
    :param number: число для расчета факториала
    :return: пошаговое выполенение умножения
    """
    mult = 1
    count = number
    while count != 0:
        mult = mult * count
        count -= 1
        yield mult


@profile
def find_fact_gen(n):
    """
        Функция для нахождения факториала числа при помощи генератора
        :param n: число для расчета факториала
        :return: факториал числа
    """
    index = 0
    for el in fact_gen(n):
        if index == n - 1:
            return el
        index += 1


find_fact_recursion(5)
"""
Результат работы функции нахождения факториала при помощи рекурсии:

Line #    Mem usage    Increment  Occurrences   Line Contents
=============================================================
    13     22.5 MiB     22.5 MiB           6   @profile
    14                                         def find_fact_recursion(num):
    15     22.5 MiB      0.0 MiB           6       if num == 0:
    16     22.5 MiB      0.0 MiB           1           return 1
    17     22.5 MiB      0.0 MiB           5       return 
                                                    find_fact_recursion(num-1)
                                                    * num
"""

find_fact_cycle(5)
"""
Результат работы функции нахождения факториала при помощи цикла:

Line #    Mem usage    Increment  Occurrences   Line Contents
=============================================================
    21     22.5 MiB     22.5 MiB           1   @profile
    22                                         def find_fact_cycle(num):
    23     22.5 MiB      0.0 MiB           1       factorial = 1
    24     22.5 MiB      0.0 MiB           5       while num > 1:
    25     22.5 MiB      0.0 MiB           4           factorial *= num
    26     22.5 MiB      0.0 MiB           4           num -= 1
    27     22.5 MiB      0.0 MiB           1       return factorial
"""

find_fact_gen(5)
"""
Результат работы функции нахождения факториала при помощи генератора:

Line #    Mem usage    Increment  Occurrences   Line Contents
=============================================================
    44     22.5 MiB     22.5 MiB           1   @profile
    45                                         def find_fact_gen(n):
    46     22.5 MiB      0.0 MiB           1       index = 0
    47     22.5 MiB      0.0 MiB           5       for el in fact_gen(n):
    48     22.5 MiB      0.0 MiB           5           if index == n - 1:
    49     22.5 MiB      0.0 MiB           1               return el
    50     22.5 MiB      0.0 MiB           4           index += 1
"""

"""
Проведено тестирование получения факториала числа разными методами:
через рекурсию
через цикл
через генератор
По объему занимаемой памяти все три метода являются оптимизироваными. Сборщик 
мусора отрабатывает отлично, удаляя создаваемые локальные переменные после 
отработки методов.
"""


"""
2 скрипт - преобразование вводимого числа в строковый вид названия времени года
"""


# Использование списка и кортежей
@profile
def find_season_list(number):
    """
    Функция вывода времени года в строковой форме
    :param number: номер месяца года
    :return: время года
    """
    seasons = ["зима", "весна", "лето", "осень", "нет такого месяца"]
    winter = (12, 1, 2)
    spring = (3, 4, 5)
    summer = (6, 7, 8)
    autumn = (9, 10, 11)
    index = None
    if number in winter:
        index = 0
    elif number in spring:
        index = 1
    elif number in summer:
        index = 2
    elif number in autumn:
        index = 3
    else:
        index = 4
    return seasons[index]


# Использование словаря
@profile
def find_season_dict(number):
    """
    Функция вывода времени года в строковой форме
    :param number: номер месяца года
    :return: время года
    """
    result = None
    seasons = {1: 'зима', 2: 'зима', 3: 'весна', 4: 'весна', 5: 'весна',
               6: 'лето', 7: 'лето', 8: 'лето', 9: 'осень', 10: 'осень',
               11: 'осень', 12: 'зима'}
    if number < 1 or number > 12:
        result = 'нет такого месяца!'
    else:
        result = seasons[number]
    return result


find_season_list(1)
"""
Результат работы функции показа времени года(список, кортежи):

Line #    Mem usage    Increment  Occurrences   Line Contents
=============================================================
   110     22.5 MiB     22.5 MiB           1   @profile
   111                                         def find_season_list(number):
   112                                             ""Show time of year""
   113     22.5 MiB      0.0 MiB           1       seasons = ["зима", "весна",
                                        "лето", "осень", "нет такого месяца"]
   114     22.5 MiB      0.0 MiB           1       winter = (12, 1, 2)
   115     22.5 MiB      0.0 MiB           1       spring = (3, 4, 5)
   116     22.5 MiB      0.0 MiB           1       summer = (6, 7, 8)
   117     22.5 MiB      0.0 MiB           1       autumn = (9, 10, 11)
   118     22.5 MiB      0.0 MiB           1       index = None
   119     22.5 MiB      0.0 MiB           1       if number in winter:
   120     22.5 MiB      0.0 MiB           1           index = 0
   121                                             elif number in spring:
   122                                                 index = 1
   123                                             elif number in summer:
   124                                                 index = 2
   125                                             elif number in autumn:
   126                                                 index = 3
   127                                             else:
   128                                                 index = 4
   129     22.5 MiB      0.0 MiB           1       return seasons[index]

"""

find_season_dict(1)
"""
Результат работы функции показа времени года(словарь):

Line #    Mem usage    Increment  Occurrences   Line Contents
=============================================================
   132     22.5 MiB     22.5 MiB           1   @profile
   133                                         def find_season_dict(number):
   134                                             ""Show time of year""
   135     22.5 MiB      0.0 MiB           1       result = None
   136     22.5 MiB      0.0 MiB           2       seasons = {1: 'зима', 2: 
                                                            'зима', 3: 'весна',
                                                             4: 'весна', 
                                                             5: 'весна',
   137     22.5 MiB      0.0 MiB           1                 6: 'лето', 
                                                             7: 'лето', 
                                                             8: 'лето', 
                                                             9: 'осень',
                                                             10: 'осень',
   138     22.5 MiB      0.0 MiB           1                 11: 'осень', 
                                                             12: 'зима'}
   139     22.5 MiB      0.0 MiB           1       if number < 1 or number >12:
   140                                                 result = 'нет такого 
                                                                месяца!'
   141                                             else:
   142     22.5 MiB      0.0 MiB           1           result = seasons[number]
   143     22.5 MiB      0.0 MiB           1       return result

"""

"""
Результат: Проблем с памятью нет, все в пределах нормы.
"""


