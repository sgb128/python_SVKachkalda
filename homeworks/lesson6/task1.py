"""
Создать класс TrafficLight (светофор) и определить у него один атрибут color (цвет) и метод running (запуск).
Атрибут реализовать как приватный. В рамках метода реализовать переключение светофора в режимы: красный, желтый,
зеленый. Продолжительность первого состояния (красный) составляет 7 секунд, второго (желтый) — 2 секунды,
третьего (зеленый) — на ваше усмотрение. Переключение между режимами должно осуществляться только в указанном
порядке (красный, желтый, зеленый). Проверить работу примера, создав экземпляр и вызвав описанный метод.

Задачу можно усложнить, реализовав проверку порядка режимов, и при его нарушении выводить соответствующее
сообщение и завершать скрипт.
"""

import time
from itertools import cycle
# мои светофоры можно запускать с задержкой, то есть они могут быть не синхронизированны
# правда пока не понял откуда задержка при запуске, вероятно ждет первые 7 секунд при установке красного света в первом светофоре
class TrafficLight:
    # режимы
    __lights = (('выключен', 0), ('красный', 7), ('желтый', 2), ('зеленый', 3))

    # инициализация
    def __init__(self, lighter_id, lighter_start):
        self.__color = self.__lights[0][0]
        self.__next_light = 1
        self.__time = time.time() + lighter_start
        self.__return_vector = True
        self.lighter_id = lighter_id

    def running(self):
        # здесь я решил запустить цикл не по времени переключения светофора, чтобы у меня выводилось текущее состояние
        # светофора (выключен или какой цвет горит)
        tmp_time = time.time()
        while True:
            if time.time() >= tmp_time + 1:
                tmp_time = time.time()
                yield self.__light_trigger()



    def __light_trigger(self):
        # собственно сам переключатель, с условиями я конечно же намудрил, но главное ведь работает! :)
        if self.__time + self.__lights[self.__next_light][1] <= time.time(): # здесь проверяем "тик" таймера
            if self.__return_vector: # здесь проверяем в каком направлении будем менять цвет светофора
                                     # от красного к зеленому или в обратную сторону
                if self.__next_light > 1: # если дошли до 1го элемента - то переключаем направление
                    self.__next_light -= 1
                else:
                    self.__return_vector = not self.__return_vector
                    self.__next_light += 1
                self.__time = time.time()
            else:
                if self.__next_light < 3: # если дошли до 4го элемента - то переключаем направление
                    self.__next_light += 1
                else:
                    self.__return_vector = not self.__return_vector
                    self.__next_light -= 1
                self.__time = time.time()
        return str(self.lighter_id) + ' ' + self.__lights[self.__next_light][0] # выводим значение каким бы оно ни было

lighter1 = TrafficLight(1, 0)
lighter2 = TrafficLight(2, 3)
lighter3 = TrafficLight(3, 6)

# ну и мне не нужен enumerate, так как я задал дополнительное свойство отвечающее за id светофора
for lighters in cycle(zip(lighter1.running(), lighter2.running(), lighter3.running())):
    print(lighters)