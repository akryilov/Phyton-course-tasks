import random
from random import randint
# import itertools
import time


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

     # """формирование таблицы игрока"""
    def card_output(self, card):
        if self.name == 'Игрок':
            print(f"Игрок:\n{26*'-'}")
        if self.name == 'Компьютер':
            print(f"Компьютер:\n{26 * '-'}")
        for i in range(0, len(card), 9):
            self.temp_list2 = card[i:i + 9]
            print(' '.join(map(str, self.temp_list2)))
        print(f"{26*'-'}")


class LotoGame(LotoCard):
    def __init__(self, human_player, pc_player):
        self.h_p_temp_list = human_player.temp_list
        self.h_p_len_4 = human_player.len_4
        self.pc_player_len_4 = pc_player.len_4
        self.pc_p_temp_list = pc_player.temp_list

    def start(self):
        self.start_time = time.time()
        human_player.card_output(self.h_p_temp_list)  # сформировали карточку игрока
        pc_player.card_output(self.pc_p_temp_list)  # сформировали карточку компьютера
        boch_num_range = list(range(1, 91))  # диапазон номеров боченков от 1 до 90

        while True:

            print(f"Ваши очки: {self.h_p_len_4.count('xx')} из 15")
            print(f"Очки компьютера: {self.pc_player_len_4.count('xx')} из 15")

            if self.h_p_len_4.count('xx') == 3 and self.pc_player_len_4.count('xx') == 3:
                print('Ничья!')
                break

            if self.h_p_len_4.count('xx') == 3:
                print('Вы победитель!')
                print(f'Время игры: {int(time.time() - start_time)} секунд(ы)')
                break

            elif self.pc_player_len_4.count('xx') == 3:
                print('Вы проиграли!')
                break

            boch = random.sample(boch_num_range,1)  # цикл для каждого номера боченка ищем элемент
            boch_num_range.remove(boch[0])  # исключение выпавшего боченка из списка
            print(f'Осталось боченков: {len(boch_num_range)}\n{26 * "-"}\n№ Боченка: {boch[0]}')  # выводим информацию о боченках

            print('Зачеркнуть цифру? (y/n)')
            your_choice = input()
            """зачеркивание номера в карте игрока"""
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
                    print('Вы проиграли!')
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
                    print('Вы проиграли!')
                    break
            # """зачеркивание номера в карте компьютера"""
            if boch[0] in self.pc_player_len_4:
                for item in range(len(self.pc_player_len_4)):
                    if self.pc_player_len_4[item] == boch[0]:
                        self.pc_player_len_4[item] = 'xx'
                        self.pc_p_temp_list = ['{:2}'.format(x) for x in self.pc_player_len_4]
                        print(f"Компьютер:\n{26 * '-'}")
                        for i in range(0, len(self.pc_player_len_4), 9):
                            self.h_p_temp_list2 = self.pc_p_temp_list[i:i + 9]
                            print(' '.join(map(str, self.h_p_temp_list2)))
                        print(f"{26 * '-'}")
            else:
                if boch[0] not in self.pc_player_len_4:
                    # for i in range(0, len(len_4), 9):
                    #     print(f'{len_4[i:i + 9]}')
                    self.pc_p_temp_list = ['{:2}'.format(x) for x in self.pc_player_len_4]
                    print(f"Компьютер:\n{26 * '-'}")
                    for i in range(0, len(self.pc_player_len_4), 9):
                        self.h_p_temp_list2 = self.pc_p_temp_list[i:i + 9]
                        print(' '.join(map(str, self.h_p_temp_list2)))
                    print(f"{26 * '-'}")
        # else:
        #     if self.h_p_len_4.count('xx') == 3:
        #         print('Вы победитель!')
        #
        #     elif self.pc_player_len_4.count('xx') == 3:
        #         print('Вы проиграли!')


human_player = LotoCard('Игрок')
# human_player.create_card()
# human_player.create_card()
# print(human_player)

pc_player = LotoCard('Компьютер')
# pc_player.create_card()
# print(pc_player)
game = LotoGame(human_player, pc_player)
game.start()