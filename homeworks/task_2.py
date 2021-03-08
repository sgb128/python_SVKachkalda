import timeit
import cProfile
import matplotlib.pyplot as plt


def era(n):
    k = n
    a = []
    b = []
    while True:
        a.extend([0] * k)  # создание массива с n количеством элементов
        i = k - n
        while i < k:
            a[i] = i  # значениями от 0 до n-1
            i += 1
        a[1] = 0

        m = 2  # замена на 0 начинается с 3-го элемента (первые два уже нули)
        while m < k:  # перебор всех элементов до заданного числа
            if a[m] != 0:  # если он не равен нулю, то
                j = m * 2  # увеличить в два раза (текущий элемент - простое число)
                while j < k:
                    a[j] = 0  # заменить на 0
                    j = j + m  # перейти в позицию на m больше
            m += 1

        # вывод простых чисел на экран (может быть реализован как угодно)
        b = []
        for i in a:
            if a[i] != 0:
                b.append(a[i])

        if n > len(b) - 1:
            k += n
        else:
            break

    del a
    return b[n - 1]


def my_not_era(n):
    i = 1
    nums = []
    while len(nums) < n + 1:
        i += 1
        if i == 2:
            nums.append(i)
        else:
            j = 2
            while j < i:
                if not i % j:
                    break
                if j + 1 == i and i % j:
                    nums.append(i)
                j += 1
    return nums[n - 1]


"""
VAL = 50
print('С помощью алгоритма "решето Эратосфена"')
print(era(VAL))
print('\nПростой алгоритм')
print(my_era(VAL))
"""
print('Запуск функции с алгоритмом "Решето Эратосфена"')
print(timeit.timeit('era(100)', number=10, globals=globals()))  # 0.034046699999999985
print(timeit.timeit('era(150)', number=10, globals=globals()))  # 0.0505355999999999
print(timeit.timeit('era(200)', number=10, globals=globals()))  # 0.056298200000000076
print(timeit.timeit('era(250)', number=10, globals=globals()))  # 0.07164740000000003
print(timeit.timeit('era(300)', number=10, globals=globals()))  # 0.11178440000000012
print(timeit.timeit('era(350)', number=10, globals=globals()))  # 0.1313350000000002
print(timeit.timeit('era(400)', number=10, globals=globals()))  # 0.13124800000000003

print('Запуск функции без алгоритма "Решето Эратосфена"')
print(timeit.timeit('my_not_era(100)', number=10, globals=globals()))  # 0.08462989999999992
print(timeit.timeit('my_not_era(150)', number=10, globals=globals()))  # 0.2530127000000002
print(timeit.timeit('my_not_era(200)', number=10, globals=globals()))  # 0.4400453999999998
print(timeit.timeit('my_not_era(250)', number=10, globals=globals()))  # 0.7382843000000001
print(timeit.timeit('my_not_era(300)', number=10, globals=globals()))  # 1.2565204000000003
print(timeit.timeit('my_not_era(350)', number=10, globals=globals()))  # 1.5302454
print(timeit.timeit('my_not_era(400)', number=10, globals=globals()))  # 2.199009900000001

print()
print('Строим график...')

fig = plt.figure()
ax = fig.add_subplot(111)

x_points = range(50, 500, 50)
y_points = [timeit.timeit(f'era({i})', number=10, globals=globals()) for i in x_points]
p1 = ax.plot(x_points, y_points, 'y')
y_points = [timeit.timeit(f'my_not_era({i})', number=10, globals=globals()) for i in x_points]
p2 = ax.plot(x_points, y_points, 'g')
print('Для продолжения закройте график!')
ax.set_xlabel('Значение')
ax.set_ylabel('Время выполнения 10 запусков')
ax.set_title('График зависимости времени от максимального числа передаваемого в алгоритм')
plt.show()
print()

print('Алгоритм "Решето Эратосфена":')
cProfile.run('era(5000)')
print('Простой алгоритм:')
cProfile.run('my_era(5000)')

"""
Алгоритм "Решето Эратосфена":
         29688 function calls in 0.503 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.503    0.503 <string>:1(<module>)
        1    0.492    0.492    0.503    0.503 task_2.py:5(era)
        1    0.000    0.000    0.503    0.503 {built-in method builtins.exec}
       10    0.000    0.000    0.000    0.000 {built-in method builtins.len}
    29664    0.006    0.000    0.006    0.000 {method 'append' of 'list' objects}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
       10    0.005    0.000    0.005    0.000 {method 'extend' of 'list' objects}


Простой алгоритм:
         53624 function calls in 58.257 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000   58.257   58.257 <string>:1(<module>)
        1   58.233   58.233   58.257   58.257 task_2.py:41(my_not_era)
        1    0.000    0.000   58.257   58.257 {built-in method builtins.exec}
    48619    0.015    0.000    0.015    0.000 {built-in method builtins.len}
     5001    0.009    0.000    0.009    0.000 {method 'append' of 'list' objects}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
"""
# Выврод: алгоритм описанный в функции my_era получился медленнее из-за множества вызовов вложенного цикла. Взявший на себя
# всю основную нагрузку поиска простого числа.
