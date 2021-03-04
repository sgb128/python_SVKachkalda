"""
В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.
"""
import random

MIN_VAL = 10
MAX_VAL = 100
ARR_SIZE = 5
array = [random.randint(MIN_VAL, MAX_VAL) for _ in range(ARR_SIZE)]

min_i = max_i = 0

for i in range(len(array)):
    if array[min_i] > array[i]:
        min_i = i
    if array[max_i] < array[i]:
        max_i = i

print(array)
array[max_i], array[min_i] = array[min_i], array[max_i]
print(array)
