"""
Во втором массиве сохранить индексы четных элементов первого массива.
Например, если дан массив со значениями 8, 3, 15, 6, 4, 2,
второй массив надо заполнить значениями 0, 3, 4, 5, (индексация начинается с нуля),
т.к. именно в этих позициях первого массива стоят четные числа.
"""
import random

MIN_VAL = 10
MAX_VAL = 100
ARR_SIZE = 5
array = [random.randint(MIN_VAL, MAX_VAL) for _ in range(ARR_SIZE)]
res = []

for i in range(len(array)):
    if not array[i] % 2:
        res.append(i)

print(array, res, sep='\n')
