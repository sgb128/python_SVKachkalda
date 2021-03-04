"""
В диапазоне натуральных чисел от 2 до 99 определить, сколько из них кратны каждому из чисел в диапазоне от 2 до 9.
"""
MIN_VAL = 2
MIN_DIVIDER = 2
MAX_VAL = 99
MAX_DIVIDER = 9

r = MIN_DIVIDER
c = MIN_VAL
while r <= MAX_DIVIDER:
    rez = MAX_VAL//r - MIN_VAL//r
    if not MIN_VAL % r:
        rez += 1

    # для корректного вывода
    if rez % 10 in (2, 3, 4) and (14 < rez or rez < 12):
        s_num = 'числа!'
    elif rez % 10 == 1 and rez != 11:
        s_num = 'число!'
    else:
        s_num = 'чисел!'

    print(f'Числу {r} кратны {rez} ' + s_num)
    r += 1
