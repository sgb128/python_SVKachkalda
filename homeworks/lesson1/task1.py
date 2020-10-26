s_initialised_in_pr_code = 'Строка инициализированная в программном коде.'
print(s_initialised_in_pr_code);
s_from_user_input = input('Введите строку: ')
print('Строка введенная пользователем: ' + s_from_user_input)
n_initialised_in_pr_code = 10
print('Целое число инициализированное в программном коде: {0}'.format(n_initialised_in_pr_code))
n_from_user_input = int(input('Введите целое число: '))
print('Целое число введеное пользователем: {0}'.format(n_from_user_input))
f_initialised_in_pr_code = 10.0
print('Вещественное число инициализированное в программном коде: {0}'.format(f_initialised_in_pr_code))
f_from_user_input = float(input('Введите число с плавающей точкой: '))
print('Вещественное число введенное пользователем: {0}'.format(f_from_user_input))
s_concat = s_initialised_in_pr_code + ' ' + s_from_user_input
print('Сконкатенированная строка:\n' + s_concat)

# операции с целыми числами
print('\nОперации с целыми числами:')
sp_int_and_int = 'Умножение чисел: {0}'
print(sp_int_and_int.format(n_initialised_in_pr_code * n_from_user_input))
sp_int_and_int = 'Сложение чисел: {0}'
print(sp_int_and_int.format(n_initialised_in_pr_code + n_from_user_input))
sp_int_and_int = 'Разность чисел: {0}'
print(sp_int_and_int.format(n_initialised_in_pr_code - n_from_user_input))
sp_int_and_int = 'Частное чисел: {0}'
print(sp_int_and_int.format(n_initialised_in_pr_code / n_from_user_input))
sp_int_and_int = 'Целочисленное деление чисел: {0}'
print(sp_int_and_int.format(n_initialised_in_pr_code // n_from_user_input))
sp_int_and_int = 'Остаток от целочисленного деления чисел: {0}'
print(sp_int_and_int.format(n_initialised_in_pr_code % n_from_user_input))

# операции с вещественными числами
print('\nОперации с вещественными числами:')
sp_int_and_int = 'Умножение чисел: {0}'
print(sp_int_and_int.format(f_initialised_in_pr_code * f_from_user_input))
sp_int_and_int = 'Сложение чисел: {0}'
print(sp_int_and_int.format(f_initialised_in_pr_code + f_from_user_input))
sp_int_and_int = 'Разность чисел: {0}'
print(sp_int_and_int.format(f_initialised_in_pr_code - f_from_user_input))
sp_int_and_int = 'Частное чисел: {0}'
print(sp_int_and_int.format(f_initialised_in_pr_code / f_from_user_input))
sp_int_and_int = 'Целочисленное деление чисел: {0}'
print(sp_int_and_int.format(f_initialised_in_pr_code // f_from_user_input))
sp_int_and_int = 'Остаток от целочисленного деления чисел: {0}'
print(sp_int_and_int.format(f_initialised_in_pr_code % f_from_user_input))
