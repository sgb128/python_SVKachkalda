import os
# путь к файлу
p_data = os.path.join(os.path.dirname(__file__), 'task3.txt')
# считываем файл и записываем содержимое в словарь
with open(p_data, 'r', encoding='UTF-8') as f_file:
    d_data = dict( [ values.split( ':' ) for values in f_file.readlines() ] )
# считаем среднюю зп
n_average = sum( list( map( float, list( d_data.values() ) ) ) ) / len( d_data )
# ну и времени нет, завтра дедлайн а мне еще остальные задачи делать, так что вот так:
print('Сотрудники у которых низкий оклад:')
for key in d_data:
    if float(d_data[key]) < 20000:
        print(key)
print('Средний оклад: ' + str(n_average))