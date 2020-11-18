# Создать программно файл в текстовом формате, записать в него построчно данные,
# вводимые пользователем. Об окончании ввода данных свидетельствует пустая строка.

my_file = open("Lesson5_task1.txt", "w")  # Open file for writing
while True:
    text_line = input('Enter the data:')
    my_file.write(text_line + '\n')  # Writing the entered data into file

    if text_line == '':  # Checking for empty line
        print('The data has been entered')
        my_file.close()
        my_file = open("Lesson5_task1.txt", "r")  # Open file for reading and print the result
        print(f'The data from file: \n{my_file.readlines()}')
        my_file.close()
        break

