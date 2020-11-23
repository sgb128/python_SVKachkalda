"""
4)  Начните работу над проектом «Склад оргтехники».
    Создайте класс, описывающий склад.
    А также класс «Оргтехника», который будет базовым для классов-наследников.
    Эти классы — конкретные типы оргтехники (принтер, сканер, ксерокс).
    В базовом классе определить параметры, общие для приведенных типов.
    В классах-наследниках реализовать параметры, уникальные для каждого типа оргтехники.

5)  Продолжить работу над первым заданием.
    Разработать методы, отвечающие за приём оргтехники на склад и передачу в определенное подразделение компании.
    Для хранения данных о наименовании и количестве единиц оргтехники, а также других данных, можно использовать
    любую подходящую структуру, например словарь.

6)  Продолжить работу над вторым заданием.
    Реализуйте механизм валидации вводимых пользователем данных.
    Например, для указания количества принтеров, отправленных на склад, нельзя использовать строковый тип данных.

    Подсказка: постарайтесь по возможности реализовать в проекте «Склад оргтехники» максимум возможностей, изученных на уроках по ООП.
"""
from abc import ABC, abstractmethod


def add_to_wh(warehouse, hardwars: list):
    if isinstance(warehouse, Warehouse):
        idx = 0
        while True:
            try:
                hardwars[idx].send_to_warehouse(warehouse)
            except IndexError:
                break
            idx += 1


class NotSend(Exception):
    def __init__(self, n_err, s_model = '', text_error=''):
        if n_err == 0:
            self.__text_error = text_error
        elif n_err == 1:
            self.__text_error = f'Устройство: Модель №:{s_model} не было отправлено организациям или подразделениям.'
        elif n_err == 2:
            self.__text_error = 'Еще ничего не отправлено.'

    def __str__(self):
        return self.__text_error


class PrintError(Exception):
    def __init__(self, n_err, text_error=''):
        if n_err == 0:
            self.__text_error = text_error
        elif n_err == 1:
            self.__text_error = 'Тип печати не определен.'
        elif n_err == 2:
            self.__text_error = 'Цвет печати не определен.'

    def __str__(self):
        return self.__text_error


class ScanError(Exception):
    def __init__(self, n_err, text_error=''):
        if n_err == 0:
            self.__text_error = text_error
        elif n_err == 1:
            self.__text_error = 'Разрешение сканирования не задано.'
        elif n_err == 2:
            self.__text_error = 'Разрешение сканера не задано.'

    def __str__(self):
        return self.__text_error


class QuantityError(Exception):
    def __init__(self, text_error='Количество должно быть целым числом.'):
        self.__text_error = text_error

    def __str__(self):
        return self.__text_error


class ObjectNotFound(Exception):
    def __init__(self, s_model='', text_error=''):
        if len(text_error) == 0:
            self.__text_error = f'Устройство: Модель №:"{s_model}" отсутствует на складе.'
        else:
            self.__text_error = text_error

    def __str__(self):
        return self.__text_error


class WarehouseIterator:

    def __init__(self, warehouse):
        self.warehouse = warehouse
        self.index = 0

    def __next__(self):
        while True:
            try:
                hardware = self.warehouse[self.index]
                self.index += 1
                return hardware
            except IndexError:
                raise StopIteration


class Warehouse:
    def __init__(self):
        self.__hardware = []
        self.__affiliations = []

    def __str__(self):
        result_string = ''
        for item in self.__hardware:
            result_string += str(item) + f'Количество: {self.count_hard(item.model)}\n\n'
        return result_string

    def __iter__(self):
        return WarehouseIterator(self.__hardware)

    def __getitem__(self, item):
        return self.__hardware[item]

    def count_hard(self, md):
        cnt = 0
        for idx, item in enumerate(self):
            if item.model == md:
                cnt += 1
        return cnt

    def index(self, md):
        for idx, item in enumerate(self):
            if item.model == md:
                return idx

    def add(self, other):
        self.__hardware.append(other)

    def print_org_devices(self):
        result_string = ''
        for item in self.__affiliations:
            result_string += str(item) + '\n'
        return result_string

    def pop(self, md):
        if self.count_hard(md):
            tmp = self.__hardware.pop(self.index(md))
            if tmp.get_type() == 'PRINTER':
                return Printer(tmp.brand, tmp.model, tmp.is_colored, tmp.print_type)
            elif tmp.get_type() == 'SCANNER':
                return Scanner(tmp.brand, tmp.model, tmp.resolution)
            elif tmp.get_type() == 'XEROX':
                return Xerox(tmp.brand, tmp.model, tmp.xerox_type, tmp.is_colored, tmp.resolution)
        else:
            raise ObjectNotFound(md)

    def find_aff(self, org, md):
        if len(self.__affiliations) > 0:
            for idx, item in enumerate(self.__affiliations):
                if (item.get_affiliation() == org or org == '') and item.model == md:
                    return idx
            raise NotSend(1, md)
        else:
            raise NotSend(2)

    def moveto_org(self, org, md):
        if self.count_hard(md):
            self.__affiliations.append(self.pop(md))
            self.__affiliations[self.find_aff('', md)].set_affiliation(org)
            print(f'Устройство передано. На складе осталось {self.count_hard(md)} шт.\n')
        else:
            raise ObjectNotFound(md)


# end class Warehouse

class OfficeEquipment(ABC):
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

        self.__affiliation = 'на складе'

    def send_to_warehouse(self, warehouse):
        if isinstance(warehouse, Warehouse):
            warehouse.add(self)

    def get_affiliation(self):
        return self.__affiliation if self.__affiliation is not None else 'на складе'

    def set_affiliation(self, org):
        self.__affiliation = org

    @abstractmethod
    def get_type(self):
        pass

    @abstractmethod
    def __str__(self):
        pass


# end class OfficeEquipment


class Printer(OfficeEquipment):
    __TYPE = 'PRINTER'

    def __init__(self, brand, model, is_colored: bool, print_type):
        super().__init__(brand, model)

        if print_type in ['matrix', 'jet', 'laser']:
            self.print_type = print_type
        else:
            raise PrintError(1)

        if isinstance(is_colored, bool):
            self.is_colored = is_colored
        else:
            raise PrintError(2)

    @classmethod
    def create_printers(cls, brand, quantity):
        if isinstance(quantity, int):
            return [cls(brand, brand[0:2].upper()+str('matrix' if rng % 3 == 0 else 'jet' if rng % 3 == 1 else 'laser')[0:2],
                    rng % 2 == 0, 'matrix' if rng % 3 == 0 else 'jet' if rng % 3 == 1 else 'laser') for rng in range(quantity)]
        else:
            raise QuantityError

    def get_type(self):
        return self.__TYPE

    @property
    def __print_color(self):
        return 'цветная' if self.is_colored else 'черно-белая'

    def __str__(self):
        return f'Тип устройства: {self.__TYPE}\n' \
               f'Бренд: {self.brand}\n' \
               f'Модель: {self.model}\n' \
               f'Цвет печати: {self.__print_color}\n' \
               f'Тип печати: {self.print_type}\n' \
               f'Местонахождение: {self.get_affiliation()}\n'

# end class Printer


class Scanner(OfficeEquipment):
    __TYPE = 'SCANNER'

    def __init__(self, brand, model, resolution):
        super().__init__(brand, model)

        if isinstance(resolution, int):
            self.resolution = resolution
        else:
            raise ScanError(2)

    def __str__(self):
        return f'Тип устройства: {self.__TYPE}\n' \
               f'Бренд: {self.brand}\n' \
               f'Модель: {self.model}\n' \
               f'Разрешение: {self.resolution}\n' \
               f'Местонахождение: {self.get_affiliation()}\n'

    @classmethod
    def create_scanners(cls, brand, quantity):
        if isinstance(quantity, int):
            return [cls(brand, brand[0:2].upper()+str((rng % 4)*10.1), rng * 50 + 50) for rng in range(quantity)]
        else:
            raise QuantityError

    def get_type(self):
        return self.__TYPE


# end class Scanner

class Xerox(OfficeEquipment):
    __TYPE = 'XEROX'

    def __init__(self, brand, model, xerox_type, is_colored: bool, resolution):
        super().__init__(brand, model)

        if xerox_type in ['matrix', 'jet', 'laser']:
            self.print_type = xerox_type
        else:
            raise PrintError(1)

        if isinstance(is_colored, bool):
            self.is_colored = is_colored
        else:
            raise PrintError(2)

        if isinstance(resolution, int):
            self.resolution = resolution
        else:
            raise ScanError(1)

    @classmethod
    def create_xeroxes(cls, brand, quantity):
        if isinstance(quantity, int):
            return [cls(brand, brand[0:2].upper()+str('matrix' if rng % 3 == 0 else 'jet' if rng % 3 == 1 else 'laser')[0:2],
                    'matrix' if rng % 3 == 0 else 'jet' if rng % 3 == 1 else 'laser', rng % 2 == 0, rng * 50 + 50) for rng in range(quantity)]
        else:
            raise QuantityError

    @property
    def __print_color(self):
        return 'цветная' if self.is_colored else 'черно-белая'

    def get_type(self):
        return self.__TYPE

    def __str__(self):
        return f'Тип устройства: {self.__TYPE}\n' \
               f'Бренд: {self.brand}\n' \
               f'Модель: {self.model}\n' \
               f'Цвет печати: {self.__print_color}\n' \
               f'Тип печати: {self.print_type}\n' \
               f'Разрешение: {self.resolution}\n' \
               f'Местонахождение: {self.get_affiliation()}\n'


# end class Xerox

if __name__ == '__main__':
    hardware = Warehouse()
    print('Валидация вводимых данных:')
    print('                                         Бренд   ,  Модель , количество, качество сканирования')
    print("Проверка качества сканирования: Scanner('Samsung', 'SM0123', 1         , '400'                )")
    try:
        samsung_scanner = Scanner('Samsung', 'SM0123', '400')
    except ScanError as qnt:
        print('Перехвачена ошибка ScanError:\n', qnt, '\n')
    finally:
        samsung_scanner = Scanner('Samsung', 'SM0123', 400)

    # ну и сгенерируем 5 сканеров Samsung
    samsung_scanners = Scanner.create_scanners('Samsung', 5)

    print('                               Бренд          ,  Модель , количество, цветопечать, тип печати')
    print("Проверка цветопечати: Printer('Невлет Раскард', 'HP001' , 1         , 1          , 'jet'     )")
    try:
        hp_printer = Printer('Невлет Раскард', 'HP001', 1, 'jet')
    except PrintError as per:
        print('Перехвачена ошибка PrintError:\n', per, '\n')

    print('                               Бренд          ,  Модель , количество, цветопечать, тип печати')
    print("Проверка типа печати: Printer('Невлет Раскард', 'HP001' , 1         , True       , 'laserjet')")
    try:
        hp_printer = Printer('Невлет Раскард', 'HP001', True, 'laserjet')
    except PrintError as per:
        print('Перехвачена ошибка PrintError:\n', per, '\n')
    finally:
        hp_printer = Printer('Невлет Раскард', 'HP001', True, 'jet')

    # так же сгенерируем 4 принтера HewlettPackard
    hp_printers = Printer.create_printers('HewlettPackard', 4)
    # и 3 штук ксероксов
    sony_xeroxes = Xerox.create_xeroxes('Sony', 3)

    # передадим то что по одному произвели
    hp_printer.send_to_warehouse(hardware)
    samsung_scanner.send_to_warehouse(hardware)

    # передадим то что произвели в контейнерах(списках)
    add_to_wh(hardware, hp_printers)
    add_to_wh(hardware, samsung_scanners)
    add_to_wh(hardware, sony_xeroxes)

    print("Получилось на складе:")
    print(hardware)

    print('Проверим отправлялось ли что-нибудь со склада:')
    try:
        hardware.find_aff('', 'HP002')
    except NotSend as nsd:
        print('Перехвачена ошибка NotSend:\n', nsd, '\n')

    print('Передача организации:\n')
    print('Сначала попробуем передать несуществующую модель: "qwerty"')
    try:
        hardware.moveto_org('ООО "Рога и копыта"', 'qwerty')
    except ObjectNotFound as onf:
        print('Перехвачена ошибка ObjectNotFound:\n', onf, '\n')

    print('Теперь передаем существующую модель "HP001":')
    hardware.moveto_org('ООО "Рога и копыта"', 'HP001')
    hardware.moveto_org('ООО "Рога и копыта"', 'HEma')
    print(hardware.print_org_devices())

    print('Проверим существует ли какая-нибудь другая модель устройства в организации:')
    try:
        hardware.find_aff('ООО "Рога и копыта"', 'HP002')
    except NotSend as nsd:
        print('Перехвачена ошибка NotSend:\n', nsd, '\n')

    print('Устройства на складе(если списка нет, значит я закомментировал команду и надо ее раскомментировать):\n')
    # print(hardware)