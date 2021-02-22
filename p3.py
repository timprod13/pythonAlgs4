"""
Задание 3.

Приведен код, формирующий из введенного числа
обратное по порядку входящих в него
цифр и вывести на экран.

Сделайте профилировку каждого алгоритма через cProfile и через timeit

Сделайте вывод, какая из трех реализаций эффективнее и почему!!!

И можете предложить еще свой вариант решения!
Без аналитики задание считается не принятым
"""
from cProfile import run
import timeit


def revers_1(enter_num, revers_num=0):
    if enter_num == 0:
        return revers_num
    else:
        num = enter_num % 10
        revers_num = (revers_num + num / 10) * 10
        enter_num //= 10
        return revers_1(enter_num, revers_num)


def revers_2(enter_num, revers_num=0):
    while enter_num != 0:
        num = enter_num % 10
        revers_num = (revers_num + num / 10) * 10
        enter_num //= 10
    return revers_num


def revers_3(enter_num):
    enter_num = str(enter_num)
    revers_num = enter_num[::-1]
    return revers_num


#   Создадим функцию для отработки cProfile всех трёх функций
def main(numb):
    result_revers1 = revers_1(numb)
    result_revers2 = revers_2(numb)
    result_revers3 = revers_3(numb)


num = 123456789012345678901231323156464878979754654684948654561123156456545454654641231321654564897874564564654878654564
run("main(num)")
""" Вывод cProfile:
   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.000    0.000 <string>:1(<module>)
    115/1    0.000    0.000    0.000    0.000 p3.py:19(revers_1)
        1    0.000    0.000    0.000    0.000 p3.py:29(revers_2)
        1    0.000    0.000    0.000    0.000 p3.py:37(revers_3)
        1    0.000    0.000    0.000    0.000 p3.py:44(main)
        1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
Результат вычисления времени через cProfile лишь показал, что все 3 функции отрабаываются за время меньше тысячной 
секунды, лишь можем увидеть, что revers_1 - это рекурсивная функция и она накапливает вызовы, в остальных двух
функциях рекурсий нет и вызываются они один раз. В принципе можно как в уроке прописать во всех трёх функциях sleep,
чтобы было более наглядно видно разницу между временем отработки функций, число вхождений и итераций. Однако можно
обойтись без этого с вычислением времени исполнения через timeit и анализа кода:
"""

print(f'revers_1: {timeit.timeit("revers_1(num)", setup="from __main__ import revers_1, num", number=10000)}')
print(f'revers_2: {timeit.timeit("revers_2(num)", setup="from __main__ import revers_2, num", number=10000)}')
print(f'revers_3: {timeit.timeit("revers_3(num)", setup="from __main__ import revers_3, num", number=10000)}')

""" Вывод timeit с выполнением функции 10000 раз (для наглядности):
revers_1: 0.3854417
revers_2: 0.26700029999999997
revers_3: 0.00975540000000008
"""

# Вывод: функция revers_1 - самая медленная (за счёт рекурсий), в revers_2 - присуствует итерация цикла с
# предусловием, поэтому отрабатывает функция чуть быстрее, но в revers_3 реализован реверс списка, что я и предлагал
# как решение в предыдущей задаче, в этой функции нет ни рекурсий, ни итераций, поэтому время её выполнения наиболее
# быстрое
