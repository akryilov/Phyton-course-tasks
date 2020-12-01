# 4. Реализуйте базовый класс Car.
# У данного класса должны быть следующие атрибуты: speed, color, name, is_police (булево).
# А также методы: go, stop, turn(direction), которые должны сообщать,
# что машина поехала, остановилась, повернула (куда).
# Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar.
# Добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля.
# Для классов TownCar и WorkCar переопределите метод show_speed.
# При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.
#
# Создайте экземпляры классов, передайте значения атрибутов.
#
# Выполните доступ к атрибутам, выведите результат.
#
# Выполните вызов методов и также покажите результат.

# Create base class Car
class Car:
    def __init__(self, speed, color, name, is_police):
        # creation of class atributes: speed, color, name, is_police
        self.speed = int(speed)
        self.color = str(color)
        self.name = str(name)
        self.is_police = bool(is_police)

    #creation of class methods
    def go(self):
        print(f'the car {self.name} is moving')

    def stop(self):
        print(f'the car {self.name} stopped')

    def turn(self, direction):
        if direction == 'left':
            print(f'the car {self.name} turned left')
        if direction == 'right':
            print(f'the car {self.name} turned right')

    def car_info(self):
        print(f'car name:{self.name}\n car color:{self.color}\n')

    def show_speed(self):
        print(f'car {self.name} speed:{self.speed}')

#creation of child classes:

class TownCar(Car):

    def type(self):
        print('your choice is town car')

    def show_speed(self):
        if self.speed >= 60:
            print(f'the speed of car {self.name} exceeded')
        else:
            print(f'the speed of car {self.name} is not exceeded')

class SportCar(Car):

    def type(self):
        print('your choice is sport car')

class WorkCar(Car):

    def type(self):
        print('your choice is work car')

    def show_speed(self):
        if self.speed >= 40:
            print('speed exceeded')

class PoliceCar(Car):

    def type(self):
        print('your choice is police car')

    def police(self):
       if self.is_police:
          print('police car')
       else:
           print('not police car')

car_1 = TownCar(60, 'red', 'VW', False)
car_1.stop()
car_1.go()
car_1.turn('right')
car_1.show_speed()

car_2 = PoliceCar(20, 'green', 'Lada', True)
car_2.stop()
car_2.go()
car_2.turn('left')
car_2.show_speed()
car_2.police()
car_2.type()

car_3 = WorkCar(100, 'blue', 'KIA', False)
car_3.stop()
car_3.go()
car_3.turn('right')
car_3.show_speed()
car_3.type()