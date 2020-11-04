# использую процедуру проверки ввода из первого задания
def f_check_prompt(p_prompt: str = 'Введите число:') -> float:
    """
    f_check_prompt выполняет запрос данных у пользователя и проверяет является ли эти данные вещественным типом.
    В случае успеха - возвращает число типа float, в противном случае запрашивает ввод пока пользователь не введет
    число.
    :param p_prompt: строка, приглашение ко вводу
    :return:
    """
    while True:
        try:
            v_value = float(input(p_prompt))
            break
        except ValueError:
            print('Вы ввели не число! Повторите ввод!')
    return v_value

# функция, которую требуется написать в задании 3
def f_sum_greater(arg1: float, arg2: float, arg3: float) -> float:
    """
    f_sum_greater принимает в качестве аргументов 3 любых числа, и складывает самые большие из них
    :param arg1: число тип float или int
    :param arg2: число тип float или int
    :param arg3: число тип float или int
    :return: число тип float или int
    """
    def f_greater(*args) -> list:
        """
        f_greater список из 2-х наибольших аргументов по значению учитывая знак
        :param args: числа тип float или int
        :return: возвращает list из 2х значений
        """
        # упорядочим список используя свойство множеств, так же заодно удалим дубли (1 выстрелом 2 зайца)
        # никаких циклов, никаких "пузырьковых" методов и тому подобное
        v_list = list(set(args))
        # список в который будут записываться наши значения
        v_res = []
        # если самое большое значение в отсортированном списке встречается хотя бы 2 раза в исходном списке
        # то в итоговый список записываем это значение как 2 самых больших
        # в противном случае пишем в итоговый список 2 последних значения отсортированного списка
        if args.count(v_list[len(v_list) - 1]) > 1:
            v_res.append(v_list[len(v_list) - 1])
            v_res.append(v_list[len(v_list) - 1])
        else:
            v_res.append(v_list[len(v_list) - 2])
            v_res.append(v_list[len(v_list) - 1])
        return v_res

    # получаем 2 самых больших значения из наших аргументов
    val_1, val_2 = f_greater(arg1, arg2, arg3)
    # складываем и возвращаем
    return val_1 + val_2

v_arg1 = f_check_prompt()
v_arg2 = f_check_prompt()
v_arg3 = f_check_prompt()

print(f_sum_greater(v_arg1, v_arg2, v_arg3))

