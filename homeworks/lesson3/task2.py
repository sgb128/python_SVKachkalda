def f_resume(**kwargs):
    """
    f_resume принимает любые ИМЕНОВАННЫЕ параметры и выводит их данные в одну строку
    :param kwargs: именованные параметры любого типа
    :return: строка str
    """
    s_str = ''
    # В условиях задачи не совсем понятно сказано, что именно все-таки выводить: значения или ключ + значение
    # поэтому делаю и так и так
    for v_key, v_val in kwargs.items():
        s_str += str(v_key) + ': ' + str(v_val) + ', '
    print(s_str[:-2])# -2 потому что в конце строки после обработки словаря добавятся 2 лишних символа, их и убираем

    s_str = ''
    for v_val in kwargs.values():
        s_str += str(v_val) + ', '
    print(s_str[:-2])

f_resume(name='Ivan', surname='Ivanov', city='Moscow', age=30)