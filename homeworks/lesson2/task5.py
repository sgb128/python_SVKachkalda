import math
l_raiting = []
l_exit = ['нет', 'no', 'n', 'н']
vs_exit = ''
vn_user_number = int(input('Введите число:'))
vn_index = 0
while vs_exit.lower() not in l_exit:
    print(l_raiting)
    if len(l_raiting) == 0:
        l_raiting.append(vn_user_number)
    elif l_raiting.count(vn_user_number) > 0:
        l_raiting.insert(l_raiting.index(vn_user_number, l_raiting.count(vn_user_number) - 1), vn_user_number)
    elif vn_user_number == 0:
        l_raiting.append(vn_user_number)
    else:
        while l_raiting[vn_index] > vn_user_number:
            vn_index += 1
        l_raiting.insert(vn_index, vn_user_number)
    print('Рейтинг чисел:')
    print(l_raiting)
    vs_exit = input('Желаете продолжить? (да/нет):')

    if vs_exit.lower() not in l_exit:
        vn_user_number = int(input('Введите число:'))
