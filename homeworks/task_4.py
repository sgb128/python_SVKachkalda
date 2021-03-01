"""
Посчитать, сколько раз встречается определенная цифра в введенной последовательности чисел.
Количество вводимых чисел и цифра, которую необходимо посчитать, задаются вводом с клавиатуры.
"""
def cnt_numb(fnum, i, num = 0):
    if num != 0:
        if num%10 == fnum:
            return 1 + cnt_numb(fnum, i, num//10)
        else:
            return cnt_numb(fnum, i, num // 10)
    else:
        if i > 0:
            a = int(input('Введите число:'))
            return cnt_numb(fnum, i - 1, a)
        else:
            return 0

cnt = int(input('Введите количество чисел:'))
find_num = int(input('Введите искомое число:'))
rez = cnt_numb(find_num, cnt)
print(rez)