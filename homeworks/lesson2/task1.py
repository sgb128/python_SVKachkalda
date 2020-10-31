# этого конечно еще не было в уроках, поискав в интернете как работать с датой - нашел вот это:
import datetime

# собираю список
v_list = [1, 2, 3, 'a', 's', 'd', [True, False]]

# ну чтобы не все было указано на прямую - на всякий случай добавляю элемент в конец списка
v_list.append(datetime.date(2020, 10, 28))

# функции еще не изучали, так бы через рекурсивную вывел бы типы каждого элемента включая вложенный список
for v_iterator1 in list(range(0,len(v_list))):                # функцию range подсмотрел в интернете
    if str(type(v_list[v_iterator1])) == '<class \'list\'>':  # если тип элемента является списком то обходим его
        for v_iterator2 in list(range(0, len(v_list[v_iterator1]))):
            print( # вот еще 1 вопрос: строка оказывается достаточно длинная. Корректно ли оформление ниже?
                'Номер элемента вложенного списка: '
                + str(v_iterator1) + ':' + str(v_iterator2)
                + ' Значение: '
                + str(v_list[v_iterator1][v_iterator2])
                + ' Тип: '+ str(type(v_list[v_iterator1][v_iterator2])))
    else:
        print(
            'Номер элемента: '
            + str(v_iterator1)
            + ' Значение: '
            + str(v_list[v_iterator1])
            + ' Тип: '
            + str(type(v_list[v_iterator1]))
             )