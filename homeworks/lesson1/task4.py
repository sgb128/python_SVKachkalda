vs_prompt = 'Введите целое положительное число: '
vs_result = 'Самая большая цифра в веденном числе: {0}'
vs_iterator = 'Количество циклов выполнено: {0}'
vpn_int_positive_number = int(input(vs_prompt))
vn_iterator = 0
vn_result = -1
while vpn_int_positive_number and vn_result != 9:
    if vn_result < vpn_int_positive_number % 10:
        vn_result = vpn_int_positive_number % 10
    vn_iterator += 1
    vpn_int_positive_number //= 10
print(vs_result.format(vn_result))
print(vs_iterator.format(vn_iterator))