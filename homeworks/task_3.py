# Пользователь вводит две буквы. Определить, на каких местах алфавита они стоят и сколько между ними находится букв.
str = input('Введите две буквы:')
c1, c2 = str
place1 = ord(c1) - 96
place2 = ord(c2) - 96

if place1 > place2:
    dif = place1 - place2 - 1
else:
    dif = place2 - place1 - 1
print(f'Порядковый номер первой буквы: {place1}')
print(f'Порядковый номер второй буквы: {place2}')

# здесь я просто делаю красивый вывод количества букв между введенными буквами, на блок-схеме все что ниже - блок "вывод"
if dif == 1 or dif == 21:
    print(f'Между буквами находится {dif} буква.')
else:
    print(f'Между буквами находится {dif} букв.')
