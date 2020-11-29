"""
== Лото ==

Правила игры в лото.

Игра ведется с помощью специальных карточек, на которых отмечены числа,
и фишек (бочонков) с цифрами.

Количество бочонков — 90 штук (с цифрами от 1 до 90).

Каждая карточка содержит 3 строки по 9 клеток. В каждой строке по 5 случайных цифр,
расположенных по возрастанию. Все цифры в карточке уникальны. Пример карточки:

--------------------------
    9 43 62          74 90
 2    27    75 78    82
   41 56 63     76      86
--------------------------

В игре 2 игрока: пользователь и компьютер. Каждому в начале выдается
случайная карточка.

Каждый ход выбирается один случайный бочонок и выводится на экран.
Также выводятся карточка игрока и карточка компьютера.

Пользователю предлагается зачеркнуть цифру на карточке или продолжить.
Если игрок выбрал "зачеркнуть":
    Если цифра есть на карточке - она зачеркивается и игра продолжается.
    Если цифры на карточке нет - игрок проигрывает и игра завершается.
Если игрок выбрал "продолжить":
    Если цифра есть на карточке - игрок проигрывает и игра завершается.
    Если цифры на карточке нет - игра продолжается.

Побеждает тот, кто первый закроет все числа на своей карточке.

Пример одного хода:

Новый бочонок: 70 (осталось 76)
------ Ваша карточка -----
 6  7          49    57 58
   14 26     -    78    85
23 33    38    48    71
--------------------------
-- Карточка компьютера ---
 7 87     - 14    11
      16 49    55 88    77
   15 20     -       76  -
--------------------------
Зачеркнуть цифру? (y/n)

Подсказка: каждый следующий случайный бочонок из мешка удобно получать
с помощью функции-генератора.

Подсказка: для работы с псевдослучайными числами удобно использовать
модуль random: http://docs.python.org/3/library/random.html

"""

import random
from random import randint
import itertools

# class LotoCard:
#     def __init__(self, name):
#         self.name = name
#
#     def create_card(self):
#         if name == 'Игрок':
#         iter = int
#             for el in range(1,90):
#                 iter += random

"""
numbers = list()
zeros = [' ', ' ', ' ', ' ']
for el in range(3):
    # numbers.append(randint(1, 90))  # 
    numbers.append(random.sample(range(1, 90), 5))  # сгенерировали 5 цифр из списка от 1 о 90
    numbers[el].sort()  # отсортировали по возрастанию
    print(numbers[el])
    
for el in range(4):
    numbers.insert(randint(0, len(numbers)), 0)  # добавили 4 нуля в произвольном порядке
# c = numbers + zeros  # сложили со списком нулей
# random.shuffle(c)    # перемешали в случайном порядке
# for id, el in enumerate(c):
#     while id <= len(c):
#         if c[id] != ' ' and c[id+1] != 0:
#             if c[id] > c[id+1]:
#                 x = c[id]
#                 c[id] = c[id+1]
#                 c[id+1] = x
#                 id += 1
#         else:
#             id += 1
# print(c)
print(str(numbers))
"""
#########################
numbers = list()

numbers = random.sample(range(1, 90), 15)  # сгенерировали 15 цифр из списка от 1 о 90 в случайном порядке
# numbers.sort()  # отсортировали по возрастанию

print(numbers)

len_1 = numbers[:5]  # делим список на 3 части
len_1.sort()  # и сортируем список
for el in range(4):  # добавляем 4 нуля в произвльном порядке
    len_1.insert(randint(0, len(len_1)), 0)   # insert вставляет в список len_1 на значение индекса из randint(0, len(len_1)) значение 0

len_2 = numbers[5:10]
len_2.sort()
for el2 in range(4):
    len_2.insert(randint(0, len(len_2)), 0)

len_3 = numbers[10:15]
len_3.sort()
for el3 in range(4):
    len_3.insert(randint(0, len(len_3)), 0)

print(numbers)
print(len_1 + len_2 + len_3)
len_4 = len_1 + len_2 + len_3
######## Поиск элемента в списках #####
"""
boch = randint(1, 90)  # цикл для каждого номера боченка ищем элемент
print(f'# bochenka: {boch}')
"""
### Замена элемента в общем списке:

# length = len(len_4)
# while True:
#     boch = randint(1, 90)  # цикл для каждого номера боченка ищем элемент
#     print(f'# bochenka: {boch}')
#     print('Зачеркнуть цифру? (y/n)')
#     your_choice = input()
#     print(type(your_choice))
#     if your_choice == 'y':
#         if boch in len_4:
#             for item in range(len(len_4)):
#                 if len_4[item] == boch:
#                     len_4[item] = 'x'
#                     for i in range(0, len(len_4), 9):
#                         print(f'{str(len_4[i:i + 9])}')
#         else:
#             print('Вы проиграли')
#             break
#     elif your_choice == 'n':
#         if boch not in len_4:
#             # for i in range(0, len(len_4), 9):
#             #     print(f'{len_4[i:i + 9]}')
#             temp_list = ['{:3}'.format(x) for x in len_4]
#             for i in range(0, len(temp_list), 9):
#                 temp_list2 = temp_list[i:i + 9]
#                 print(' '.join(map(str, temp_list2)))
#
#         else:
#             print('Вы проиграли')
#             break

line_4 = [5, 0, 24, 0, 27, 29, 0, 46, 0, 0, 7, 33, 0, 55, 0, 68, 89, 0, 0, 30, 0, 49, 0, 0, 59, 70, 79]

temp_list = ['{:3}'.format(x) for x in line_4]
print(temp_list)
for i in range(0, len(temp_list), 9):
    temp_list2 = temp_list[i:i + 9]
    print(' '.join(map(str, temp_list2)))

# print(f'{line_4[:9]}\n{line_4[9:18]}\n{line_4[18:27]}')
