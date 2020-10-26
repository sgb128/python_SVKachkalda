v_prompt = 'Введите целое число n: '
v_number = str(input(v_prompt))
result = str(int(v_number) + int(v_number*2) + int(v_number*3))
print('Результат {0} + {0}{0} + {0}{0}{0}: {1}'.format(v_number, result))
