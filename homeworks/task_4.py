"""
Определить, какое число в массиве встречается чаще всего.
"""
import random

MIN_VAL = 0
MAX_VAL = 3
ARR_SIZE = 10
array = [random.randint(MIN_VAL, MAX_VAL) for _ in range(ARR_SIZE)]

cnt = 0
num = [array[cnt], 0]
i = j = 0
print()
print('Исходный массив:', array)
while i < len(array):
    while j < len(array):
        if array[j] == array[i]:
            cnt += 1

        j += 1

    if num[1] < cnt:
        num = [array[i], cnt]

    cnt = 0
    i += 1
    j = i

print('Чаще всего встречающееся число и количество его повторений:', num)

