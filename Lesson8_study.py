# Статические методы и методы класса

# Статический метод: Обращение к методам без создания экземпляра класса

# class DataBase:
#     # def __init__(self, x, w, e, r, t):
#     # x + 5
#
#     def connect(self):
#         print('connect')
#
#     @staticmethod  # обращение к методу без создания экземпляра класса
#     def select():
#         print('select')

# Как будет выглядеть код если я захочу запустить ф-цию селект:

# db = DataBase()
# db.select()
#
# DataBase.select(x=1)

# Но DataBase может содержать Init c обязательным типом аргументов:

# МЕТОДА КЛАССА:

# class MyClass:
#     def qwe(self):
#         print('')
#
#     @classmethod  # Первый аргумент cls -> ссылка на класс (My class в данном случае находится cls.) Зона видимости
#     def my_method(cls, param):
#         print(cls, param)
#         print(cls().qwe())
#
# MyClass.my_method(10)


## СИСТЕМНЫЕ АТРИБУТЫ:##########

class Customer:
    """Это класс покупатель"""
    def __init__(self, name, tel):
        self.name = name
        self.tel = tel

john = Customer('John', 453523425)
# print(john.__dict__)  # ключи - это имя атрибутов в атрибуте dict
# print(john.__doc__)  # комментарии сохраняется в системный атрибут doc. Можем писать документацию """ """
# my_int = 5
# print(my_int.doc)
# print(john.__class__.__name__)
# print(john.__module__)

#################################

## СОЗДАНИЕ ООП ПРОГРАММЫ ##

# Разработать виртуальныю модель образовательного процесса, учитель, ученики

#Расставление пробелов: Ctrl + Alt + l
#Дублирование строки Ctrl + D

# class Person:
#     def __init__(self, name, surname):
#         self.name = name
#         self.surname = surname
#
#     def __str__(self):
#         return f'{self.name} {self.surname}'
#
# class Teacher(Person):
#     def to_teach(selfself, subj, *puplis):
#         for pupil in puplis:
#             pupil.to_take(subj)
#
# class Pupil(Person):
#     def __init__(self, name, surname):
#         super().__init__(name,surname)
#         self.knowledge = []
#
#     def to_take(self, subj):
#         self.knowledge.append(subj)
#
# class Subject:
#     def __init__(self, *subjects):
#         self.subjects = subjects
#
#     def __str__(self):
#         return f'{self.subjects}'
#
# s = Subject('math', 'physics')
# print(s)
# t = Teacher('Ivan', 'Ivanov')
# p_1 = Pupil('Petr', 'Petrov')
# p_2 = Pupil('Sidr', 'Sidorov')
# p_3 = Pupil('Alesha', 'Aleshin')
#
# t.to_teach(s, p_1, p_2)
# print(p_1.knowledge)  # Лист
# print(p_1.knowledge)  # пустой лист
#
# print(p_1.knowledge[0])
# print(p_2.knowledge[0])
# print(p_3.knowledge[0])


##### СОЗДАНИЕ ИСКЛЮЧЕНИЙ #####

# class BelowZero(Exception): # Можно наследоваться от базового класса
#     pass
#
# user = int(input('Введите положительное число: '))
#
# if user < 0:
#     print('Неверно')
#     raise BelowZero()
#
# class MyDist(dict):  # Модифицированный дикт
#     pass


###### PIP ####

import time
import math

import numpy
import pandas

# Заходим в консоль
# Сайт с модулями: pypi.org

#### Виртуальная среда #####
Под каждый проект создают све окружение (см. урок)

