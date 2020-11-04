def f_sum_list(*args):
    """
    f_sum_list предназначена для получения суммы из входных аргументов, а так же проверка аргумента на наличие спецсимвола
    :param args: int, float или str неограниченное количество
    :return: int или float, bool
    """
    v_sum = 0
    b_exit = False
    for i_item in args:
        try:
            v_sum += float(i_item) if i_item else 0
        except ValueError:
            if i_item.count('n') > 0:
                b_exit = not b_exit
                break
    return v_sum, b_exit

vb_exit = False
v_result  = 0
while not vb_exit:
    s_str_of_numbers = input('Введите числа через пробел:')
    vn_sum, vb_exit = f_sum_list(*s_str_of_numbers.split(' '))
    v_result += vn_sum
print(v_result)