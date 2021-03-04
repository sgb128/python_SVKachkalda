"""
В массиве найти максимальный отрицательный элемент.
Вывести на экран его значение и позицию в массиве.

Примечание к задаче: пожалуйста не путайте «минимальный» и «максимальный отрицательный».
Это два абсолютно разных значения.
"""
import random

MIN_VAL = -5
MAX_VAL = 20
ARR_SIZE = 10
array = [random.randint(MIN_VAL, MAX_VAL) for _ in range(ARR_SIZE)]

min_i = 0
exists = 0
print(array)
for i in range(len(array)):
    if 0 > array[i] >= array[min_i] or array[min_i] >= 0 > array[i]:
        min_i = i
        exists = 1

if exists:
    print('Максимальные отрицательный элемент:', array[min_i], '\nПозиция:', min_i)
else:
    print('В массиве отсутствуют отрицательные элементы.')

