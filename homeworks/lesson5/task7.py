import os
import json
# путь к файлу
p_data = os.path.join(os.path.dirname(__file__), 'task6.txt')
d_org = {}

with open('task7.txt', 'r', encoding='UTF-8') as f_file:
    for itm in f_file:
        items = itm.split(' ')
        d_org[items[0]] = int(items[2]) - int(items[3])
d_average = {'average_profit': sum(filter(lambda x: x >= 0, d_org.values())) / len(d_org)}
v_res = [d_org, d_average]

with open('task7.json', 'w') as f_file:
    json.dump(v_res, f_file, ensure_ascii=False)