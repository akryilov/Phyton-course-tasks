# 7. Создать (не программно) текстовый файл,
# в котором каждая строка должна содержать данные о фирме:
# название, форма собственности, выручка, издержки.
# Пример строки файла: firm_1 ООО 10000 5000.
#
# Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а также среднюю прибыль.
#
# Если фирма получила убытки, в расчет средней прибыли ее не включать.
# Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями,
# а также словарь со средней прибылью.
#
# Если фирма получила убытки, также добавить ее в словарь (со значением убытков).
# Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].
# Итоговый список сохранить в виде json-объекта в соответствующий файл.
# Пример json-объекта:
# [{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit": 2000}]
#
# Подсказка: использовать менеджеры контекста.

from itertools import groupby  # import module groupby to group names of firms
import json  # import json module

Name = []  # List of firm's names
Name_2 = []  # Final list of names

profit = 0  # Variable for profit calc
i2 = 0  # Variable for number of firm with profit

final_numbers = []  # list for profit or loss results

final_list = []  # Final list for creating the requested results

with open("Lesson5_task7.txt", "r", encoding='utf-8') as my_file:
    for line in my_file:  # calculate the number of lines
        integ = []  # list of all numbers in line
        i = 0
        l = len(line)  # calculate the lenght of line
        for name in line:
            if name == ' ':
                Name.append(line[0:line.index(' ')])  # Parsing the name from line
        while i < l:  # parsing thru lenght line
            s_int = ''
            a = line[i]  # calculate the length of line
            while '0' <= a <= '9':  # checking if the symbol is number or not
                s_int += a  # if the number then add to previous to get the full number
                i += 1
                if i < l:
                    a = line[i]  # bring the next symbol for checking
                else:
                    break
            i += 1
            if s_int != '':
                integ.append(int(s_int))
        integ.pop(0)  # delete zero value from list since it includes the firm number
        for el in integ:  # calc the profit or loss
            if el > int(integ[1]):
                i2 += 1
                final_numbers.append(integ[0] - integ[1])
                profit += (integ[0] - integ[1])
            else:
                final_numbers.append(integ[0] - integ[1])
    my_file.close()

Name_2 = [el for el, _ in groupby(Name)]  # list of firm's names
final_numbers = [el for el, _ in groupby(final_numbers)]  # list of profits or losses
dict_1 = dict(zip(Name_2, final_numbers))  # dict with names/profits or losses
dict_2 = {'avg profit': profit / i2}  # dict with avg profits

final_list.append(dict_1)  # put dict 1 into list
final_list.append(dict_2)  # put dict 2 into list
print(f'final list is: {final_list}')  # print the final list

with open("Lesson5_task7.json", "w") as write_f:  # save the list as .json object
    json.dump(final_list, write_f)
