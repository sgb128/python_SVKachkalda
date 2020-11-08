"""
Представлен список чисел. Необходимо вывести элементы исходного списка, значения которых больше предыдущего элемента.
Подсказка: элементы, удовлетворяющие условию, оформить в виде списка. Для формирования списка использовать генератор.
Пример исходного списка: [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55].
Результат: [12, 44, 4, 10, 78, 123].
"""
def f_some_elements(*args):
    v_prev = float('inf')
    for v_val in args:
        if v_val > v_prev:
            yield v_val
        v_prev = v_val

v_list = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
print(v_list)
v_result = list(f_some_elements(*v_list))
print(v_result)

v_list = v_result[:]
v_result = list(f_some_elements(*v_list))
print(v_result)

v_list = v_result[:]
v_result = list(f_some_elements(*v_list))
print(v_result)

v_list = v_result[:]
v_result = list(f_some_elements(*v_list))
print(v_result)

v_list = v_result[:]
v_result = list(f_some_elements(*v_list))
print(v_result)

v_list = v_result[:]
v_result = list(f_some_elements(*v_list))
print(v_result)
