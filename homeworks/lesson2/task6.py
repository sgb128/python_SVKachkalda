d_prompt = {'name': 'Введите наименование товара:', 'price': 'Введите стоимость товара:', 'quant': 'Введите количество товара:', 'meas_mnemo': 'Введите единицу измерения:'}
d_goods = {}
d_anl_goods = {}
l_anl_goods = []
l_goods = []
#заполненный список на случай если лень вводить
#l_goods = [(1, {'название': 'компьютер', 'цена': 20000, 'количество': 5, 'eд': 'шт.'}),
#           (2, {'название': 'принтер', 'цена': 6000, 'количество': 2, 'eд': 'шт.'}),
#           (3, {'название': 'сканер', 'цена': 2000, 'количество': 7, 'eд': 'шт.'})]
vs_exit = ''
l_exit = ['нет', 'no', 'n', 'н']
v_number = 0
while vs_exit.lower() not in l_exit:
    for v_key, v_value in d_prompt.items():
        d_goods[v_key] = input(v_value)
    v_number += 1
    t_goods = v_number, d_goods
    l_goods.append(t_goods)
    vs_exit = input('Желаете еще добавить товар? (Enter - да/чтобы закончить введите "нет" и нажмите Enter)')
l_anl = list(l_goods[0][1])
for val in l_anl:
    for item in l_goods:
        d_anl_goods[val] = []
for val in l_anl:
    for item in l_goods:
        d_anl_goods[val].append(item[1][val])
print(d_anl_goods)