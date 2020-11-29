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

class LotoCard:
    def __init__(self, name):
        self.name = name
    #
    # def create_card(self):
        if self.name == 'Игрок' or self.name == 'Компьютер':
            self.numbers = list()
            self.numbers = random.sample(range(1, 90), 15)

            self.len_1 = self.numbers[:5]  # делим список на 3 части
            self.len_1.sort()  # и сортируем список
            for el_1 in range(4):  # добавляем 4 нуля в произвльном порядке
                self.len_1.insert(randint(0, len(self.len_1)), ' ')  # insert вставляет в список len_1 на значение индекса из randint(0, len(len_1)) значение 0

            self.len_2 = self.numbers[5:10]
            self.len_2.sort()
            for el_2 in range(4):
                self.len_2.insert(randint(0, len(self.len_2)), ' ')

            self.len_3 = self.numbers[10:15]
            self.len_3.sort()
            for el_3 in range(4):
                self.len_3.insert(randint(0, len(self.len_3)), ' ')
            self.len_4 = self.len_1 + self.len_2 + self.len_3
            # print(self.len_4)
            self.temp_list = ['{:2}'.format(x) for x in self.len_4]
            # print(f'temp: {self.temp_list}')

            # for i in range(0, len(self.temp_list), 9):
            #     self.temp_list2 = self.temp_list[i:i + 9]
            #     print(' '.join(map(str, self.temp_list2)))
            pass

class LotoGame(LotoCard):
    def __init__(self, human_player, pc_player):
        self.h_p_temp_list = human_player.temp_list
        self.h_p_len_4 = human_player.len_4
        self.pc_player = pc_player

        """формирование таблицы игрока"""
        print(f"Игрок:\n{26*'-'}")
        for i in range(0, len(self.h_p_temp_list), 9):
            self.temp_list2 = self.h_p_temp_list[i:i + 9]
            print(' '.join(map(str, self.temp_list2)))
        print(f"{26*'-'}")

        """формирование таблицы компьютера"""
        print(f"Компьютер:\n{26*'-'}")
        for i in range(0, len(pc_player.temp_list), 9):
            self.temp_list3 = pc_player.temp_list[i:i + 9]
            print(' '.join(map(str, self.temp_list3)))
        print(f"{26*'-'}")

        boch_num_range = list(range(1, 91))  # диапазон номеров боченков от 1 до 90
        # print(boch_num_range)

        while True:
            boch = random.sample(boch_num_range,1)  # цикл для каждого номера боченка ищем элемент
            boch_num_range.remove(boch[0])  # исключение выпавшего боченка из списка
            print(f'№ боченка: {boch[0]}\nосталось боченков: {len(boch_num_range)}')


            print('Зачеркнуть цифру? (y/n)')
            your_choice = input()
            if your_choice == 'y':
                if boch[0] in self.h_p_len_4:
                    for item in range(len(self.h_p_len_4)):
                        if self.h_p_len_4[item] == boch[0]:
                            self.h_p_len_4[item] = 'xx'
                            self.h_p_temp_list = ['{:2}'.format(x) for x in self.h_p_len_4]
                            print(f"Игрок:\n{26 * '-'}")
                            for i in range(0, len(self.h_p_temp_list), 9):
                                self.h_p_temp_list2 = self.h_p_temp_list[i:i + 9]
                                print(' '.join(map(str, self.h_p_temp_list2)))
                            print(f"{26 * '-'}")
                else:
                    print('Вы проиграли')
                    break
            elif your_choice == 'n':
                if boch[0] not in self.h_p_len_4:
                    # for i in range(0, len(len_4), 9):
                    #     print(f'{len_4[i:i + 9]}')
                    self.h_p_temp_list = ['{:2}'.format(x) for x in self.h_p_len_4]
                    print(f"Игрок:\n{26 * '-'}")
                    for i in range(0, len(self.h_p_temp_list), 9):
                        self.h_p_temp_list2 = self.h_p_temp_list[i:i + 9]
                        print(' '.join(map(str, self.h_p_temp_list2)))
                    print(f"{26 * '-'}")
                else:
                    print('Вы проиграли')
                    break



human_player = LotoCard('Игрок')
# human_player.create_card()
# human_player.create_card()
# print(human_player)

pc_player = LotoCard('Компьютер')
# pc_player.create_card()
# print(pc_player)
game = LotoGame(human_player, pc_player)