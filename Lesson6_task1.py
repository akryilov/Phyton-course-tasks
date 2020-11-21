# 1. Создать класс TrafficLight (светофор) и определить у него один атрибут color (цвет) и метод running (запуск).
# Атрибут реализовать как приватный.
# В рамках метода реализовать переключение светофора в режимы: красный, желтый, зеленый.
# Продолжительность первого состояния (красный) составляет 7 секунд, второго (желтый) — 2 секунды, третьего (зеленый)
# — на ваше усмотрение.
# Переключение между режимами должно осуществляться только в указанном порядке (красный, желтый, зеленый).
# Проверить работу примера, создав экземпляр и вызвав описанный метод.



from itertools import cycle  # import cycle function from "itertools" module
import time  # import "time" module


class TrafficLight:  # creating TrafficLight class
    def __init__(self):  # initialization
        self._color = ['Red', 'Yellow', 'Green']  # 'colors' attribute

    def running(self):  # creating 'running' method
        for el in cycle(self._color):
            if el == 'Red':
                print(el)
                time.sleep(7)
            if el == 'Yellow':
                print(el)
                time.sleep(2)
            if el == 'Green':
                print(el)
                time.sleep(10)


traffic_light_1 = TrafficLight()  # instantiating 'traffic_light_1' object of 'TrafficLight' class
traffic_light_1.running()  # call 'running' method for 'traffic_light_1' object

