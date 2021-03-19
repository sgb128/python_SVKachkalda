"""
Отсортируйте по возрастанию методом слияния одномерный вещественный массив,
заданный случайными числами на промежутке [0; 50).
Выведите на экран исходный и отсортированный массивы.
"""
import random

array = [random.randint(0, 500)/10 for _ in range(10)]


def merge_sort(data):
    new_data = []
    if len(data) > 1:
        da = merge_sort(data[0:len(data) // 2])
        ta = merge_sort(data[len(data) // 2:len(data)])
    else:
        return data

    while len(da) or len(ta):
        if not len(da):
            while len(ta):
                new_data.append(ta.pop(0))
        elif not len(ta):
            while len(da):
                new_data.append(da.pop(0))
        elif da[0] > ta[0]:
            new_data.append(ta.pop(0))
        else:
            new_data.append(da.pop(0))

    return new_data


print(array)
new_array = merge_sort(array)
# В старых операционных системах я помню был звук с таким характерным названием, и теперь где бы я не прочитал эти буквы
# в голове невольно проигрывается этот звук. (В W10 я почему-то не смог найти этот звук, неужели его убрали?)
print('Tadaaaaaa!!!!(Hello from Win98)', new_array)
# Ну и data превратить в tada - вышло уже случайно, но получилось это весьма кстати!
