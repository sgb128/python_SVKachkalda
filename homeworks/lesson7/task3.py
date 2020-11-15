"""
Реализовать программу работы с органическими клетками.
Необходимо создать класс Клетка.
В его конструкторе инициализировать параметр, соответствующий количеству клеток (целое число).
В классе должны быть реализованы методы перегрузки арифметических операторов:
                                                                             сложение (__add__()),
                                                                             вычитание (__sub__()),
                                                                             умножение (__mul__()),
                                                                             деление (__truediv__()).
Данные методы должны применяться только к клеткам и выполнять увеличение, уменьшение, умножение
и обычное (не целочисленное) деление клеток, соответственно.
В методе деления должно осуществляться округление значения до целого числа.

Сложение. Объединение двух клеток. При этом число ячеек общей клетки должно равняться сумме ячеек исходных двух клеток.
Вычитание. Участвуют две клетки. Операцию необходимо выполнять только если разность количества ячеек двух клеток больше нуля, иначе выводить соответствующее сообщение.
Умножение. Создается общая клетка из двух. Число ячеек общей клетки определяется как произведение количества ячеек этих двух клеток.
Деление. Создается общая клетка из двух. Число ячеек общей клетки определяется как целочисленное деление количества ячеек этих двух клеток.

В классе необходимо реализовать метод make_order(), принимающий экземпляр класса и количество ячеек в ряду.
Данный метод позволяет организовать ячейки по рядам.
Метод должен возвращать строку вида
*****\n
*****\n
*****
...
**
, где количество ячеек между \n равно переданному аргументу.
Если ячеек на формирование ряда не хватает, то в последний ряд записываются все оставшиеся.
Например, количество ячеек клетки равняется 12, количество ячеек в ряду — 5.
Тогда метод make_order() вернет строку:
*****\n
****\n
**.
Или, количество ячеек клетки равняется 15, количество ячеек в ряду — 5.
Тогда метод make_order() вернет строку:
*****\n
*****\n
*****.
"""
import inspect
# столько всего написано, а оказалось все так просто
class BioCell:

    def __init__(self, count: int):
        self.__count = count

    # для красоты, подсмотрел в интернете
    def getVarName(self):
        for i in inspect.currentframe().f_back.f_locals.items():
            if id(self) == id(i[1]):
                return i[0]

    # проверочка на "вшивость"
    def __check_bio_cell(self, other):
        if not isinstance(other, BioCell):
            raise TypeError('Ошибка. Неверный аргумент.')

    # сложение(__add__())
    def __add__(self, other):
        self.__check_bio_cell(other)
        return BioCell(self.__count + other.__count)

    # вычитание(__sub__()),
    def __sub__(self, other):
        self.__check_bio_cell(other)
        if (self.__count - other.__count) > 0:
            return BioCell(self.__count - other.__count)
        else:
            raise Exception('Вы не можете отнять больше клеток чем есть в наличии. :)')

    # умножение(__mul__()),
    def __mul__(self, other):
        self.__check_bio_cell(other)
        return BioCell(self.__count * other.__count)

    # деление(__truediv__()).
    def __floordiv__(self, other):
        self.__check_bio_cell(other)
        if self.__count == 0:
            raise Exception('В теории вы можете делить 0 на сколько угодно частей, но на практике вам нечего делить!')
        if other.__count == 0:
            raise Exception('Нельзя разделить на ничто.')
        return BioCell(self.__count // other.__count)

    # ячейки по рядам
    def make_order(self, count_in_string):
        strings = self.__count // count_in_string
        remind = self.__count % count_in_string
        return ('*' * count_in_string + '\n') * strings + ('*' * remind)

    def __str__(self):
        return str(self.__count)
# end class BioCell

#итак, проверочки, поехали...
a = BioCell(11)
b = BioCell(12)
c = BioCell(13)
d = BioCell(14)
e = BioCell(5)
f = BioCell(6)
g = BioCell(17)
h = BioCell(18)
h1 = BioCell(0)
# создали ячейки, теперь операции:
# я решил дописать вывод в сами операции, просто лень каждый раз здесь писать print()...
# сложение
print(f'сложение {a.getVarName()}={a} и {b.getVarName()}={b}')
i = a + b
print(i)
# вычитание из меньшего
print(f'вычитание {c.getVarName()}={c} из {d.getVarName()}={d}')
try:
    j = c - d
except Exception as exc:
    print(exc)
# вычитание из большего
print(f'вычитание {d.getVarName()}={d} из {c.getVarName()}={c}')
k = d - c
print(k)
# умножение
print(f'умножение {e.getVarName()}={e} и {f.getVarName()}={f}')
l = e * f
print(l)
# деление
print(f'деление {h.getVarName()}={h} на {g.getVarName()}={g}')
m = h // g
print(m)
print(f'деление {h1.getVarName()}={h1} на {h.getVarName()}={h}')
try:
   n = h1 // h
except Exception as exc:
    print(exc)

print('Результат i')
print(i.make_order(5))
print('Результат k')
print(k.make_order(7))
print('Результат l')
print(l.make_order(8))
print('Результат m')
print(m.make_order(9))
