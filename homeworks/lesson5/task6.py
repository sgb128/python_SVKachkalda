import os
# путь к файлу
p_data = os.path.join(os.path.dirname(__file__), 'task6.txt')
d_dict = {}
with open(p_data, 'r', encoding='UTF-8') as f_file:
    for v_line in f_file:
        # сделал так чтобы было видно, что я понял что происходило в цикле
        # заодно от лишних переменных избавился
        # да, знаю что некрасиво, обещаю что больше так не буду. просто спать уже охота
        d_dict[v_line.split(' ')[0].split(':')[0]] = sum(int(v_item.split('(')[0]) for v_item in v_line.split(' ')[1:] if v_item.split('(')[0].isdigit())
print(d_dict)