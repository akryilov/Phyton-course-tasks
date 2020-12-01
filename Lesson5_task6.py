# 6. Необходимо создать (не программно) текстовый файл,
# где каждая строка описывает учебный предмет и наличие лекционных,
# практических и лабораторных занятий по этому предмету и их количество.
# Важно, чтобы для каждого предмета не обязательно были все типы занятий.
# Сформировать словарь, содержащий название предмета и общее количество занятий по нему.
# Вывести словарь на экран.
#
# Примеры строк файла:
# Информатика: 100(л) 50(пр) 20(лаб).
# Физика: 30(л) — 10(лаб)
# Физкультура: — 30(пр) —
#
# Пример словаря:
# {“Информатика”: 170, “Физика”: 40, “Физкультура”: 30}

my_file = open('Lesson5_task6.txt', 'r', encoding='utf-8')

Name = []  # list with names of disciplines
sum_1 = []  # list with sum of study hours

for line in my_file:  # calculate the number of lines
    integ = []
    i = 0
    print(line)  # print the line from file
    l = len(line)  # calculate the length of line
    for name in line:
        if name == ':':
            Name.append(line[0:line.index(':')])  # Parsing the name from line
            print(Name)
    while i < l:  # parsing thru lenght line
        s_int = ''
        a = line[i]  # bring the symbol with i index
        while '0' <= a <= '9':  # checking if the symbol is number or not
            s_int += a  # if the number then add to previous to get the full number
            i += 1  # step on the next symbol
            if i < l:
                a = line[i]  # bring the next symbol for checking
            else:
                break  # if the end of the line achieved then break
        i += 1
        if s_int != '':
            integ.append(int(s_int))  # add number in the list integ

    sum_1.append(sum(int(el) for el in integ))  # sum all numbers in list and place in the new list

my_file.close()
print(sum_1)

dict_my = dict(zip(Name, sum_1))  # create the final dictionary
print(dict_my)
