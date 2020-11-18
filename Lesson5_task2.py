# Создать текстовый файл (не программно), сохранить в нем несколько строк,
# выполнить подсчет количества строк, количества слов в каждой строке.

lines = 0  # Set the number of lines
word = 0  # Set the number of words

my_file = open('Lesson5_task2.txt', 'r')
print(my_file.readlines())  # print the lines from file
my_file.seek(0)  # set the cursor at zero bite

dict_1 ={}  # dictionary for printing the results in format "line: number of words in line"

for line in my_file:  # calculate the number of lines
    lines += 1
    for letter in line:
        if letter == ' ':  # end of 'word' checking criteria
            word += 1
        if letter == '\n':  # end of 'line' checking criteria
            word +=1
            dict_1[lines] = word  # add info about the # of words in the current line
            word = 0

print(f'number of lines is: {lines}')
print(f'"#line: #words" pairs: {dict_1}')

my_file.close()