"""
Среди натуральных чисел, которые были введены, найти наибольшее по сумме цифр.
Вывести на экран это число и сумму его цифр.
"""
def sum_nums(x):
    if x//10 == 0:
        return x
    return x%10 + sum_nums(x//10)

num_max = 0
sum_max = 0
num = int(input('Введите натуральное число:'))
while num != 0:
    sum_n = sum_nums(num)
    if sum_n > sum_max:
        num_max, sum_max = num, sum_n
    num = int(input('Введите натуральное число:'))
print(f'Число с наибольшей суммой цифр: {num_max}, сумма его цифр составляет:{sum_max}')
