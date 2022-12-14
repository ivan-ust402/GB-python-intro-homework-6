from timeit import timeit
from task1 import find_max_digit_1, find_max_digit_2, find_max_digit_3, \
    find_max_digit_4, find_season_list, find_season_dict, pow_with_cycle, \
    pow_with_operator, pow_internal

# 1 Тест времени для функций поиска максимальной цифры в числе
print(find_max_digit_1(123456789))
print(find_max_digit_2(123456789))
print(find_max_digit_3(123456789))
print(find_max_digit_4(123456789))

print(timeit("find_max_digit_1(123456789)",
             setup="from task1 import find_max_digit_1",
             number=1000000))
# Результат: 0.7586034999694675

print(timeit("find_max_digit_2(123456789)",
             setup="from task1 import find_max_digit_2",
             number=1000000))
# Результат: 1.3885279998648912

print(timeit("find_max_digit_3(123456789)",
             setup="from task1 import find_max_digit_3",
             number=1000000))
# Результат: 1.3726840999443084
print(timeit("find_max_digit_4(123456789)",
             setup="from task1 import find_max_digit_4",
             number=1000000))
# Результат: 0.637631299905479

"""
Тестируем функции поиска максимальной цифры в числе.

В первом случае я использовал цикл и обычные операторы вычислений.
Во втором случае - встроенные методы python max и divmod.

Результат для функции с применением цикла и обычных операторов вычислений:
0.7586034999694675 секунд
Результат для функции с применением max и divmod:
1.3885279998648912 секунд
Вывод: не всегда оптимально использовать встроенные методы.


Попробуем немного модернизировать наш код, убрав метод divmod.

Результат для функции с применением цикла и обычных операторов вычислений:
0.7639486000407487 секунд
Результат для функции с применением max и divmod:
1.4045993001200259 секунд
Результат для функции с применением max и операторов вычисления:
1.3767099999822676 секунд
Вывод: метод max выполняется достаточно долго, divmode лучше оптимизирован.


Попробуем вернуть функцию divmod и заменим max на условие. 

Результат для функции с применением цикла и обычных операторов вычислений:
0.7592029999941587 секунд
Результат для функции с применением max и divmod:
1.3954588000196964 секунд
Результат для функции с применением max и операторов вычисления:
1.3799406001344323 секунд
Результат для функции с применением divmod и операторов вычисления:
0.6232388999778777 секунд

Вывод: Да, в результате данных манипуляций мы получили более оптимальную по 
времени работу функции. 
"""


# 2 Тест времени для функции отображения строкового значения месяца года
print(find_season_list(12))
print(find_season_dict(12))

print(timeit("find_season_list(12)",
             setup="from task1 import find_season_list",
             number=1000000))
# Результат: 0.13342380011454225

print(timeit("find_season_dict(12)",
             setup="from task1 import find_season_dict",
             number=1000000))
# Результат: 0.3410035998094827


"""
Тестируем функции поиска месяца года по введенному числу.

В первом случае используется список и кортежи. Запись кода достаточно
громозская.
Во втором случае - поиск производится по словарю. Запись кода лаконичная.

Результат для функции с применением списка и кортежей:
0.13342380011454225 секунд
Результат для функции с применением словаря:
0.3410035998094827 секунд
Вывод: несмотря на лаконичность кода, поиск по словарю достаточно 
времезатратная операция. Подход с применением кортежей и списка более оптимален 
"""

# 3 Тест времени для функций возведения в степень
print(pow_with_operator(2, 8))
print(pow_with_cycle(2, 8))
print(pow_internal(2, 8))

print(timeit("pow_with_operator(2, 8)",
             setup="from task1 import pow_with_operator",
             number=1000000))
# Результат: 0.06503459997475147

print(timeit("pow_with_cycle(2, 8)",
             setup="from task1 import pow_with_cycle",
             number=1000000))
# Результат: 0.33110040007159114

print(timeit("pow_internal(2, 8)",
             setup="from task1 import pow_internal",
             number=1000000))
# Результат: 0.07882179995067418


"""
Тестируем функции возведения числа в степень.

В первом случае используется оператор **.
Во втором случае - циклы и условия.
В третьем - встроенный метод pow

Результат для функции с применением оператора **:
0.06503459997475147 секунд
Результат для функции с применением циклов и условия:
0.33110040007159114 секунд
Результат для функции с применением метода pow:
0.07882179995067418 секунд
Вывод: В результате самым долгим способом возведения в степень, является
функция с использованием условия и циклов, и, как и в первой протестированной
задаче, более оптимальным по времени выполнения является функция с применением
оператора **, встроенный метод, к сожалению, отстает от него.  
"""