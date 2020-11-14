"""
Реализуйте базовый класс Car.
У данного класса должны быть следующие атрибуты: speed, color, name, is_police (булево).
А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала, остановилась, повернула (куда).
Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar.
Добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля.
Для классов TownCar и WorkCar переопределите метод show_speed.
При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.

Создайте экземпляры классов, передайте значения атрибутов.
Выполните доступ к атрибутам, выведите результат.
Выполните вызов методов и также покажите результат.
"""

class Car:

    __is_car_go = False

    def __init__(self, speed, color, name):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = False

    def go(self):
        if not self.__is_car_go:
            print('Машина поехала.')
            self.__is_car_go = not self.__is_car_go
        else:
            print('Машина едет.')

    def show_speed(self):
        print(f'Скорость {self.speed} км/ч')

    def stop(self):
        if self.__is_car_go:
            print('Машина остановилась.')
            self.__is_car_go = not self.__is_car_go
        else:
            print('Машина остановлена.')

    def turn(self, direction):
        if self.__is_car_go:
            if str(direction) in {'налево', 'направо'}:
                print(f'Машина повернула {direction}')
            else:
                print('Неверные данные!')
        else:
            print('Машина остановлена и не может совершать маневры.')

class TownCar(Car):
    __speed_limit = 60
    def show_speed(self):
        if self.speed > self.__speed_limit:
            print(f'Скорость превышена на {self.speed - self.__speed_limit} км/ч')
        super().show_speed()

class WorkCar(Car):
    __speed_limit = 40
    def show_speed(self):
        if self.speed > self.__speed_limit:
            print(f'Скорость превышена на {self.__speed_limit - self.speed}')
        super().show_speed()

class SportCar(Car):
    __is_engine_started = False
    def start_engine(self):
        if not self.__is_engine_started:
            print('Дрын-дын-дын...бух...дын-бдыщь')
            self.__is_engine_started = not self.__is_engine_started

    def stop_engine(self):
        if self.__is_engine_started:
            print('*двигатель остановлен*')
            self.__is_engine_started = not self.__is_engine_started

    def go(self):
        if self.__is_engine_started:
            super().go()
        else:
            print('Двигатель остановлен, вы не можете ехать.')

class PoliceCar(Car):
    __police_lights = False

    def __init__(self, speed, color, name):
        super().__init__(speed, color, name)
        self._is_police = True

    def police_lights(self):
        if not self.__police_lights:
            print('Маячки включены')
            self.__police_lights = not self.__police_lights
        else:
            print('Маячки выключены')
            self.__police_lights = not self.__police_lights

t_car = TownCar(80, 'white', 'Ford')
w_car = WorkCar(30, 'blue', 'KamAZ')
s_car = SportCar(380, 'red', 'Ferrari')
p_car = PoliceCar(400, 'blue/white', 'McLaren')

print('TownCar')
t_car.go()
t_car.go()
t_car.stop()
t_car.turn('направо')
t_car.go()
t_car.show_speed()

print('WorkCar')
w_car.go()
w_car.stop()
w_car.stop()
w_car.go()
w_car.turn('налево')
w_car.show_speed()

print('SportCar')
s_car.go()
s_car.start_engine()
s_car.go()
s_car.stop()
s_car.turn('направо')
s_car.go()
s_car.show_speed()

p_car.go()
p_car.stop()
p_car.stop()
p_car.go()
p_car.turn('налево')
p_car.show_speed()
p_car.police_lights()