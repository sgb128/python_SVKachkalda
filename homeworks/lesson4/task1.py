"""
Реализовать скрипт, в котором должна быть предусмотрена функция расчета заработной платы сотрудника.
В расчете необходимо использовать формулу: (выработка в часах * ставка в час) + премия.
Для выполнения расчета для конкретных значений необходимо запускать скрипт с параметрами.
"""
import sys
_, v_rate_per_hour, v_output_per_hour, v_prize, *__ = sys.argv
try:
    v_salary = float(v_rate_per_hour) * float(v_output_per_hour) + float(v_prize)
except ValueError:
    print('Ошибка ввода!')
    v_salary = float('nan')

print(v_salary)