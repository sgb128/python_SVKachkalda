v_prompt = 'Введите целое положительное число: '
v_result = 'Самая большая цифра в веденном числе: {0}'
v_str_positive_number = str(input(v_prompt))
iterator = 0
result = -1
while iterator < len(v_str_positive_number):
    if int(v_str_positive_number[iterator]) > result:
        result = int(v_str_positive_number[iterator])
    iterator += 1

print(v_result.format(result))