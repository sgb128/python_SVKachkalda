sp_proceeds = 'Введите сумму выручки: '
sp_costs = 'Введите сумму издержек: '
sp_count_workers = 'Введите количество сотрудников организации: '
v_costs = int(input(sp_costs))
v_proceeds = int(input(sp_proceeds))
v_profit = v_proceeds - v_costs
if v_profit > 0:
    print('Организация получила прибыль!')
    print('Рентабельность прибыли составила: {0}%'.format(round(v_profit / v_proceeds * 10000)/100))
    v_count_workers = int(input(sp_count_workers))
    v_profit_worker = round(v_profit / v_count_workers * 100) / 100
    print('Прибыль фирмы в расчете на одного сотрудника составила: {0} руб.'.format(v_profit_worker))
elif v_profit < 0:
    print('Организация в убытке!')
else:
    print('Организация отработала в 0!')
