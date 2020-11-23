"""
Реализовать проект «Операции с комплексными числами».

Создайте класс «Комплексное число», реализуйте перегрузку методов сложения и умножения комплексных чисел.

Проверьте работу проекта, создав экземпляры класса (комплексные числа) и выполнив сложение и умножение созданных экземпляров.

Проверьте корректность полученного результата.
"""

class Complex:
    def __init__(self, re, im=0):
        self.re = re
        self.im = im

    def __str__(self):
        return f'({self.re}{" + " if self.im > 0 else " - "}{abs(self.im)}i)'

    def __add__(self, other):
        return Complex(self.re + other.re, self.im + other.im)

    def __mul__(self, other):
        re = (self.re * other.re) - (self.im * other.im)
        im = (self.re * other.im) + (self.im * other.re)
        return Complex(re, im)

if __name__ == '__main__':

    a = Complex(1, 2)
    b = Complex(3, 4)
    c = a + b
    c1 = a * b
    print(f'{a} + {b} = {c}')
    print(f'{a} * {b} = {c1}')

    a = Complex(1, -2)
    b = Complex(-3, 4)
    c = a + b
    c1 = a * b
    print(f'{a} + {b} = {c}')
    print(f'{a} * {b} = {c1}')
