vl_seasons = ['Зима', 'Весна', 'Лето', 'Осень']
vd_seasons = {0:'Зима', 1:'Весна', 2:'Лето', 3:'Осень'}
vs_month = input('Введите месяц в числовом формате:')

if not vs_month.isdigit():
    print('Вы ввели не число!')
elif int(vs_month) not in list(range(1,13)):
    print('Вы ввели число за пределами диапазона порадкового номера месяца!')
else:
    vn_month = int(vs_month)
    key = vn_month // 3 - 4 * ( vn_month // 12 )
    print('Решение через список:')
    print('Этот месяц относится к сезону "' + vl_seasons[key] + '"')
    print('Решение через словарь:')
    print('Этот месяц относится к сезону "' + vd_seasons[key] + '"')
