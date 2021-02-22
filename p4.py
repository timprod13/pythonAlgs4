"""
Задание 4.

Приведены два алгоритма. В них определяется число,
которое встречается в массиве чаще всего.

Сделайте профилировку каждого алгоритма через timeit

Попытайтесь написать третью версию, которая будет самой быстрой.
Сделайте замеры и опишите, получилось ли у вас ускорить задачу.

Без аналитики задание считается не принятым
"""
import timeit

array = [1, 3, 1, 3, 4, 5, 1]


def func_1():
    m = 0
    num = 0
    for i in array:
        count = array.count(i)
        if count > m:
            m = count
            num = i
    return f'Чаще всего встречается число {num}, ' \
           f'оно появилось в массиве {m} раз(а)'


def func_2():
    new_array = []
    for el in array:
        count2 = array.count(el)
        new_array.append(count2)

    max_2 = max(new_array)
    elem = array[new_array.index(max_2)]
    return f'Чаще всего встречается число {elem}, ' \
           f'оно появилось в массиве {max_2} раз(а)'


# Упростим вторую функцию и напишем третью функцию в одну строку (как и сказано было на вебинаре) c помощью max(set())
def func_3():
    elem = max(set(array), key=array.count)
    return f'Чаще всего встречается число {elem}, ' \
           f'оно появилось в массиве {array.count(elem)} раз(а)'


# Для вычисления времени выполнения функций применим timeit с выполнением функции 10000 раз
print(f"func_1(): {timeit.timeit('func_1()', setup='from __main__ import func_1', number=10000)}")
print(func_1())
print(f"func_2(): {timeit.timeit('func_2()', setup='from __main__ import func_2', number=10000)}")
print(func_2())
print(f"func_3(): {timeit.timeit('func_3()', setup='from __main__ import func_3', number=10000)}")
print(func_3())
""" Вывод timeit:
func_1(): 0.015444099999999999
func_2(): 0.020499999999999997
func_3(): 0.013538300000000004
"""

# Вывод: функция func_3 быстрее остальных, так как была использована функция max с параметром key с переводом во
# множество для отсечения дублей
