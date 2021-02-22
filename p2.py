"""
Задание 2.

Приведен код, который формирует из введенного числа
обратное по порядку входящих в него цифр.
Задача решена через рекурсию
Выполнена попытка оптимизировать решение через мемоизацию.
Сделаны замеры обеих реализаций.

Сделайте аналитику, нужна ли здесь мемоизация или нет и почему?!!!
Если у вас есть идеи, предложите вариант оптимизации, если мемоизация не имеет смысла.
Без аналитики задание считается не принятым
"""

from timeit import timeit
from random import randint


def recursive_reverse(number):
    if number == 0:
        return ''
    return f'{str(number % 10)}{recursive_reverse(number // 10)}'


num_100 = randint(10000, 1000000)
num_1000 = randint(1000000, 10000000)
num_10000 = randint(100000000, 10000000000000)

print('Не оптимизированная функция recursive_reverse')
print(
    timeit(
        "recursive_reverse(num_100)",
        setup='from __main__ import recursive_reverse, num_100',
        number=10000))
print(
    timeit(
        "recursive_reverse(num_1000)",
        setup='from __main__ import recursive_reverse, num_1000',
        number=10000))
print(
    timeit(
        "recursive_reverse(num_10000)",
        setup='from __main__ import recursive_reverse, num_10000',
        number=10000))


def memoize(f):
    cache = {}

    def decorate(*args):

        if args in cache:
            return cache[args]
        else:
            cache[args] = f(*args)
            return cache[args]

    return decorate


@memoize
def recursive_reverse_mem(number):
    if number == 0:
        return ''
    return f'{str(number % 10)}{recursive_reverse_mem(number // 10)}'


print('Оптимизированная функция recursive_reverse_mem')
print(
    timeit(
        'recursive_reverse_mem(num_100)',
        setup='from __main__ import recursive_reverse_mem, num_100',
        number=10000))
print(
    timeit(
        'recursive_reverse_mem(num_1000)',
        setup='from __main__ import recursive_reverse_mem, num_1000',
        number=10000))
print(
    timeit(
        'recursive_reverse_mem(num_10000)',
        setup='from __main__ import recursive_reverse_mem, num_10000',
        number=10000))


def extended_slices(number):
    return f'{(str(number)[::-1])}'


print('Неудачная попытка оптимизации с помощью функции extended_slices')
print(
    timeit(
        "extended_slices(num_100)",
        setup='from __main__ import extended_slices, num_100',
        number=10000))
print(
    timeit(
        "extended_slices(num_1000)",
        setup='from __main__ import extended_slices, num_1000',
        number=10000))
print(
    timeit(
        "extended_slices(num_10000)",
        setup='from __main__ import extended_slices, num_10000',
        number=10000))

""" Вывод timeit:
Не оптимизированная функция recursive_reverse
0.0240904
0.027961
0.05268880000000001
Оптимизированная функция recursive_reverse_mem
0.0019465999999999928
0.0019376000000000115
0.0023891999999999802
Неудачная попытка оптимизации с помощью функции extended_slices
0.0033278999999999948
0.0035238999999999965
0.003895599999999999
"""

# После нескольких попыток оптимизировать выполнение задачи (ускорение рекурсии, а так же применение других функций)
# для решения задачи - я понял, что использование мемоизации является наиболее быстрым вариантом за счёт её
# структуры: мемоизация использует словарь для отслеживания результатов вычисления, уменьшая тем самым число вызовов
# функции, то есть на каждое уникальное значение приходится по 1 вызову, иначе используется кэшированное в словаре
# значение, однако при бОльшем количестве входных данных мемоизация может наоборот замедлить работу из-за
# необходимости выделения памяти для хранения значений. Но в данном случае мемоизация справляется на ура,
# так как имеется повторный запуск функции
