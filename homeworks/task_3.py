"""
Массив размером 2m + 1, где m — натуральное число, заполнен случайным образом.
Найдите в массиве медиану.
Медианой называется элемент ряда, делящий его на две равные части: в одной находятся элементы, которые не меньше медианы,
в другой — не больше медианы.
"""
import random

#         1   2  3   4   5  6   7  8   9 10  11  12  13  14  15 16 17  18  19  20  21
ARRAY = [49, 45, 4, 27, 48, 2, 37, 0, 27, 6, 16, 12, 27, 50, 26, 0, 1, 46, 50, 40, 13]
M = 10
# ARRAY = [random.randint(0, 50) for _ in range(2 * M + 1)]


# пытаюсь реализовать алгоритм BFPRT описанный по ссылке:
# http://www.mathnet.ru/links/df955578498bdb2984b665f99ea98f63/mp894.pdf
def split_array(data: list):
    x = data[len(data)//2]
    # print(x)
    left = 0
    right = len(data)-1
    while right > left:
        # print(data, left, right)
        if data[left] > x >= data[right]:
            data[left], data[right] = data[right], data[left]
            left += 1
            right -= 1
        else:
            if data[left] <= x:
                left += 1
            if data[right] > x:
                right -= 1
    return data


def find_median(data):
    median_array = []
    if len(data) > 3:
        for i in range(len(data)//3):
            # print(data[(i*3)], data[1+(i*3)], data[2+(i*3)])
            a, b, c = data[(i * 3)], data[1 + (i * 3)], data[2 + (i * 3)]
            if b < a < c or c < a < b:
                median_array.append(a)
            elif a < b < c or c < b < a:
                median_array.append(b)
            else:
                median_array.append(c)
        return find_median(median_array)
    else:
        a, b, c = data[0], data[1], data[2]
        if b < a < c or c < a < b:
            return a
        elif a < b < c or c < b < a:
            return b
        else:
            return c


# попытка за 5 минут решить задачу простым способом, но что-то я видимо устал и алгоритм получился неверный
# если придет решение то этот алгоритм удалю
def find_median_simple(data):
    for i in range(len(data)):
        left = right = 0
        for j in range(len(data)):
            if data[j] != data[i]:
                if data[j] > data[i]:
                    left += 1
                else:
                    right += 1
        if left == right:
            return data[left]


res = find_median_simple(ARRAY)
print(res)
