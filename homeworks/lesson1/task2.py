v_prompt = 'Введите время в секундах: '
v_int_seconds = int(input(v_prompt))
hours = v_int_seconds // 60 // 60
minutes = v_int_seconds // 60 % 60
seconds = v_int_seconds % 60

result = '{0}:{1}:{2}'

print(result.format(hours, minutes, seconds))
