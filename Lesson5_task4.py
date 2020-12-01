# 4. Создать (не программно) текстовый файл со следующим содержимым:
# One — 1
# Two — 2
# Three — 3
# Four — 4
# Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные.
# При этом английские числительные должны заменяться на русские.
# Новый блок строк должен записываться в новый текстовый файл.


my_file = open('Lesson5_task4.txt', 'r', encoding='utf-8')

print(my_file.readlines())  # print the lines from file
my_file.seek(0)  # set the cursor at zero byte

my_file2 = open('Lesson5_task4_1.txt', 'w', encoding='utf-8')

Name_2 = []  # New line object for changing the names

for line in my_file:  # calculate the number of lines
    for name in line:
        if name == '—':
            Name = line[0:line.index('—') - 1]  # Parsing the name from line until '-' symbol
            if Name == 'One':
                Name_2 = 'Один' + line[line.index('—')-1:len(line)]
                my_file2.write(Name_2)
            elif Name == 'Two':
                Name_2 = 'Два' + line[line.index('—') - 1:len(line)]
                my_file2.write(Name_2)
            elif Name == 'Three':
                Name_2 = 'Три' + line[line.index('—') - 1:len(line)]
                my_file2.write(Name_2)
            elif Name == 'Four':
                Name_2 = 'Четыре' + line[line.index('—') - 1:len(line)]
                my_file2.write(Name_2)
my_file.close()

my_file2 = open('Lesson5_task4_1.txt', 'r', encoding='utf-8')
print(my_file2.readlines())  # print the lines from file

my_file2.close()
