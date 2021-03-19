"""
Массив размером 2m + 1, где m — натуральное число, заполнен случайным образом.
Найдите в массиве медиану.
Медианой называется элемент ряда, делящий его на две равные части: в одной находятся элементы, которые не меньше медианы,
в другой — не больше медианы.
"""

import random
import statistics

arr = [random.randint(0,50) for _ in range(21)]


# сортировка грабл... расческой
def pitchfork(data):
    ln = len(data)
    step = (ln * 10 // 13) if ln > 1 else 0  #
    while step:
        if 8 < step < 11:
            step = 11
        is_moved = False
        for i in range(ln - step):
            if data[i + step] < data[i]:
                data[i], data[i + step] = data[i + step], data[i]
                is_moved = True
        step = (step * 10 // 13) or is_moved


# пытаюсь реализовать алгоритм BFPRT описанный по ссылке:
# https://ru.wikipedia.org/wiki/Алгоритм_выбора
def choise_middle(data):
    div_x = 3
    ln = len(data)
    middles = []

    print(data)
    # print(f'{ln=}')
    if ln == 3:
        a = data[0]
        b = data[1]
        c = data[2]
        if b < a < c or c < a < b:
            return a
        elif a < b < c or c < b < a:
            return b
        else:
            return c
    elif ln == 1:
        return data[0]

    while ln % div_x % 2 == 0 and div_x < ln:
        # print(div_x, ln, ln % 2)
        div_x += 2

    if div_x == ln:
        return data[ln//2]
    # print(f'{div_x=}')
    for i in range(ln // div_x):
        # print(ln, div_x * i, ln // div_x + ln // div_x * i)
        # print(data[div_x * i: div_x + div_x * i])
        if len(data[div_x * i: div_x + div_x * i]):
            middles.append(choise_middle(data[div_x * i: div_x + div_x * i]))
    if len(data[ln - ln % div_x:]):
        middles.append(choise_middle(data[ln - ln % div_x:]))

    # print(len(middles))
    pitchfork(middles)
    # print(middles)
    return middles[len(middles)//2]


median_val = choise_middle(arr)
print('Исходный массив:')
print(arr)
print('Сортирую для наглядности:')
pitchfork(arr)
print(arr)
print('#########################################')
print('Мой результат:')
print(median_val)
print('Проверка:')
checked_val = statistics.median(arr);
print(statistics.median(arr))
if checked_val != median_val:
    print('Сдаюсь! Не знаю как... 8 часов и правильная реализация алгоритма привели меня к неверному результату.')
