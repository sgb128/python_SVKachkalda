sp_start_value = 'Введите результат в первый день: '
sp_desired_result = 'Введите желаемый результат: '
v_start_value = int(input(sp_start_value))
v_desired_result = int(input(sp_desired_result))
v_result = v_start_value;
v_koef = 1.1
v_day = 1
print('{0}-й день: {1}'.format(v_day, round(v_result*100)/100))
while v_result < v_desired_result:
    v_result *= v_koef
    v_day += 1
    print('{0}-й день: {1}'.format(v_day, round(v_result*100)/100))
print('Ответ: на {0}-й день спортсмен достиг результата - не менее {1} км.'.format(v_day, v_desired_result))
