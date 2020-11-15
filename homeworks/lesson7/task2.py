"""
Реализовать проект расчета суммарного расхода ткани на производство одежды.
Основная сущность (класс) этого проекта — одежда, которая может иметь определенное название.
К типам одежды в этом проекте относятся пальто и костюм.
У этих типов одежды существуют параметры: размер (для пальто) и рост (для костюма).
Это могут быть обычные числа: V и H, соответственно.

Для определения расхода ткани по каждому типу одежды использовать формулы:
                                                                          для пальто (V/6.5 + 0.5)
                                                                          для костюма (2 * H + 0.3)
Проверить работу этих методов на реальных данных.

Реализовать общий подсчет расхода ткани.
Проверить на практике полученные на этом уроке знания: реализовать абстрактные классы для основных классов проекта,
проверить на практике работу декоратора @property.
"""

from abc import ABC, abstractmethod, abstractproperty

class ClothAbstract(ABC):
    # я решил схитрить и определил общий список для всех дочерних классов, и у каждого экземпляра будет свой
    # индекс в этом списке
    __total = []

    def __init__(self, name):
        self.name = name
        self.__val = 0
        self.__ind = -1


    @property
    def all_rates(self):
        return self.__total

    @property
    def rate(self):
        return self.__val

    @rate.setter
    def rate(self, value):
        self.__val = value

    @abstractmethod
    def issue_rate(self, val):
        if self.__ind == -1:
            self.__total.append(self.rate)
        else:
            self.__total[self.__ind] = self.rate
# end class ClothAbstract

class Coat(ClothAbstract):

    def __init__(self, name):
        self.__type = 'пальто'
        super().__init__(name)

    def issue_rate(self, val: int):
        self.rate = round((val / 6.5 + 0.5), 2)
        super().issue_rate(self.rate)

    def __str__(self):
        return f'{self.__type.title()} {self.name}'
# end class Coat

class Suit(ClothAbstract):

    def __init__(self, name):
        self.__type = 'костюм'
        super().__init__(name)

    def issue_rate(self, val: int):
        self.rate = 2 * val + 0.3
        super().issue_rate(self.rate)

    def __str__(self):
        return f'{self.__type.title()} {self.name}'
# end class Suit

coat = Coat('обычное')
suit = Suit('повседневный')

print(coat)
print(suit)

coat.issue_rate(53)
suit.issue_rate(2)

print(f'Необходимо для пальто: {coat.rate}')
print(f'Необходимо для костюма: {suit.rate}')
# уж не знаю насколько правильно это или нет, но это избавило меня от необходимости писать для этого отдельный метод
print(f'Всего требуется ткани: {sum(coat.all_rates)}')