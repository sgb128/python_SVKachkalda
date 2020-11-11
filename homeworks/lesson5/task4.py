# файл не должен содержать лишних строк, в противном случае выдаст ошибку при попытке записать пустые значения в словарь
import os
# путь к файлу
p_data = os.path.join(os.path.dirname(__file__), 'task4.txt')

d_replace = {'one': 'один', 'two': 'два', 'three': 'три', 'four': 'четыре'}

with open(p_data, 'r', encoding='UTF-8') as f_file:
    d_data = dict([values.split(' - ') for values in f_file.readlines()])

with open(p_data, 'a', encoding='UTF-8') as f_file:
    f_file.write('\n')
    for key in d_data:
        f_file.write(d_replace[str(key).lower()] + ' - ' + d_data[key])
