"""
Написать программу сложения и умножения двух положительных целых шестнадцатеричных чисел.
При этом каждое число представляется как коллекция, элементы которой — цифры числа.
Например, пользователь ввёл A2 и C4F.
Нужно сохранить их как [‘A’, ‘2’] и [‘C’, ‘4’, ‘F’] соответственно.
Сумма чисел из примера: [‘C’, ‘F’, ‘1’], произведение - [‘7’, ‘C’, ‘9’, ‘F’, ‘E’].
"""
from collections import defaultdict, deque


def sum_16(in_a: list, in_b: list):
    c = deque()
    rank = 0
    l_a = len(in_a)
    l_b = len(in_b)
    if l_a > l_b:
        la = l_a
        lb = l_b
        a = in_a
        b = in_b
    else:
        la = l_b
        lb = l_a
        a = in_b
        b = in_a

    for i in range(la):
        if i < lb:
            tmp = X16[a[la - i - 1]] + X16[b[lb - i - 1]] + rank
            rank = 0
            if tmp > 15:
                tmp -= 16
                c.appendleft(S16[tmp])
                rank = 1
            else:
                c.appendleft(S16[tmp])
        else:
            c.appendleft(S16[X16[a[la - i - 1]] + rank])
            rank = 0
    return c


def pr_16(a: list, b: list):
    c = deque()
    la = len(a)
    lb = len(b)
    t_var = []
    for i in range(lb):
        for j in range(la):
            tmp = X16[a[la - j - 1]] * X16[b[lb - i - 1]]
            if tmp > 15:
                tmp_rem = tmp % 16
                tmp //= 16
                c.appendleft(S16[tmp_rem])
                c.appendleft(S16[tmp])
            else:
                c.appendleft(S16[tmp])

            if i or j:
                c.extend([0] * (i + j))
            if not len(t_var):
                t_var = c
                # print(f'{i=}, {j=}, {t_var}')
            else:
                # print(f'{i=}, {j=}, {t_var} + {c}')
                t_var = sum_16(t_var, c)
            c = deque()
    return t_var


# Константные значения (надо наверное было в самый верх переместить?)  АААа... пойду читать дзен...
X16 = defaultdict(int)
S16 = defaultdict(str)
S = '0123456789ABCDEF'

for v, char in enumerate(S):
    X16[char] = v

for v, char in enumerate(S):
    S16[v] = char


a_ = ['A', '2']
b_ = ['C', '4', 'F']

d = sum_16(a_, b_)
f = pr_16(a_, b_)
print('Сумма чисел ', end='')
print(*a_, sep='', end='')
print(' и ', end='')
print(*b_, sep='', end='')
print(' равна ', end='')
print(*d, sep='')
print('Произведение чисел ', end='')
print(*a_, sep='', end='')
print(' и ', end='')
print(*b_, sep='', end='')
print(' равно ', end='')
print(*f, sep='')

