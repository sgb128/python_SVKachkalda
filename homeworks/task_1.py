"""
Пользователь вводит данные о количестве предприятий, их наименования и прибыль за 4 квартал (т.е. 4 числа)
для каждого предприятия. Программа должна определить среднюю прибыль (за год для всех предприятий)
и отдельно вывести наименования предприятий, чья прибыль выше среднего и ниже среднего.
"""
# я оставил модули, которые пробовал для решения задачи.
from collections import namedtuple, defaultdict, Counter

orgs = Counter()
n = int(input('Введите количество организаций:'))
s = 0
for i in range(n):
    org_name = input('Введите название организации:')
    for q in range(4):
        orgs[org_name] += int(input(f'Сумма организации {org_name} за {q+1}-й квартал:'))
    orgs[org_name] /= 4

avg_sum = sum(orgs.values()) / len(orgs)

print(f'Средняя прибыль всех организаций за год: {avg_sum}')
i = False
j = True
for key, val in orgs.most_common():
    if val < avg_sum and j:
        j = not j
    if not i and val > avg_sum:
        print('Организации с прибылью выше средней:')
        i = not i
    if not j and val < avg_sum:
        print('Организации с прибылью ниже средней:')
        j = not j
    print(f'Наименование организации:' + key + f'. Среднегодовой доход: {val}')
