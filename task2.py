"""
2) Из ваших заданий в уроках 1-5 найти 2-3 скрипта, сделать замеры памяти,
оптимизировать, вновь выполнить замеры и ОПИСАТЬ СЛОВАМИ, что вы сделали и чего
удалось добиться

Описания нужно делать в виде docstrings
"""
from memory_profiler import profile


# 1 скрипт - нахождение факториала
# Рекурсия
@profile
def find_fact_recursion(num):
    if num == 0:
        return 1
    return find_fact_recursion(num-1) * num


# Цикл
@profile
def find_fact_cycle(num):
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
    index = 0
    for el in fact_gen(n):
        if index == n - 1:
            return el
        index += 1


find_fact_recursion(5)
"""
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
Line #    Mem usage    Increment  Occurrences   Line Contents
=============================================================
    44     22.5 MiB     22.5 MiB           1   @profile
    45                                         def find_fact_gen(n):
    46     22.5 MiB      0.0 MiB           1       index = 0
    47     22.5 MiB      0.0 MiB           5       for el in fact_gen(n):
    48     22.5 MiB      0.0 MiB           5           if index == n - 1:
    49     22.5 MiB      0.0 MiB           1               return el
    50     22.5 MiB      0.0 MiB           4           index += 1



Process finished with exit code 0

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
