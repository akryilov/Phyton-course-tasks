# перегрузка операторов или перегрузка системных методов

# class Car:
#     def __init__(self):
#         self.modules = []
#         self._fc = 10
#
#     def __add__(self, other):
#         self.modules.append(other)
#         return self  # важно при сложении нескольких
#
#     def __str__(self): # описание ф-ции str
#         return f'{self.modules}'
#
#     def __del__(self):  # если ссылок на объект нет, то мы можем его удалить с исп. этого метода. Деструктор вызывается в момент удаления объекта.
#         print('Объект удален')
#
#     def __setattr__(self, key, value):
#         super().__setattr__(key, value)  # реализация старого функионала
#         # self.__dict__[key] = value
#         print(f'Добавлен атрибут {key} со значением {value}')
#
#     def __getitem__(self, item):
#         return self.modules[item]
#
#     def __call__(self, price = None):
#         self.prince = price
#         print(f'Full car info\nmodules: {self.modules}\nprice: {price}')
#
#     def __eq__(self, other):
#         return self._fc == other
#
# car = Car()
# module1 = 'теплый руль'
# module2 = 'парктроник'
# module3 = 'розовый ручник'
#
# # неудобно добавлять модули
# car.modules.append(module1)
# car.modules.append(module2)
# car.modules.append(module3)
#
# # заменяем на
#
# car + module1 # эквивалентно car.__add__(module1)
# car + module2
# car + module3
#
# car + module1 + module2 + module3
# car.model = 'Tesla'
# qwe = str(car)
# print(qwe)
#
# print(car)
# print(car[1]) # отработка getitem
#
# car(5000)
# car()
#
# print(car == 7) # воод описания для модцля eq

# ПЕРЕОПРЕДЕЛЕНИЕ МЕТОДА
 # см прошлый урок

# ИНТЕРФЕЙСЫ:

# есть в ДЗ (реализация абстрактного класса):

# from abc import ABC, abstractmethod
#
# class MyAbsClass(ABC):
#     @abstractmethod
#     def my_method(self):  # здесь пишем только
#         pass
#
#     @abstractmethod
#     def my_method2(self):
#         pass
#
# class MyClass(MyAbsClass):
#     # необходимо реализовать ранее обозначенные методы
#     def my_method1(self):
#         print('we')
#
#     def my_method2(self):
#         print('we')
#
# mc = MyClass()
#

# Интерфейс итерации:

# for x in [1, 2, 3]: # iter? -> object -> next -> next -> StopIteration
#     print(x)

# class Iterator:
#     def __init__(self):
#         self.i = 0
#
#     def __iter__(self):
#         return self
#
#     def __next__(self):
#         self.i +=1
#         if self.i <= 5:
#             return self.i
#         else:
#             raise StopIteration
#
# qwe = Iterator()
#
# for i in qwe:
#     print(i)


# ДЕКОРАТОР Prperty

# class Human:
#     def __init__(self, name, age):
#         self.name = name
#         self._age = age
#
#     @property  # обращение к методу внешне как к атрибуту
#     def age(self):  # переделали из атрибута в метод
#         # check age
#         return self._age
#
#     # many codes
#     # many codes
#
# human = Human('Ivan', 20)
# print(human.age)


# КОМПОЗИЦИЯ: СОЗДАНИЕ КЛАССА КОНТЕЙНЕР С ВХОДЯЩИМИ ДРУГИМИ КЛАССАМИ

class WinDorr:
    #области окон и дверей
    def __init__(self, lenght, width):
        self.square = lenght * width

class Room:
    def __init__(self, len1, len2, h):
        self.square = 2 * h * (len1 + len2) # площадь комнаты за вычетом потолка и пола
        self.wd = []

    def add_windoor(self, w, l):
        self.wd.append(WinDorr(w,l)) # Хранилище экземпляров класса

    def common_square(self):
        main_square = self.square
        for el in self.wd:
            main_square -=el.square
            return main_square

    r = Room(10, 20, 4)
    print(r.square)
    r.add_windoor(2,2)
    r.add_windoor(2,1)

    ДЗ:
