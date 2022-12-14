"""
1) Из ваших заданий в уроках 1-5 найти 2-3 скрипта, сделать замеры времени,
оптимизировать, вновь выполнить замеры и ОПИСАТЬ СЛОВАМИ, что вы сделали и чего
удалось добиться

Описания нужно делать в виде docstrings
"""


# 1 скрипт - поиск максимальной цифры в числе
def find_max_digit_1(num):
    """Использование цикла"""
    max_digit = num % 10
    while num != 0:
        compare_digit = num // 10 % 10
        if compare_digit > max_digit:
            max_digit = compare_digit
        num = num // 10
    return max_digit


def find_max_digit_2(num):
    """Использование встроенных методов"""
    maximum = 0
    while num:
        num, n = divmod(num, 10)
        maximum = max(maximum, n)
    return maximum


def find_max_digit_3(num):
    """Использование встроенных методов"""
    maximum = 0
    while num:
        n = num % 10
        maximum = max(maximum, n)
        num = num // 10
    return maximum


def find_max_digit_4(num):
    """Использование встроенных методов"""
    maximum = 0
    while num:
        num, n = divmod(num, 10)
        if n > maximum:
            maximum = n
    return maximum


# 2 скрипт - поиск месяца
def find_season_list(number):
    """Show time of year"""
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


def find_season_dict(number):
    """Show time of year"""
    result = None
    seasons = {1: 'зима', 2: 'зима', 3: 'весна', 4: 'весна', 5: 'весна',
               6: 'лето', 7: 'лето', 8: 'лето', 9: 'осень', 10: 'осень',
               11: 'осень', 12: 'зима'}
    result = seasons[number]
    return result


# 3 скрипт - функция возведения в степень
def pow_with_operator(x_parameters, y_parameters):
    """
    Функция возведения числа в степень с помощью оператора **
    :param x_parameters: число
    :param y_parameters: степень
    :return: Возврат значения возведения в степень
    """
    return x_parameters ** y_parameters


def pow_with_cycle(x_parameters, y_parameters):
    """
    Функция возведения  числа в степень с помощью цикла
    :param x_parameters: число
    :param y_parameters: степень
    :return: Возврат значения возведения в степень
    """
    mult = 1
    if y_parameters < 0:
        while y_parameters < 0:
            mult *= 1 / x_parameters
            y_parameters += 1
    else:
        while y_parameters > 0:
            mult *= x_parameters
            y_parameters -= 1
    return mult


def pow_internal(x_parameters, y_parameters):
    """
    Функция возведения числа в степень с помощью оператора **
    :param x_parameters: число
    :param y_parameters: степень
    :return: Возврат значения возведения в степень
    """
    return pow(x_parameters, y_parameters)
