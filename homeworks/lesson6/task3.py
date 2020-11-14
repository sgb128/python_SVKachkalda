"""
Реализовать базовый класс Worker (работник), в котором определить атрибуты: name, surname, position (должность),
income (доход). Последний атрибут должен быть защищенным и ссылаться на словарь, содержащий элементы: оклад и премия,
например, {"wage": wage, "bonus": bonus}.

Создать класс Position (должность) на базе класса Worker.

В классе Position реализовать методы получения полного имени сотрудника (get_full_name) и дохода с
учетом премии (get_total_income).

Проверить работу примера на реальных данных (создать экземпляры класса Position,
передать данные, проверить значения атрибутов, вызвать методы экземпляров).
"""

class Worker:

    # в этом классе мы можем задать только имя и фамилию
    # остальные параметры будут "пустые"
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.position = ''
        self._income = {'wage': 0, 'bonus': 0}

class Position(Worker):

    # в этом классе задаются параметры наследованные из предыдущего класса
    # но в этот раз мы задаем все параметры
    def __init__(self, position, name, surname, wage, bonus):
        super().__init__(name, surname)
        self.position = position
        self._income['wage'] = wage
        self._income['bonus'] = bonus

    # возвращаем имя и фамилию
    def get_full_name(self):
        return self.name + ' ' + self.surname

    # возвращаем общую зарплату
    def get_total_income(self):
        return self._income['wage'] + self._income['bonus']

if __name__ == '__main__':
    client_person = Position('Слесарь', 'Иван', 'Иванов', 10000, 5000)

    print(client_person.get_full_name())
    print(client_person.get_total_income())