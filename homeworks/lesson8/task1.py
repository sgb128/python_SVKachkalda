"""
1) Реализовать класс «Дата», функция-конструктор которого должна принимать дату в виде строки формата «день-месяц-год».

В рамках класса реализовать два метода.

2) Первый, с декоратором @classmethod, должен извлекать число, месяц, год и преобразовывать их тип к типу «Число».

3) Второй, с декоратором @staticmethod, должен проводить валидацию числа, месяца и года (например, месяц — от 1 до 12).

Проверить работу полученной структуры на реальных данных.
"""
import re
class MyDate:

    def __init__(self, p_date: str):
        self.date = p_date
        self.day = 0
        self.month = 0
        self.year = 0

    @classmethod
    def parse_date(cls, other):
        if isinstance(other, cls):
            str_date = re.match(r'(\d{1,2}-\d{1,2}-\d{4}|\d{2}){1}', other.date).group()
            if str_date:
                result = [int(item) for item in str_date.split('-')]
                if MyDate.is_valid(result):
                    other.day = result[0]
                    other.month = result[1]
                    other.year = result[2]
                else:
                    raise TypeError('Ошибка переданного аргумента. Неверное количество дней в месяце или номер месяца')
            else:
                raise TypeError('Ошибка переданного аргумента. Аргумент не удовлетворяет шаблону.')
        else:
            raise TypeError('Ошибка переданного аргумента. Аргумент неверного типа.')

    @staticmethod
    def is_valid(date:list):
        if date[1] in range(1, 13):
            # не пугайтесь, это формула которая позволяет узнать в каком месяце сколько будет дней в любом году (не проверял),
            # хотя сам тоже почти до этого догадался в одном из предыдущих уроков, когда нужно было соотнести месяцы и
            # времена года, только там формула была попроще
            # взята отсюда: https://habr.com/ru/post/261773/
            days_in_month = 28 +\
                            ((date[1] + int(date[1] / 8)) % 2) +\
                            2 % date[1] +\
                            int((1 + (1 - (date[2] % 4 + 2) % (date[2] % 4 + 1)) *
                                  ((date[2] % 100 + 2) % (date[2] % 100 + 1)) +
                                  (1 - (date[2] % 400 + 2) % (date[2] % 400 + 1))) / date[1]) +\
                            int(1 / date[1]) -\
                            int(((1 - (date[2] % 4 + 2) % (date[2] % 4 + 1)) *
                                   ((date[2] % 100 + 2) % (date[2] % 100 + 1)) +
                                   (1 - (date[2] % 400 + 2) % (date[2] % 400 + 1))) / date[1])

            if date[0] in range(1, days_in_month + 1):
                return True
            else:
                raise TypeError('Ошибка переданного аргумента. Неверное количество дней в месяце.')
        else:
            raise TypeError('Ошибка переданного аргумента. Неверный номер месяца.')


    def __str__(self):
        return str(self.day) + '/' + str(self.month) + '/' + str(self.year)

c_date = MyDate('22-05-2345')
MyDate.parse_date(c_date)
print(c_date)

try:
    c_date = MyDate('32-05-2345')
    MyDate.parse_date(c_date)
    print(c_date)
except TypeError as e:
    print(e)

try:
    c_date = MyDate('22-13-2345')
    MyDate.parse_date(c_date)
    print(c_date)
except TypeError as e:
    print(e)
