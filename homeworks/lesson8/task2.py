"""
Создайте собственный класс-исключение, обрабатывающий ситуацию деления на нуль.
Проверьте его работу на данных, вводимых пользователем.
При вводе пользователем нуля в качестве делителя программа должна корректно обработать эту ситуацию и не завершиться с ошибкой.
"""
def f_check_prompt(p_prompt: str = 'Введите число:') -> float:
    """
    f_check_prompt выполняет запрос данных у пользователя и проверяет является ли эти данные вещественным типом.
    В случае успеха - возвращает число типа float, в противном случае запрашивает ввод пока пользователь не введет
    число.
    :param p_prompt: строка, приглашение ко вводу
    :return:
    """
    v_value = ''
    while True:
        try:
            v_value = float(input(p_prompt))
            break
        except ValueError:
            # мне нужно чтобы цикл не останавливался, поэтому print
            print('Вы ввели не число! Повторите ввод!')
    return v_value


class ZeroDivideError(Exception):
    def __init__(self, text_error='Нельзя делить на 0! А вы знали что ламповые компьютеры могли взорваться от такой операции?'):
        self.__text_error = text_error

    # переопределил метод чтобы выводилось сообщение "по умолчанию"
    def __str__(self):
        return self.__text_error
# end class ZeroDivideError

a = f_check_prompt('jgfjgfghvghv')
b = f_check_prompt()
try:
    if not b:
        raise ZeroDivideError
    c = a / b
except ZeroDivideError as msg:
    print('Перехвачена ошибка ZeroDivideError:', msg)
else:
    print(c)
