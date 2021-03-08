"""
Задача №1: Проанализировать скорость и сложность одного любого алгоритма из разработанных в рамках
домашнего задания первых трех уроков.

Итак, в качестве "испытуемого" я взял первое домашнее задание от третьего урока урока:

В диапазоне натуральных чисел от 2 до 99 определить, сколько из них кратны каждому из чисел в диапазоне от 2 до 9.
"""

# я скопировал ваш вариант домашнего задания 1 (честно-пречестно у мея первые два аварианта решения были такими же, сделал это
# исключительно чтобы повторно не набирать код).
# Ведь цель стоит проанализировать алгоритм, а не написать его.
# Только разница в том что мне пришлось оформить данные алгоритмы в виде функций возвращающих массивы.

import timeit
import matplotlib.pyplot as plt
import cProfile


# вместо вывода (print) вывод будет осуществляться в массив (list)
def dividers_var1(min_d: int, min_v: int, max_d: int, max_v: int) -> list:
    frequency = []
    for i in range(min_d, max_d + 1):
        frequency.append(0);
        for j in range(min_v, max_v + 1):
            if j % i == 0:
                frequency[i - min_d] += 1
    return frequency


def dividers_var2(min_d: int, min_v: int, max_d: int, max_v: int) -> list:
    result = []
    freq = [0] * (max_d - min_d + 1)
    for i in range(min_v, max_v + 1):
        for j in range(min_d, max_d + 1):
            if i % j == 0:
                freq[j - min_d] += 1

    for i, item in enumerate(freq, start=min_d):
        result.append(item)
    return result


def dividers_var3(min_d: int, min_v: int, max_d: int, max_v: int) -> list:
    result = []
    r = min_d
    while r <= max_d:
        rez = max_v // r - min_v // r
        if not min_v % r:
            rez += 1

        result.append(rez)
        r += 1
    return result


print('запуск алгоритмов с исходными значениями задания')
print(timeit.timeit('dividers_var1(2, 2, 9, 99)', number=10, globals=globals()))  # 0.00173230000000002
print(timeit.timeit('dividers_var2(2, 2, 9, 99)', number=10, globals=globals()))  # 0.0013768999999999032
print(timeit.timeit('dividers_var3(2, 2, 9, 99)', number=10, globals=globals()))  # 7.8400000000034e-05
print()
print('увеличиваю диапазон значений делимых чисел (max_v)')
print(timeit.timeit('dividers_var1(2, 2, 9, 999)', number=10, globals=globals()))  # 010468800000000167
print(timeit.timeit('dividers_var2(2, 2, 9, 999)', number=10, globals=globals()))  # 0.015722000000000014
print(timeit.timeit('dividers_var3(2, 2, 9, 999)', number=10, globals=globals()))  # 3.250000000010189e-05
print()
print('увеличиваю еще на 9000')
print(timeit.timeit('dividers_var1(2, 2, 9, 9999)', number=10, globals=globals()))  # 0.1631612
print(timeit.timeit('dividers_var2(2, 2, 9, 9999)', number=10, globals=globals()))  # 0.28391959999999994
print(timeit.timeit('dividers_var3(2, 2, 9, 9999)', number=10, globals=globals()))  # 8.689999999988984e-05
print()
print('и еще на 90_000')
print(timeit.timeit('dividers_var1(2, 2, 9, 99_999)', number=10, globals=globals()))  # 2.6697182
print(timeit.timeit('dividers_var2(2, 2, 9, 99_999)', number=10, globals=globals()))  # 3.1011767
print(timeit.timeit('dividers_var3(2, 2, 9, 99_999)', number=10, globals=globals()))  # 9.400000000070463e-05
print('Запуск третьего алгоритма с изменением диапазона делителя на [2, 99_999]')
print(timeit.timeit('dividers_var3(2, 2, 99_999, 99_999)', number=10, globals=globals()))  # 9.400000000070463e-05

print()
print('Строим график...')

fig = plt.figure()
ax = fig.add_subplot(111)

max_val = 5_000
x_points = range(0, max_val, 500)
y_points = [timeit.timeit(f'dividers_var1(2, 2, 9, {i})', number=100, globals=globals()) for i in x_points]
p = ax.plot(x_points, y_points, 'r')
y_points = [timeit.timeit(f'dividers_var2(2, 2, 9, {i})', number=100, globals=globals()) for i in x_points]
p1 = ax.plot(x_points, y_points, 'y')
y_points = [timeit.timeit(f'dividers_var3(2, 2, 9, {i})', number=100, globals=globals()) for i in x_points]
p2 = ax.plot(x_points, y_points, 'g')
print('Для продолжения закройте график!')
ax.set_xlabel('MAX_VALs')
ax.set_ylabel('TIME')
ax.set_title('График зависимости времени от максимального числа передаваемого в алгоритм')
plt.show()
print()

# вывод анализа по timeit: судя по всремени выполнения - первый и второй варианты алгоритмов примерно одинаковы по времени
# выполнения, но значительно проигрывают третьему, так как в нем нет вложенного цикла, а единственный цикл является статичным
# за исключением диапазона делимых чисел, что не сильно влияет на его скорость выполнения, но сильно повлияет на скорость
# выполнения двух первых алгоритмов.

print('Первый вариант алгоритма:')
cProfile.run('dividers_var1(2, 2, 9, 9_999_999)')
print('Второй вариант алгоритма:')
cProfile.run('dividers_var2(2, 2, 9, 9_999_999)')
print('Третий вариант алгоритма:')
# значение делителя специально увеличено для отображения значений в результатах запуска
cProfile.run('dividers_var3(2, 2, 999_999, 999_999)')

"""
Первый вариант алгоритма:
         12 function calls in 26.948 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000   26.948   26.948 <string>:1(<module>)
        1   26.948   26.948   26.948   26.948 task_1.py:21(dividers_var1)
        1    0.000    0.000   26.948   26.948 {built-in method builtins.exec}
        8    0.000    0.000    0.000    0.000 {method 'append' of 'list' objects}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}


Второй вариант алгоритма:
         12 function calls in 30.007 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000   30.007   30.007 <string>:1(<module>)
        1   30.007   30.007   30.007   30.007 task_1.py:31(dividers_var2)
        1    0.000    0.000   30.007   30.007 {built-in method builtins.exec}
        8    0.000    0.000    0.000    0.000 {method 'append' of 'list' objects}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}


Третий вариант алгоритма:
         1000002 function calls in 1.253 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.009    0.009    1.253    1.253 <string>:1(<module>)
        1    1.029    1.029    1.245    1.245 task_1.py:44(dividers_var3)
        1    0.000    0.000    1.253    1.253 {built-in method builtins.exec}
   999998    0.216    0.000    0.216    0.000 {method 'append' of 'list' objects}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}

вывод: cProfile мало чем помог с информацией, быть может если бы я запустил его так же как 3ий вариант алгоритма - то я увидел
бы значения из которых собирается итоговое время, но боюсь что при этом мне придется ждать вечность(или около того), поэтому
экономя свое и ваше время я оставил запуск с теми значениями которые есть.
Тем не менее явно видно что 3ий алгоритм имеет (не могу вспомнить как называется слово) формулу O(1) в случае если минимальный
и максимальный делитель константны.
Или третий алгоритм будет постоянно выигрывать у первых двух по времени в случае если минимальный и максимальный делители будут
изменяться и алгоритм будет иметь формулу O(n) - где n - количество итераций цикла(количество делителей)
"""
